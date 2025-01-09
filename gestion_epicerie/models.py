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
        db_table = 'admin'


class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pseudo = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos_utilisateurs/')
    status = models.CharField(max_length=255, default='DECONNECTE')
    derniere_connexion = models.DateTimeField(auto_now_add=True)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'utilisateurs'


class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=255)

    class Meta:
        db_table = 'categorie'


class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=255)
    qte_en_stock = models.IntegerField()
    seuil_min = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    prix_promotion = models.DecimalField(max_digits=10, decimal_places=2)
    image_produit = models.ImageField(upload_to='images_produits/')
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    admin = models.CharField(max_length=5, default='OUI')
    auteur = models.CharField(max_length=255)

    class Meta:
        db_table = 'produit'


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
