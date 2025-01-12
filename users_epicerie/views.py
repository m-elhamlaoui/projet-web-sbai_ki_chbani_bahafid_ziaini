from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Avg, Count, Sum
from django.http import JsonResponse
from admins_epicerie.models import Produit, Categorie
from admins_epicerie.models import *
from users_epicerie.models import *
from .models import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password
import os
from django.utils import timezone




def index(request):
    # Affichage des produits
    produits = Produit.objects.annotate(
        totalNote=Avg('note__note'),
        totalU=Count('note__id_utilisateur')
    ).filter(qte_en_stock__gt=0)

    # Derniers produits (Wrapper 1, 2, 3)
    derniers_produits = Produit.objects.annotate(
        totalNote=Avg('note__note')
    ).order_by('-date_ajout')[:12]  # Récupère les 12 derniers produits

    # Produits recommandés
    produits_recommandes = Produit.objects.annotate(
        total=Count('recommandation__id_produit')
    ).order_by('-total')[:10]

    # Meilleures ventes
    meilleures_ventes = LigneCommande.objects.values('id_produit').annotate(
        total=Sum('qte')
    ).order_by('-total')[:8]
    produits_meilleures_ventes = Produit.objects.filter(id_produit__in=[mv['id_produit'] for mv in meilleures_ventes])

    # Produits indisponibles
    produits_indisponibles = Produit.objects.annotate(
        totalNote=Avg('note__note'),
        totalU=Count('note__id_utilisateur')
    ).filter(qte_en_stock=0)

    # Avis sur GestEpice
    avis = AvisService.objects.select_related('id_utilisateur').all()

    # Catégories
    categories = Categorie.objects.all()

    # Produits les plus commentés
    produits_commentes = Produit.objects.annotate(
        totalAvisP=Count('avisproduit__id_avis_produit')
    ).order_by('-totalAvisP')

    # Catégories de produits
    categories_produits = Produit.objects.select_related('id_categorie').all()


    # Contexte à passer au template
    context = {
        'produits': produits,
        'derniers_produits': derniers_produits,
        'produits_recommandes': produits_recommandes,
        'produits_meilleures_ventes': produits_meilleures_ventes,
        'produits_indisponibles': produits_indisponibles,
        'avis': avis,
        'categories': categories,
        'produits_commentes': produits_commentes,
        'categories_produits': categories_produits,
    }

    return render(request, 'index.html', context)




def quickview(request, id_produit):
    # Récupérer le produit en fonction de l'id_produit
    produit = get_object_or_404(Produit, id_produit=id_produit)

    # Calculer la note moyenne et le nombre total d'utilisateurs ayant noté le produit
    notes = Note.objects.filter(id_produit=produit).aggregate(
        totalNote=Avg('note'),
        totalU=Count('id_utilisateur')
    )

    # Récupérer les avis associés au produit
    avis_produits = AvisProduit.objects.filter(id_produit=produit).select_related('id_utilisateur')

    # Récupérer la catégorie du produit
    categorie = Categorie.objects.get(id_categorie=produit.id_categorie.id_categorie)

    # Contexte à passer au template
    context = {
        'produit': produit,
        'totalNote': notes['totalNote'],
        'totalU': notes['totalU'],
        'avis_produits': avis_produits,
        'categorie': categorie,
    }

    return render(request, 'quickview.html', context)



def recherche(request):
    # Récupérer les paramètres de recherche
    mot_recherche = request.GET.get('search', '')
    categorie_id = request.GET.get('category_id', '')

    # Filtrer les produits en fonction des paramètres de recherche
    produits = Produit.objects.all()

    if mot_recherche:
        produits = produits.filter(nom_produit__icontains=mot_recherche)
    if categorie_id:
        produits = produits.filter(id_categorie=categorie_id)

    # Annoter les produits avec la note moyenne et le nombre d'utilisateurs
    produits = produits.annotate(
        totalNote=Avg('note__note'),
        totalU=Count('note__id_utilisateur')
    )

    # Récupérer toutes les catégories pour le filtre
    categories = Categorie.objects.all()

    # Contexte à passer au template
    context = {
        'produits': produits,
        'categories': categories,
        'mot_recherche': mot_recherche,
        'categorie_id': categorie_id,
    }

    return render(request, 'recherche.html', context)



