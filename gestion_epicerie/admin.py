from django.contrib import admin
from .models import Admin, AvisService, Utilisateur, Categorie, Produit, Note, AvisProduit, Commande, LigneCommande, Facture, Community, Messages, Recommandation

# Admin configuration for Admin model
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id_admin', 'nom_admin', 'prenom_admin', 'pseudo_admin', 'mot_de_passe', 'photo', 'status', 'derniere_date_connexion')  
    search_fields = ['nom_admin', 'prenom_admin', 'pseudo_admin']  

# Admin configuration for AvisService model
class AvisServiceAdmin(admin.ModelAdmin):
    list_display = ('id_avis_service', 'id_utilisateur', 'avis_service')  
    search_fields = ['id_utilisateur__nom', 'id_utilisateur__prenom']  

# Admin configuration for Utilisateur model
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'nom', 'prenom', 'telephone', 'email', 'pseudo', 'mot_de_passe', 'photo', 'status', 'derniere_connexion', 'solde', 'date_inscription')  
    search_fields = ['nom', 'prenom', 'telephone', 'email', 'pseudo']  

# Admin configuration for Produit model
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id_produit', 'id_categorie', 'nom_produit', 'qte_en_stock', 'seuil_min', 'prix', 'prix_promotion', 'image_produit', 'description', 'date_ajout', 'admin', 'auteur')  
    search_fields = ['nom_produit', 'prix', 'auteur']  

# Admin configuration for Note model
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id_note', 'id_produit', 'id_utilisateur', 'note')  
    search_fields = ['id_produit__nom_produit', 'id_utilisateur__nom']  

# Admin configuration for AvisProduit model
class AvisProduitAdmin(admin.ModelAdmin):
    list_display = ('id_avis_produit', 'id_utilisateur', 'id_produit', 'id_note', 'avis_produit', 'date_ajout')  
    search_fields = ['id_utilisateur__nom', 'id_produit__nom_produit']  

# Admin configuration for Commande model
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id_commande', 'date_commande', 'montant_commande', 'commande_pret', 'paye', 'id_utilisateur')  
    search_fields = ['id_utilisateur__nom', 'date_commande']  

# Admin configuration for Facture model
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_commande', 'id_produit', 'qte', 'prix_produit', 'num_facture')  
    search_fields = ['num_facture', 'id_utilisateur__nom']  

# Admin configuration for Community model
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id_message', 'id_utilisateur', 'message', 'date_envoi')  
    search_fields = ['id_utilisateur__nom', 'message']  

# Admin configuration for Messages model
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id_message', 'id_envoyeur', 'id_recepteur', 'message', 'date_envoi')  
    search_fields = ['id_envoyeur__nom', 'id_recepteur__nom', 'message']  

# Admin configuration for Recommandation model
class RecommandationAdmin(admin.ModelAdmin):
    list_display = ('id_produit', 'id_utilisateur')  
    search_fields = ['id_utilisateur__nom', 'id_produit__nom_produit']  

# Register models in Django admin
admin.site.register(Admin, AdminAdmin)
admin.site.register(AvisService, AvisServiceAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Categorie)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(AvisProduit, AvisProduitAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(LigneCommande)
admin.site.register(Facture, FactureAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Recommandation, RecommandationAdmin)
