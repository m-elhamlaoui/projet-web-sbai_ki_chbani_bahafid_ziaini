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
from django.db.models import Q
from django.utils.translation import get_language, activate





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

    user_language = request.GET.get('lang', 'fr')  # Default to French
    activate(user_language)  # Force language activation
    request.session['django_language'] = user_language  # Save to session
    print(f"Current language: {get_language()}")  # Debug output

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

@csrf_exempt
def panier(request):
    return render(request, 'panier.html')




@csrf_exempt
@transaction.atomic
def commander(request):
    if request.method == 'POST':
        response = ""
        verification = True
        num_facture = "FAC"

        # Vérifier que l'utilisateur est connecté
        if 'id_utilisateur' not in request.session:
            response = "-1"
            return JsonResponse(response, safe=False)

        if response != "-1":
            if 'shopping_cart' in request.session:
                montant_total = Decimal('0.00')  # Utiliser Decimal pour éviter les erreurs d'arrondi
                shopping_cart = request.session['shopping_cart']

                # Vérifier la disponibilité des produits et calculer le montant total
                for item in shopping_cart:
                    product_id = item['product_id']
                    product_quantity = int(item['product_quantity'])  # Convertir en entier
                    product_price = Decimal(str(item['product_price']))  # Convertir en Decimal

                    produit = get_object_or_404(Produit, id_produit=product_id)
                    if produit.qte_en_stock < product_quantity:
                        verification = False
                        response += f" La quantité disponible du produit {item['product_name']} est insuffisante."

                    montant_total += product_quantity * product_price  # Calculer le montant total
                    num_facture += str(product_id)

                if verification:
                    # Enregistrer la commande
                    last_commande = Commande.objects.all().order_by('-id_commande').first()
                    id_com = last_commande.id_commande + 1 if last_commande else 1

                    num_facture += str(id_com)

                    commande = Commande.objects.create(
                        id_commande=id_com,
                        montant_commande=montant_total,
                        id_utilisateur_id=request.session['id_utilisateur'],
                        paye='NON'
                    )

                    # Enregistrer chaque produit dans la commande
                    for item in shopping_cart:
                        product_id = item['product_id']
                        product_quantity = int(item['product_quantity'])  # Convertir en entier

                        LigneCommande.objects.create(
                            id_commande=commande,
                            id_produit_id=product_id,
                            qte=product_quantity
                        )

                        # Mettre à jour la quantité en stock
                        produit = Produit.objects.get(id_produit=product_id)
                        produit.qte_en_stock -= product_quantity
                        produit.save()

                        # Enregistrer le produit dans la facture
                        Facture.objects.create(
                            id_utilisateur_id=request.session['id_utilisateur'],
                            id_commande=commande,
                            id_produit_id=product_id,
                            qte=product_quantity,
                            prix_produit=product_quantity * Decimal(str(item['product_price'])),  # Convertir en Decimal
                            num_facture=num_facture
                        )

                    # Vider le panier
                    del request.session['shopping_cart']
                    response = "0"

        return JsonResponse(response, safe=False)
    



@csrf_exempt
def gestion_panier(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        # Initialiser le panier dans la session s'il n'existe pas
        if 'shopping_cart' not in request.session:
            request.session['shopping_cart'] = []

        shopping_cart = request.session['shopping_cart']

        if action == 'add':
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_price = request.POST.get('product_price')
            product_quantity = int(request.POST.get('product_quantity', 1))  # Par défaut, quantité = 1
            product_photo = request.POST.get('product_photo')

            # Vérifier si le produit est déjà dans le panier
            product_exists = False
            for item in shopping_cart:
                if item['product_id'] == product_id:
                    item['product_quantity'] += product_quantity
                    product_exists = True
                    break

            # Si le produit n'est pas déjà dans le panier, l'ajouter
            if not product_exists:
                item = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_price': product_price,
                    'product_quantity': product_quantity,
                    'product_photo': product_photo
                }
                shopping_cart.append(item)

        elif action == 'remove':
            product_id = request.POST.get('product_id')
            # Supprimer le produit du panier
            shopping_cart = [item for item in shopping_cart if item['product_id'] != product_id]

        elif action == 'ajouter':
            product_id = request.POST.get('product_id')
            # Augmenter la quantité du produit de 1
            for item in shopping_cart:
                if item['product_id'] == product_id:
                    item['product_quantity'] += 1
                    break

        elif action == 'moins':
            product_id = request.POST.get('product_id')
            # Diminuer la quantité du produit de 1 (si la quantité est supérieure à 1)
            for item in shopping_cart:
                if item['product_id'] == product_id:
                    if item['product_quantity'] > 1:
                        item['product_quantity'] -= 1
                    break

        elif action == 'empty':
            # Vider le panier
            shopping_cart.clear()

        # Mettre à jour la session avec le panier modifié
        request.session['shopping_cart'] = shopping_cart
        request.session.modified = True

        # Retourner une réponse JSON
        return JsonResponse({'status': 'success', 'shopping_cart': shopping_cart})
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'}, status=405)
    

