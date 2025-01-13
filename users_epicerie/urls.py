from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quickview/<int:id_produit>', views.quickview, name='quickview'),
    path('recherche/', views.recherche, name='recherche'),
    path('product/<int:id_produit>/', views.product_detail, name='product'),
    path('ajouter_avis_produit/', views.ajouter_avis_produit, name='ajouter_avis_produit'),
    path('recommander_produit/', views.recommander_produit, name='recommander_produit'),
    path('ajouter_avis_service/', views.ajouter_avis_service, name='ajouter_avis_service'),
    path('categorie/<int:id_categorie>/', views.categorie, name='categorie'),
    path('editer_profil/', views.editer_profil, name='editer_profil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('panier/', views.panier, name='panier'),
    path('gestion_panier/', views.gestion_panier, name='gestion_panier'),
    path('fetch_cart/', views.fetch_cart, name='fetch_cart'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
    path('commander/', views.commander, name='commander'),
    path('mesCommandes/', views.mesCommandes, name='mesCommandes'),
    path('facture/<int:id_commande>/', views.facture, name='facture'),
    path('chat/', views.chat, name='chat'),
    path('affiche_conversation_action/', views.affiche_conversation_action, name='affiche_conversation_action'),
    path('enregistrer_message/', views.enregistrer_message, name='enregistrer_message'),
    path('utilisateurs_en_ligne/', views.utilisateurs_en_ligne, name='utilisateurs_en_ligne'),
    path('recherche_utilisateurs/', views.recherche_utilisateurs, name='recherche_utilisateurs'),
    path('chat_admin/', views.chat_admin, name='chat_admin'),

]
