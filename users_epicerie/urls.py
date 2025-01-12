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

]
