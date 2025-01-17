from django.db import models


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nom_admin = models.CharField(max_length=255)
    prenom_admin = models.CharField(max_length=255)
    pseudo_admin = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    photo = models.TextField()
    status = models.CharField(max_length=255)
    derniere_date_connexion = models.DateTimeField()

    class Meta:
        db_table = "admin"


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pseudo = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="users_epicerie/static/image/photos_utilisateurs/"
    )
    status = models.CharField(max_length=255, default="DECONNECTE")
    derniere_connexion = models.DateTimeField(auto_now_add=True)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "utilisateurs"