def product_detail(request, id_produit):
    # Récupérer le produit en fonction de l'id_produit
    produit = get_object_or_404(Produit, id_produit=id_produit)

    # Récupérer toutes les catégories
    categories = Categorie.objects.all()

    # Récupérer les avis associés au produit
    avis_produits = AvisProduit.objects.filter(id_produit=produit).select_related('id_utilisateur', 'id_note')

    # Calculer le total des commentaires
    total_commentaires = AvisProduit.objects.filter(id_produit=produit).aggregate(total=Count('id_avis_produit'))

    # Calculer la note moyenne du produit
    note_moyenne = Note.objects.filter(id_produit=produit).aggregate(moyenne=Avg('note'))

    # Contexte à passer au template
    context = {
        'produit': produit,
        'categories': categories,
        'avis_produits': avis_produits,
        'total_commentaires': total_commentaires['total'],
        'note_moyenne': note_moyenne['moyenne'],
    }

    return render(request, 'product.html', context)


def ajouter_avis_produit(request):
    if request.method == 'POST':
        # Use request.POST to access form data
        avis_produit = request.POST.get('avis_produit')
        id_utilisateur = request.POST.get('id_utilisateur')
        id_produit = request.POST.get('id_produit')
        note = request.POST.get('rating')

        if avis_produit and id_utilisateur and id_produit and note:
            utilisateur = get_object_or_404(Utilisateur, id_utilisateur=id_utilisateur)
            produit = get_object_or_404(Produit, id_produit=id_produit)

            # Créer une nouvelle note
            nouvelle_note = Note.objects.create(
                id_utilisateur=utilisateur,
                id_produit=produit,
                note=note
            )

            # Créer un nouvel avis produit
            nouvel_avis = AvisProduit.objects.create(
                id_utilisateur=utilisateur,
                id_produit=produit,
                avis_produit=avis_produit,
                id_note=nouvelle_note
            )

            return JsonResponse({'status': 'success', 'message': 'Votre avis a été enregistré avec succès.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Veuillez vous connecter pour pouvoir ajouter un avis sur un produit.'})
    else:
        return JsonResponse({'status': 'errorFatal', 'message': 'Méthode non autorisée.'})