@csrf_exempt
def fetch_cart(request):
    # Initialiser les variables
    total_price = 0
    total_item = 0
    output = '''
    <div class="table-responsive" id="order_table">
        <table class="table table-bordered table-striped">
            <tr>  
                <th width="15%">Image Produit</th>  
                <th width="15%">NOM</th>  
                <th width="15%">PRIX</th>  
                <th width="15%">QUANTITE</th> 
                <th width="15%">TOTAL</th> 
                <th width="25%">Action</th>  
            </tr>
    '''

    # Vérifier si le panier existe dans la session
    if 'shopping_cart' in request.session and request.session['shopping_cart']:
        shopping_cart = request.session['shopping_cart']

        # Parcourir les articles du panier
        for item in shopping_cart:
            product_photo = item.get('product_photo', '')
            product_name = item.get('product_name', '')
            product_price = float(item.get('product_price', 0))
            product_quantity = int(item.get('product_quantity', 0))
            total_item_price = product_quantity * product_price

            # Ajouter une ligne au tableau pour chaque produit
            output += f'''
            <tr>
                <td><img src="{product_photo}" style="height:50px;"/></td>
                <td align="center">{product_name}</td>
                <td align="center">{product_price:.2f} DH</td>
                <td align="center">{product_quantity}</td>
                <td align="right">{total_item_price:.2f} DH</td>
                <td align="center">
                    <button name="delete" class="btn btn-danger btn-xs delete" id="{item['product_id']}">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                    <button name="delete" class="btn btn-primary btn-xs moins" id="{item['product_id']}">
                        <i class="fa-solid fa-minus"></i>
                    </button>
                    <button name="delete" class="btn btn-success btn-xs ajouter" id="{item['product_id']}">
                        <i class="fa-solid fa-plus"></i>
                    </button>
                </td>
            </tr>
            '''

            # Calculer le prix total et le nombre total d'articles
            total_price += total_item_price
            total_item += 1

        # Ajouter la ligne du total
        output += f'''
        <tr>  
            <td colspan="4" align="right">Total</td>  
            <td align="right">{total_price:.2f} DH</td>  
            <td></td>  
        </tr>
        '''
    else:
        # Si le panier est vide
        output += '''
        <tr>
            <td colspan="6" align="center">
                Votre Panier est vide!
            </td>
        </tr>
        '''

    # Fermer le tableau
    output += '</table></div>'

    # Préparer les données à retourner
    data = {
        'cart_details': output,
        'total_price': f'{total_price:.2f} DH',
        'total_item': total_item
    }

    # Retourner les données au format JSON
    return JsonResponse(data)



