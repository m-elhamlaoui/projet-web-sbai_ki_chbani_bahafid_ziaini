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