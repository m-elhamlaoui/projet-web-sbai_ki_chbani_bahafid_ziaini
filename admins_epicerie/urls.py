from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("utilisateurs/", views.utilisateurs, name="utilisateurs"),
    path("ajout_solde_admin/", 
         views.ajout_solde_admin, 
         name="ajout_solde_admin"),
    path("produits_inpt/", views.produits_inpt, name="produits_inpt"),
    path("commandes/", views.commandes, name="commandes"),
    path("pret/<int:id_commande>/", views.pret, name="pret"),
    path("produits/", views.produits, name="produits"),
    path(
        "affiche_produits_admin/",
        views.affiche_produits_admin,
        name="affiche_produits_admin",
    ),
    path(
        "supprimer_produit/<int:id_produit>/",
        views.supprimer_produit,
        name="supprimer_produit",
    ),
    path(
        "modifier_produit/<int:id_produit>/",
        views.modifier_produit,
        name="modifier_produit",
    ),
    path(
        "modifier_produit_ajax/",
        views.modifier_produit_ajax,
        name="modifier_produit_ajax",
    ),
    path("ajout_categorie/", views.ajout_categorie, name="ajout_categorie"),
    path("ajout_produit/", views.ajout_produit, name="ajout_produit"),
    path("deconnexion_admin/", 
         views.deconnexion_admin, 
         name="deconnexion_admin"),
]
