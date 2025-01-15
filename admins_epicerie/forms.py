from django import forms

from .models import Produit


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            "nom_produit",
            "description",
            "prix",
            "prix_promotion",
            "qte_en_stock",
            "seuil_min",
            "id_categorie",
            "image_produit",
        ]