def recommander_produit(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire via request.POST
        product_id = request.POST.get('product_id')
        user_id = request.session.get('id_utilisateur')  # Récupérer l'ID de l'utilisateur depuis la session

        if not user_id:
            # Si l'utilisateur n'est pas connecté, retourner une erreur
            return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté.'}, status=401)

        if product_id and product_id != '-2':  # Vérifier que l'ID du produit est valide
            # Vérifier si l'utilisateur a déjà recommandé ce produit
            recommandation_exists = Recommandation.objects.filter(
                id_produit=product_id,
                id_utilisateur=user_id
            ).exists()

            if not recommandation_exists:
                # Ajouter une nouvelle recommandation
                produit = get_object_or_404(Produit, id_produit=product_id)
                utilisateur = get_object_or_404(Utilisateur, id_utilisateur=user_id)

                Recommandation.objects.create(
                    id_produit=produit,
                    id_utilisateur=utilisateur
                )

                return JsonResponse({'status': 'success', 'message': 'Produit recommandé avec succès !'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Produit deja recommande !'})
        else:
            return JsonResponse({'status': 'error', 'message': 'ID de produit invalide.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'}, status=405)
    




def ajouter_avis_service(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire via request.POST
        id_utilisateur = request.POST.get('id_utilisateur')
        avis = request.POST.get('avis')

        if not id_utilisateur:
            # Si l'utilisateur n'est pas connecté, retourner une erreur
            return JsonResponse({'status': 'error', 'message': 'Utilisateur non connecté.'})

        if not avis:
            # Si l'avis est vide, retourner une erreur
            return JsonResponse({'status': 'error', 'message': 'Veuillez remplir le champ avis.'})

        # Vérifier que l'utilisateur existe
        utilisateur = get_object_or_404(Utilisateur, id_utilisateur=id_utilisateur)

        # Enregistrer l'avis dans la base de données
        AvisService.objects.create(
            id_utilisateur=utilisateur,
            avis_service=avis
        )

        return JsonResponse({'status': 'success', 'message': 'Avis enregistré avec succès !'})
    else:
        return render(request, 'ajoutAvisService.html')
    



def categorie(request, id_categorie):
    # Récupérer la catégorie sélectionnée
    categorie = get_object_or_404(Categorie, id_categorie=id_categorie)
    
    # Récupérer tous les produits de cette catégorie
    produits = Produit.objects.filter(id_categorie=id_categorie)

    # Annoter les produits avec la note moyenne et le nombre d'utilisateurs
    produits = produits.annotate(
        totalNote=Avg('note__note'),
        totalU=Count('note__id_utilisateur')
    )
    
    # Récupérer toutes les catégories pour le menu
    categories = Categorie.objects.all()
    
    # Récupérer les derniers produits ajoutés
    derniers_produits = Produit.objects.order_by('-date_ajout')[:5]  # Limite à 5 produits

    # Annoter les produits avec la note moyenne et le nombre d'utilisateurs
    derniers_produits = derniers_produits.annotate(
        totalNote=Avg('note__note'),
        totalU=Count('note__id_utilisateur')
    )
    
    context = {
        'categorie': categorie,
        'produits': produits,
        'categories': categories,
        'derniers_produits': derniers_produits,
        'id_ca': id_categorie,  # Passer l'ID de la catégorie sélectionnée
    }
    
    return render(request, 'categorie.html', context)



def editer_profil(request):
    if request.method == 'POST':
        # Récupérer l'utilisateur connecté
        utilisateur = Utilisateur.objects.get(id_utilisateur=request.session.get('id_utilisateur'))

        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        pseudo = request.POST.get('pseudo')
        mot_de_passe = request.POST.get('mot_de_passe')
        photo = request.FILES.get('photo')

        # Mettre à jour les informations de base
        utilisateur.nom = nom.upper() if nom else utilisateur.nom
        utilisateur.prenom = prenom.upper() if prenom else utilisateur.prenom
        utilisateur.telephone = telephone if telephone else utilisateur.telephone
        utilisateur.email = email if email else utilisateur.email
        utilisateur.pseudo = pseudo if pseudo else utilisateur.pseudo

        # Mettre à jour le mot de passe si fourni
        if mot_de_passe:
            utilisateur.mot_de_passe = make_password(mot_de_passe)

        # Mettre à jour la photo de profil si fournie
        if photo:
            # Vérifier l'extension du fichier
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
            file_extension = os.path.splitext(photo.name)[1]
            if file_extension not in allowed_extensions:
                return JsonResponse({'status': 'error', 'message': 'Extension de fichier non autorisée.'})

            # Supprimer l'ancienne photo si elle existe
            if utilisateur.photo:
                default_storage.delete(utilisateur.photo.path)

            # Enregistrer la nouvelle photo
            photo_path = default_storage.save(f'users_epicerie/static/image/photos_utilisateurs/{pseudo}_{photo.name}', ContentFile(photo.read()))
            utilisateur.photo = photo_path

        # Sauvegarder les modifications
        utilisateur.save()

        # Mettre à jour les données de session
        request.session['nom'] = utilisateur.nom
        request.session['prenom'] = utilisateur.prenom
        request.session['telephone'] = utilisateur.telephone
        request.session['email'] = utilisateur.email
        request.session['pseudo'] = utilisateur.pseudo
        if photo:
            request.session['photo'] = utilisateur.photo.url

        # Retourner une réponse JSON
        return JsonResponse({'status': 'success', 'message': 'Profil mis à jour avec succès !'})
    else:
        return render(request, 'editerProfil.html')
    


def deconnexion(request):
    # Vérifier si l'utilisateur est connecté
    if 'id_utilisateur' in request.session:
        # Récupérer l'utilisateur connecté
        utilisateur = Utilisateur.objects.get(id_utilisateur=request.session.get('id_utilisateur'))

        # Mettre à jour la date de dernière connexion et le statut
        utilisateur.derniere_connexion = timezone.now()
        utilisateur.status = 'DECONNECTE'
        utilisateur.save()

        # Supprimer toutes les données de la session
        request.session.flush()

    # Rediriger vers la page d'accueil
    return redirect('index')
