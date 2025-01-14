from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Avg, Count, Sum
from django.http import JsonResponse,HttpResponse
from gestion_epicerie.models import *
from admins_epicerie.models import *
from users_epicerie.models import *
from .models import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password
import os
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.db import transaction
from django.db.models import F
from django.template.loader import render_to_string
from .forms import ProduitForm
from django.conf import settings





def dashboard(request):
    # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin

    # 1. Chiffre d'affaires total
    chiffre_affaires = LigneCommande.objects.annotate(
        total_line=F('qte') * F('id_produit__prix_promotion')
    ).aggregate(mtc=Sum('total_line'))['mtc'] or 0

    # 2. Produits en dessous du seuil minimal
    produits_seuil = Produit.objects.filter(
        qte_en_stock__lte=F('seuil_min'), qte_en_stock__gt=0
    )

    # 3. Profits par catégorie
    profits_categorie = Commande.objects.annotate(
        montant=F('montant_commande')
    ).values('lignecommande__id_produit__id_categorie__nom_categorie').annotate(
        montant_total=Sum('montant_commande')
    )

    # 4. Total des commandes
    total_commandes = Commande.objects.aggregate(
        totalCom=Count('id_commande')
    )['totalCom'] or 0

    # 5. Total des produits vendus
    total_produits_vendus = LigneCommande.objects.aggregate(
        vendu=Count('id_produit')
    )['vendu'] or 0

    # 6. Prix total du stock
    prix_total_stock = Produit.objects.annotate(
        total_line=F('prix_promotion') * F('qte_en_stock')
    ).aggregate(total=Sum('total_line'))['total'] or 0

    # 7. Meilleurs clients
    meilleurs_clients = Commande.objects.values(
        'id_utilisateur__photo', 'id_utilisateur__nom', 'id_utilisateur__prenom'
    ).annotate(
        montant_total=Sum('montant_commande')
    ).order_by('-montant_total')[:9]

    # 8. Rupture de stock
    rupture_stock = Produit.objects.filter(qte_en_stock=0)

    # 9. Meilleures notes
    meilleures_notes = Note.objects.values(
        'id_produit__nom_produit', 'id_produit__prix_promotion', 'id_produit__image_produit'
    ).annotate(
        noteP=Count('id_produit')
    ).order_by('-noteP')[:7]

    # 10. Produits les plus vendus
    plus_vendus = LigneCommande.objects.values(
        'id_produit__nom_produit'
    ).annotate(
        nbVendu=Count('id_produit')
    ).order_by('-nbVendu')[:5]

    # 11. Tous les produits
    produits = Produit.objects.all()

    # 12. Toutes les catégories
    categories = Categorie.objects.all()

    # 13. Produits en dessous du seuil minimal
    produit_seuil = produits_seuil

    # Ajouter l'heure actuelle au contexte
    current_time = timezone.now()

    # Contexte pour le template
    context = {
        'chiffre_affaires': chiffre_affaires,
        'produits_seuil': produits_seuil,
        'profits_categorie': profits_categorie,
        'total_commandes': total_commandes,
        'total_produits_vendus': total_produits_vendus,
        'prix_total_stock': prix_total_stock,
        'meilleurs_clients': meilleurs_clients,
        'rupture_stock': rupture_stock,
        'meilleures_notes': meilleures_notes,
        'plus_vendus': plus_vendus,
        'produits': produits,
        'categories': categories,
        'produit_seuil': produit_seuil,
        'current_time': current_time,  # Ajout de l'heure actuelle
    }

    return render(request, 'dashboard.html', context)





def utilisateurs(request):
    # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin

    # Récupérer tous les utilisateurs
    utilisateurs = Utilisateur.objects.all()

    # Récupérer les 10 derniers utilisateurs inscrits
    nouveaux_utilisateurs = Utilisateur.objects.order_by('-date_inscription')[:10]

    # Contexte pour le template
    context = {
        'utilisateurs': utilisateurs,
        'nouveaux_utilisateurs': nouveaux_utilisateurs,
    }

    # Retourner la réponse à la page utilisateurs
    return render(request, 'utilisateurs.html', context)




