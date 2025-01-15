from django.db import models


class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=255)

    class Meta:
        db_table = "categorie"


class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=255)
    qte_en_stock = models.IntegerField()
    seuil_min = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    prix_promotion = models.DecimalField(max_digits=10, decimal_places=2)
    image_produit = models.ImageField(
        upload_to="admins_epicerie/static/image/photos_produits/"
    )
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    admin = models.CharField(max_length=5, default="OUI")
    auteur = models.CharField(max_length=255)

    class Meta:
        db_table = "produit"
