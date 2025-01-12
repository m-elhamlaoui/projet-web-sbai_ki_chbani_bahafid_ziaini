from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('utilisateurs/', views.utilisateurs, name='utilisateurs'),
    path('ajout_solde_admin/', views.ajout_solde_admin, name='ajout_solde_admin'),
    path('produits_inpt/', views.produits_inpt, name='produits_inpt'),
]
