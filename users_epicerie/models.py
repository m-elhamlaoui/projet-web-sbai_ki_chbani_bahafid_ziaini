from django.db import models
from gestion_epicerie.models import Utilisateur
from admins_epicerie.models import Produit

# Create your models here.
class Note(models.Model):
    id_note = models.AutoField(primary_key=True)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'note'


class AvisService(models.Model):
    id_avis_service = models.AutoField(primary_key=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    avis_service = models.TextField()

    class Meta:
        db_table = 'avisservice'


class AvisProduit(models.Model):
    id_avis_produit = models.AutoField(primary_key=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    id_note = models.ForeignKey(Note, on_delete=models.CASCADE)
    avis_produit = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'avis_produit'


class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    montant_commande = models.DecimalField(max_digits=10, decimal_places=2)
    commande_pret = models.CharField(max_length=10, default='NON')
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    paye = models.CharField(max_length=5, default='OUI')

    class Meta:
        db_table = 'commande'


class LigneCommande(models.Model):
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField()

    class Meta:
        db_table = 'ligne_commande'
        unique_together = ('id_commande', 'id_produit')


class Facture(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField()
    prix_produit = models.DecimalField(max_digits=10, decimal_places=0)
    num_facture = models.CharField(max_length=255)

    class Meta:
        db_table = 'facture'


class Community(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'community'


class Messages(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_envoyeur = models.IntegerField()  
    id_recepteur = models.IntegerField() 
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'



class Recommandation(models.Model):
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recommandation'
        unique_together = ('id_produit', 'id_utilisateur')