@csrf_exempt  
def ajout_solde_admin(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        solde = request.POST.get('solde')

        # Vérifier si les champs sont vides
        if not pseudo or not solde:
            return JsonResponse({"erreur": "Tous les champs sont obligatoires"})

        try:
            # Convertir le solde en Decimal
            solde = Decimal(solde)
        except (ValueError, TypeError):
            return JsonResponse({"erreur": "Le solde doit être un nombre valide"})

        # Rechercher l'utilisateur par pseudo
        try:
            utilisateur = Utilisateur.objects.get(pseudo=pseudo)
        except Utilisateur.DoesNotExist:
            return JsonResponse({"erreur": "Pseudo inexistant, vérifiez bien le pseudo"})

        # Mettre à jour le solde de l'utilisateur
        utilisateur.solde += solde  # Maintenant, les deux sont des Decimal
        utilisateur.save()

        # Retourner une réponse JSON indiquant le succès
        return JsonResponse({"success": True, "message": "Solde ajouté avec succès"})

    # Si la méthode n'est pas POST, retourner une erreur
    return JsonResponse({"erreur": "Méthode non autorisée"})



def produits_inpt(request):
     # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin
    
    # Récupérer les produits où admin = 'NON'
    produits = Produit.objects.filter(admin='NON')

    # Annoter chaque produit avec la quantité vendue
    produits = produits.annotate(
        qte_vendue=Sum('lignecommande__qte')
    )

    # Contexte pour le template
    context = {
        'produits': produits,
    }

    # Retourner la réponse à la page produitInpt.html
    return render(request, 'produitInpt.html', context)





def commandes(request):
     # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin
    
    # Récupérer les commandes non prêtes (commande_pret='NON')
    commandes = Commande.objects.filter(commande_pret='NON').annotate(
        heure=F('date_commande__hour'),  # Extraire l'heure de la commande
        minute=F('date_commande__minute')  # Extraire les minutes de la commande
    ).order_by('date_commande').prefetch_related(
        'lignecommande_set__id_produit'  # Précharger les produits associés
    )

    # Contexte pour le template
    context = {
        'commandes': commandes,
    }

    # Retourner la réponse à la page commande.html
    return render(request, 'commande.html', context)




def pret(request, id_commande):
     # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin
    
    # Récupérer la commande spécifique ou renvoyer une erreur 404 si elle n'existe pas
    commande = get_object_or_404(Commande, id_commande=id_commande)

    # Mettre à jour le statut de la commande à "OUI" (livrée)
    commande.commande_pret = 'OUI'
    commande.save()

    # Rediriger vers la page des commandes
    return redirect('commandes')


def produits(request):
    # Vérifier si l'utilisateur est un administrateur
    if not request.session.get('admin_connecte'):
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas un admin
    
    # Récupérer les 5 meilleurs produits (top 5 des meilleures ventes)
    meilleurs_ventes = Produit.objects.annotate(
        total_vendu=Sum('lignecommande__qte')  # Calculer la quantité totale vendue
    ).order_by('-total_vendu')[:5]  # Trier par quantité vendue (descendant) et limiter à 5

    # Récupérer toutes les catégories
    categories = Categorie.objects.all()

    # Contexte pour le template
    context = {
        'meilleurs_ventes': meilleurs_ventes,
        'categories': categories,
    }

    # Retourner la réponse à la page produit.html
    return render(request, 'produit.html', context)


@csrf_exempt
def affiche_produits_admin(request):
    if request.method == 'POST' and 'id' in request.POST:
        id_categorie = request.POST['id']
        
        # Récupérer les produits de la catégorie spécifiée
        produits = Produit.objects.filter(id_categorie=id_categorie)
        
        # Générer le HTML à renvoyer
        html = render_to_string('produit_admin_partial.html', {'produits': produits})
        
        # Renvoyer la réponse JSON avec le HTML généré
        return JsonResponse({'html': html})
    
    # Si la requête n'est pas une requête POST valide, renvoyer une erreur
    return JsonResponse({'error': 'Requête invalide'}, status=400)



def supprimer_produit(request, id_produit):
    # Récupérer le produit spécifique ou renvoyer une erreur 404 si il n'existe pas
    produit = get_object_or_404(Produit, id_produit=id_produit)
    
    # Supprimer le produit
    produit.delete()
    
    # Rediriger vers la page 
    return redirect('produits')


def modifier_produit(request, id_produit):
    # Récupérer le produit spécifique ou renvoyer une erreur 404 s'il n'existe pas
    produit = get_object_or_404(Produit, id_produit=id_produit)
    
    # Récupérer toutes les catégories pour le formulaire
    categories = Categorie.objects.all()

    if request.method == 'POST':
        # Si le formulaire est soumis, traiter les données
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produits')  # Rediriger vers la page des produits après la modification
    else:
        # Si c'est une requête GET, afficher le formulaire pré-rempli
        form = ProduitForm(instance=produit)

    # Contexte pour le template
    context = {
        'produit': produit,
        'categories': categories,
        'form': form,
    }

    # Retourner la réponse à la page modifierProduit.html
    return render(request, 'modifierProduit.html', context)


@csrf_exempt
def modifier_produit_ajax(request):
    if request.method == 'POST':
        # Initialiser la réponse
        reponse = {"status": "Echec", "message": "Une erreur est survenue."}

        # Récupérer les données du formulaire
        id_produit = request.POST.get('id')
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        prix_promotion = request.POST.get('prixPromotion', prix)  # Utiliser le prix normal si le prix promotionnel n'est pas fourni
        qte = request.POST.get('qte')
        seuil_min = request.POST.get('seuil_min')
        categorie_id = request.POST.get('categorie')
        image = request.FILES.get('image')

        # Vérifier que tous les champs obligatoires sont remplis
        if not all([id_produit, nom, description, prix, qte, seuil_min, categorie_id]):
            reponse["message"] = "Tous les champs obligatoires doivent être remplis."
            return JsonResponse(reponse)

        try:
            # Récupérer le produit à modifier
            produit = Produit.objects.get(id_produit=id_produit)
            categorie = Categorie.objects.get(id_categorie=categorie_id)

            # Mettre à jour les champs du produit
            produit.nom_produit = nom
            produit.description = description
            produit.prix = prix
            produit.prix_promotion = prix_promotion
            produit.qte_en_stock = qte
            produit.seuil_min = seuil_min
            produit.id_categorie = categorie

            # Gérer l'upload de la nouvelle image (si une image est fournie)
            if image:
                # Vérifier l'extension de l'image
                allowed_extensions = ['.jpg', '.jpeg', '.png']
                if not any(image.name.lower().endswith(ext) for ext in allowed_extensions):
                    reponse["message"] = "Veuillez choisir une image en JPG ou PNG."
                    return JsonResponse(reponse)

                # Enregistrer l'image dans le dossier approprié
                image_path = default_storage.save(f'admins_epicerie/static/image/photos_produits/{image.name}', image)
                produit.image_produit = image_path

            # Sauvegarder les modifications
            produit.save()

            # Réponse de succès
            reponse = {"status": "Succès", "message": "Modification effectuée avec succès."}
            return JsonResponse(reponse)

        except Produit.DoesNotExist:
            reponse["message"] = "Le produit spécifié n'existe pas."
            return JsonResponse(reponse)

        except Categorie.DoesNotExist:
            reponse["message"] = "La catégorie spécifiée n'existe pas."
            return JsonResponse(reponse)

        except Exception as e:
            reponse["message"] = f"Une erreur est survenue : {str(e)}"
            return JsonResponse(reponse)

    else:
        return JsonResponse({"status": "Echec", "message": "Méthode non autorisée."}, status=405)
    



@csrf_exempt
def ajout_categorie(request):
    reponse = "Erreur d'ajout"

    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()

        if nom:
            categorie = Categorie(nom_categorie=nom)
            categorie.save()
            reponse = 0

    return JsonResponse(reponse, safe=False)




@csrf_exempt
def ajout_produit(request):
    reponse = ""

    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        description = request.POST.get('description', '').strip()
        prix = request.POST.get('prix', '').strip()
        qte = request.POST.get('qte', '').strip()
        seuil_min = request.POST.get('seuil_min', '').strip()
        categorie_id = request.POST.get('categorie', '').strip()
        image = request.FILES.get('image', None)
        prix_promotion = request.POST.get('prixPromotion', prix).strip()
        proprietaire = request.POST.get('Proprietaire', '').strip()
        auteur = request.POST.get('auteur', '').strip()

        if nom and description and prix and qte and seuil_min and categorie_id and image:
            try:
                # Convertir les valeurs en nombres
                prix = Decimal(prix)
                prix_promotion = Decimal(prix_promotion)
                qte = int(qte)
                seuil_min = int(seuil_min)

                # Récupérer la catégorie
                categorie = Categorie.objects.get(id_categorie=categorie_id)
            except Categorie.DoesNotExist:
                return JsonResponse("Catégorie non trouvée", safe=False)
            except (ValueError, TypeError):
                return JsonResponse("Veuillez entrer des valeurs numériques valides pour le prix, la quantité ou le seuil minimum.", safe=False)

            # Vérifier l'extension de l'image
            allowed_extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
            file_extension = os.path.splitext(image.name)[1]

            if file_extension in allowed_extensions:
                # Enregistrer l'image dans le dossier spécifié
                image_path = os.path.join('admins_epicerie/static/image/photos_produits/', image.name)
                with open(os.path.join(settings.MEDIA_ROOT, image_path), 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

                # Enregistrer le produit dans la base de données
                produit = Produit(
                    id_categorie=categorie,
                    nom_produit=nom,
                    qte_en_stock=qte,
                    seuil_min=seuil_min,
                    prix=prix,
                    prix_promotion=prix_promotion,
                    image_produit=image_path,
                    description=description,
                    admin=proprietaire,
                    auteur=auteur
                )
                produit.save()

                reponse = 0
            else:
                reponse = "Veuillez choisir une image en jpg ou png !"
        else:
            reponse = "Tous les champs sont obligatoires !"

    return JsonResponse(reponse, safe=False)



def deconnexion_admin(request):
    # Vérifier si l'admin est connecté
    if 'admin_connecte' in request.session:
        # Récupérer l'admin connecté
        admin = Admin.objects.get(id_admin=1)

        # Mettre à jour la date de dernière connexion et le statut
        admin.derniere_date_connexion = timezone.now()
        admin.status = 'DECONNECTE'
        admin.save()

        # Supprimer toutes les données de la session
        request.session.flush()

    # Rediriger vers la page d'accueil
    return redirect('index')