@transaction.atomic  # Assure que toutes les opérations sont exécutées dans une transaction
@csrf_exempt
def passer_commande(request):
    if request.method == 'POST':
        # Vérifier si l'utilisateur est connecté
        if 'id_utilisateur' not in request.session:
            return JsonResponse({'status': '-1', 'message': 'Utilisateur non connecté.'})

        user_id = request.session['id_utilisateur']
        utilisateur = Utilisateur.objects.get(id_utilisateur=user_id)

        # Vérifier si le panier existe dans la session
        if 'shopping_cart' not in request.session or not request.session['shopping_cart']:
            return JsonResponse({'status': 'error', 'message': 'Le panier est vide.'}, status=400)

        shopping_cart = request.session['shopping_cart']
        montant_total = Decimal('0.00')
        verification = True
        reponse = ""
        num_facture = "FAC"

        # Vérifier la disponibilité des produits et calculer le montant total
        for item in shopping_cart:
            produit = Produit.objects.get(id_produit=item['product_id'])
            quantite_demandee = item['product_quantity']
            prix_produit = Decimal(str(item['product_price']))

            if produit.qte_en_stock < quantite_demandee:
                verification = False
                reponse += f" La quantité disponible du produit {item['product_name']} est insuffisante."
                break

            montant_total += quantite_demandee * prix_produit
            num_facture += str(item['product_id'])

        if not verification:
            return JsonResponse({'status': 'error', 'message': reponse})

        # Vérifier le solde de l'utilisateur
        if utilisateur.solde < montant_total:
            return JsonResponse({'status': 'error', 'message': 'Votre solde est insuffisant. Veuillez le recharger !'})

        # Enregistrer la commande
        try:
            # Générer un nouvel ID de commande
            derniere_commande = Commande.objects.last()
            id_commande = (derniere_commande.id_commande + 1) if derniere_commande else 1

            # Créer la commande
            commande = Commande.objects.create(
                id_commande=id_commande,
                montant_commande=montant_total,
                id_utilisateur=utilisateur
            )

            # Enregistrer chaque produit dans la commande
            for item in shopping_cart:
                produit = Produit.objects.get(id_produit=item['product_id'])
                quantite_demandee = item['product_quantity']
                prix_produit = Decimal(str(item['product_price']))

                # Créer une ligne de commande
                LigneCommande.objects.create(
                    id_commande=commande,
                    id_produit=produit,
                    qte=quantite_demandee
                )

                # Mettre à jour la quantité en stock du produit
                produit.qte_en_stock -= quantite_demandee
                produit.save()

                # Créer une facture pour chaque produit
                Facture.objects.create(
                    id_utilisateur=utilisateur,
                    id_commande=commande,
                    id_produit=produit,
                    qte=quantite_demandee,
                    prix_produit=prix_produit,
                    num_facture=num_facture + str(id_commande)
                )

            # Mettre à jour le solde de l'utilisateur
            utilisateur.solde -= montant_total
            utilisateur.save()

            # Vider le panier
            del request.session['shopping_cart']
            request.session.modified = True

            return JsonResponse({'status': '0', 'message': 'Commande passée avec succès !'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Erreur lors de la commande : {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'}, status=405)
    



def mesCommandes(request):
    # Vérifier si l'utilisateur est connecté
    if 'id_utilisateur' not in request.session:
        return redirect('index')

    # Récupérer l'ID de l'utilisateur depuis la session
    user_id = request.session.get('id_utilisateur')

    # Récupérer l'utilisateur
    utilisateur = get_object_or_404(Utilisateur, id_utilisateur=user_id)

    # Récupérer les commandes de l'utilisateur
    commandes = Commande.objects.filter(id_utilisateur=utilisateur).select_related('id_utilisateur')

    # Préparer les données à passer au template
    commandes_data = []
    for commande in commandes:
        # Compter le nombre de produits associés à la commande
        nombre_produits = LigneCommande.objects.filter(id_commande=commande).count()

        commandes_data.append({
            'id_commande': commande.id_commande,
            'date_commande': commande.date_commande.strftime('%Y-%m-%d %H:%M:%S'),
            'montant_commande': float(commande.montant_commande),
            'commande_pret': commande.commande_pret,
            'paye': commande.paye,
            'id_utilisateur': commande.id_utilisateur.id_utilisateur,
            'nom_utilisateur': commande.id_utilisateur.nom,
            'prenom_utilisateur': commande.id_utilisateur.prenom,
            'nombre_produits': nombre_produits,  # Ajouter le nombre de produits
        })

    # Passer les données au template
    return render(request, 'mesCommandes.html', {'commandes': commandes_data})




def facture(request, id_commande):
    # Vérifier si l'utilisateur est connecté
    if 'id_utilisateur' not in request.session:
        return redirect('index')  # Rediriger vers la page d'accueil si l'utilisateur n'est pas connecté

    # Récupérer les produits associés à la commande
    produits = Facture.objects.filter(id_commande=id_commande).select_related('id_produit')

    # Calculer le montant total de la facture
    total = Facture.objects.filter(id_commande=id_commande).aggregate(total=Sum('prix_produit'))['total']

    # Récupérer le numéro de facture (on prend le premier enregistrement)
    num_facture = Facture.objects.filter(id_commande=id_commande).first().num_facture

    # Récupérer le statut de la commande
    commande = get_object_or_404(Commande, id_commande=id_commande)
    status = commande.commande_pret

    # Récupérer la date et l'heure actuelles
    date_facture = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    # Préparer les données à passer au template
    context = {
        'produits': produits,
        'total': total,
        'num_facture': num_facture,
        'status': status,
        'date_facture': date_facture,  # Ajout de la date de la facture
    }

    # Passer les données au template
    return render(request, 'facture.html', context)


@csrf_exempt
def chat(request):
    # Récupérer l'administrateur (récepteur)
    try:
        admin = Admin.objects.first()  # Récupérer le premier administrateur
    except Admin.DoesNotExist:
        return redirect('index')  # Rediriger si aucun administrateur n'existe

    # Mettre les informations dans des variables
    status = admin.status
    id_recepteur = admin.id_admin
    photo_recepteur = admin.photo
    nom_recepteur = admin.nom_admin
    prenom_recepteur = admin.prenom_admin
    derniere_connexion_recepteur = admin.derniere_date_connexion

    # Préparer les données à passer au template
    context = {
        'status': status,
        'id_recepteur': id_recepteur,
        'photo_recepteur': photo_recepteur,
        'nom_recepteur': nom_recepteur,
        'prenom_recepteur': prenom_recepteur,
        'derniere_connexion_recepteur': derniere_connexion_recepteur,
    }

    # Passer les données au template
    return render(request, 'chat.html', context)



@csrf_exempt
def affiche_conversation_action(request):
    # Récupérer l'utilisateur connecté
    id_envoyeur = request.session.get('id_utilisateur')
    id_recepteur = request.POST.get('id_recepteur', 0)  # Récupérer l'ID du récepteur depuis la requête AJAX

    # Récupérer les messages entre l'utilisateur et le récepteur
    messages = Messages.objects.filter(
        (Q(id_envoyeur=id_envoyeur) & Q(id_recepteur=id_recepteur)) |
        (Q(id_envoyeur=id_recepteur) & Q(id_recepteur=id_envoyeur))
    ).order_by('date_envoi')

    # Récupérer la photo du récepteur (admin)
    try:
        admin = Admin.objects.first()  # Récupérer le premier administrateur
        photo_recepteur = admin.photo
    except Admin.DoesNotExist:
        photo_recepteur = None

    # Récupérer la photo de l'utilisateur connecté
    user_photo = request.session.get('photo')

    # Générer le HTML des messages
    html_response = ""
    if messages.exists():
        for message in messages:
            if message.id_envoyeur == id_envoyeur:
                # Message envoyé par l'utilisateur
                html_response += f'''
                <div class="d-flex justify-content-end mb-4">
                    <div class="msg_cotainer_send" style="font-size:1.3rem;">
                        {message.message}
                        <span class="msg_time_send">{message.date_envoi.strftime('%Y-%m-%d %H:%M:%S')}</span>
                    </div>
                    <div class="img_cont_msg">
                        <img src="{user_photo}" class="rounded-circle user_img_msg">
                    </div>
                </div>
                '''
            else:
                # Message reçu de l'administrateur
                html_response += f'''
                <div class="d-flex justify-content-start mb-4">
                    <div class="img_cont_msg">
                        <img src="admins_epicerie/static/image/{photo_recepteur}" class="rounded-circle user_img_msg">
                    </div>
                    <div class="msg_cotainer" style="font-size:1.3rem;">
                        {message.message}
                        <span class="msg_time">{message.date_envoi.strftime('%Y-%m-%d %H:%M:%S')}</span>
                    </div>
                </div>
                '''
    else:
        # Aucun message
        html_response = '<p style="color:white;font-size:1.6rem">Aucun message envoyé</p>'

    return HttpResponse(html_response)



@csrf_exempt
def enregistrer_message(request):
    # Récupérer les données de la requête POST
    id_recepteur = request.POST.get('id_recepteur')
    id_envoyeur = request.POST.get('id_envoyeur')
    message = request.POST.get('message')

    # Vérifier que les données ne sont pas vides
    if not id_recepteur or not id_envoyeur or not message:
        return JsonResponse({'status': 'error', 'message': 'Tous les champs sont obligatoires'}, status=400)

    try:
        # Enregistrer le message dans la base de données
        nouveau_message = Messages.objects.create(
            id_envoyeur=id_envoyeur,
            id_recepteur=id_recepteur,
            message=message
        )

        # Retourner une réponse JSON en cas de succès
        return JsonResponse({'status': 'success', 'message': 'Message enregistré avec succès'})

    except Exception as e:
        # Retourner une réponse JSON en cas d'erreur
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    



@csrf_exempt
def utilisateurs_en_ligne(request):
    if request.method == 'POST':
        # Récupérer les utilisateurs et leurs messages
        utilisateurs_avec_messages = Utilisateur.objects.raw('''
            SELECT * FROM utilisateurs AS u
            INNER JOIN messages AS m
            ON u.id_utilisateur = m.id_envoyeur
        ''')

        if utilisateurs_avec_messages:
            # Si des utilisateurs avec des messages sont trouvés
            data = []
            for utilisateur in utilisateurs_avec_messages:
                # Récupérer le dernier message
                dernier_message = Messages.objects.filter(
                    id_envoyeur=utilisateur.id_utilisateur,
                    id_recepteur=0
                ).order_by('-date_envoi').first()

                if dernier_message:
                    dernier_message_texte = dernier_message.message
                else:
                    dernier_message_texte = 'Aucun message ....'

                # Déterminer le statut de l'utilisateur
                status = 'offline' if utilisateur.status == 'DECONNECTE' else ''

                # Construire le HTML pour l'utilisateur
                utilisateur_html = f'''
                    <li>
                        <a href="./../message/{utilisateur.id_utilisateur}/">
                            <div class="d-flex bd-highlight">
                                <div class="img_cont">
                                    <img src="./../../{utilisateur.photo}" class="rounded-circle user_img">
                                    <span class="online_icon {status}"></span>
                                </div>
                                <div class="user_info">
                                    <span>{utilisateur.nom} {utilisateur.prenom}</span>
                                    <p>{dernier_message_texte}</p>
                                </div>
                            </div>
                        </a>
                    </li>
                '''
                data.append(utilisateur_html)

            return JsonResponse(data, safe=False)
        else:
            # Si aucun utilisateur avec des messages n'est trouvé
            return JsonResponse('<div class="alert danger-alert" style="color:white;font-size:1.5rem;"> Aucun Message <div>', safe=False)





@csrf_exempt
def recherche_utilisateurs(request):
    if request.method == 'POST':
        valeur_recherche = request.POST.get('recherche', '').strip()

        if valeur_recherche:
            # Rechercher des utilisateurs en fonction de la valeur de recherche
            utilisateurs = Utilisateur.objects.raw('''
                SELECT * FROM utilisateurs
                WHERE id_utilisateur != 0 AND
                (nom LIKE %s OR
                prenom LIKE %s OR
                pseudo LIKE %s)
            ''', [f'%{valeur_recherche}%', f'%{valeur_recherche}%', f'%{valeur_recherche}%'])

            if utilisateurs:
                # Si des utilisateurs sont trouvés
                data = []
                for utilisateur in utilisateurs:
                    # Récupérer le dernier message
                    dernier_message = Messages.objects.filter(
                        id_envoyeur=utilisateur.id_utilisateur,
                        id_recepteur=0
                    ).order_by('-date_envoi').first()

                    if dernier_message:
                        dernier_message_texte = dernier_message.message
                    else:
                        dernier_message_texte = 'Aucun message ....'

                    # Déterminer le statut de l'utilisateur
                    status = 'offline' if utilisateur.status == 'DECONNECTE' else ''

                    # Construire le HTML pour l'utilisateur
                    utilisateur_html = f'''
                        <li>
                            <a href="./../message/{utilisateur.id_utilisateur}/">
                                <div class="d-flex bd-highlight">
                                    <div class="img_cont">
                                        <img src="./../../{utilisateur.photo}" class="rounded-circle user_img">
                                        <span class="online_icon {status}"></span>
                                    </div>
                                    <div class="user_info">
                                        <span>{utilisateur.nom} {utilisateur.prenom}</span>
                                        <p>{dernier_message_texte}</p>
                                    </div>
                                </div>
                            </a>
                        </li>
                    '''
                    data.append(utilisateur_html)

                return JsonResponse(data, safe=False)
            else:
                # Si aucun utilisateur n'est trouvé
                return JsonResponse('<div class="alert danger-alert"> Aucun utilisateur trouvé <div>', safe=False)
        else:
            return JsonResponse("Veuillez entrer une valeur de recherche.", safe=False)
        


def chat_admin(request):
    return render(request,'chatAdmin.html')





def message(request, user_id):
    # Récupérer l'utilisateur (récepteur) en fonction de l'ID
    utilisateur = get_object_or_404(Utilisateur, id_utilisateur=user_id)

    # Préparer les données à passer au template
    context = {
        'status': utilisateur.status,
        'photoRecepteur': utilisateur.photo.url,  
        'nomRecepteur': utilisateur.nom,
        'prenomRecepteur': utilisateur.prenom,
        'derniereConnexionRecepteur': utilisateur.derniere_connexion,
        'user_id': user_id,
    }

    # Rendre le template avec les données
    return render(request, 'message.html', context)



@csrf_exempt
def affiche_conversation_admin(request):
    if request.method == 'POST':
        # Récupérer l'ID du récepteur depuis la requête AJAX
        id_recepteur = request.POST.get('id_recepteur')
        id_envoyeur = 0  

        # Récupérer les messages entre l'envoyeur et le récepteur
        messages = Messages.objects.filter(
            (models.Q(id_envoyeur=id_envoyeur) & models.Q(id_recepteur=id_recepteur)) |
            (models.Q(id_envoyeur=id_recepteur) & models.Q(id_recepteur=id_envoyeur))
        ).order_by('date_envoi')

        # Récupérer la photo du récepteur
        recepteur = get_object_or_404(Utilisateur, id_utilisateur=id_recepteur)
        photo_recepteur = recepteur.photo.url

        # Construire le HTML des messages
        html_messages = ""
        if messages.exists():
            for message in messages:
                if message.id_envoyeur == id_envoyeur:
                    # Message envoyé par l'utilisateur connecté
                    html_messages += f'''
                    <div class="d-flex justify-content-end mb-4">
                        <div class="msg_cotainer_send" style="font-size:1.3rem;">
                            {message.message}
                            <span class="msg_time_send">{message.date_envoi.strftime("%d/%m/%Y %H:%M")}</span>
                        </div>
                        <div class="img_cont_msg">
                            <img src="./../../../static/image/{request.session.get('photo')}" class="rounded-circle user_img_msg">
                        </div>
                    </div>
                    '''
                else:
                    # Message reçu de l'autre utilisateur
                    html_messages += f'''
                    <div class="d-flex justify-content-start mb-4">
                        <div class="img_cont_msg">
                            <img src="{photo_recepteur}" class="rounded-circle user_img_msg">
                        </div>
                        <div class="msg_cotainer" style="font-size:1.3rem;">
                            {message.message}
                            <span class="msg_time">{message.date_envoi.strftime("%d/%m/%Y %H:%M")}</span>
                        </div>
                    </div>
                    '''
        else:
            # Aucun message trouvé
            html_messages = '<p style="color:white;font-size:1.6rem">Aucun message envoyé</p>'

        # Renvoyer le HTML des messages
        return JsonResponse(html_messages, safe=False)
    




@csrf_exempt
def message_action_admin(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        id_recepteur = request.POST.get('id_recepteur')
        id_envoyeur = request.POST.get('id_envoyeur')
        message = request.POST.get('message')

        # Valider que les champs ne sont pas vides
        if not id_recepteur or not id_envoyeur or not message:
            return JsonResponse({'error': 'Tous les champs sont obligatoires.'}, status=400)

        # Convertir les ID en entiers
        try:
            id_recepteur = int(id_recepteur)
            id_envoyeur = int(id_envoyeur)
        except ValueError:
            return JsonResponse({'error': 'Les ID doivent être des nombres valides.'}, status=400)

        # Enregistrer le message dans la base de données
        nouveau_message = Messages.objects.create(
            id_envoyeur=id_envoyeur,
            id_recepteur=id_recepteur,
            message=message
        )

        # Renvoyer une réponse JSON
        return JsonResponse({'success': 'Message envoyé avec succès.', 'message_id': nouveau_message.id_message})
    else:
        return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)