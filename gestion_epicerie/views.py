import os

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Admin, Utilisateur


def connexion(request):
    if request.method == "POST":
        pseudo = request.POST.get("pseudo")
        mot_de_passe = request.POST.get("mot_de_passe")

        # Vérifier si c'est un admin
        if pseudo == "Admin":
            try:
                # Chercher l'admin dans la base de données
                admin = Admin.objects.get(pseudo_admin=pseudo)

                # Vérifier le mot de passe
                if admin.mot_de_passe == mot_de_passe:
                    # Créer la session pour l'admin
                    request.session["admin_connecte"] = True
                    request.session["nom"] = admin.nom_admin
                    request.session["prenom"] = admin.prenom_admin
                    request.session["pseudo"] = admin.pseudo_admin
                    request.session["photo"] = admin.photo

                    # Mettre à jour le statut de l'admin
                    admin.status = "CONNECTE"
                    admin.save()

                    return JsonResponse(
                        {"status": 0, "url": "/admins_epicerie/dashboard/"}
                    )
                else:
                    return JsonResponse(
                        {"status": "Votre mot de passe est incorrect !"}
                    )
            except Admin.DoesNotExist:
                return JsonResponse({"status": "Admin non trouvé !"})

        else:
            # Vérifier si l'utilisateur existe
            try:
                utilisateur = Utilisateur.objects.get(pseudo=pseudo)

                # Vérifier le mot de passe
                if check_password(mot_de_passe, utilisateur.mot_de_passe):
                    # Créer la session pour l'utilisateur
                    request.session["utilisateur_connecte"] = True
                    request.session["id_utilisateur"] = utilisateur.id_utilisateur
                    request.session["nom"] = utilisateur.nom
                    request.session["prenom"] = utilisateur.prenom
                    request.session["telephone"] = utilisateur.telephone
                    request.session["email"] = utilisateur.email
                    request.session["pseudo"] = utilisateur.pseudo
                    request.session["photo"] = utilisateur.photo.url
                    request.session["solde"] = float(utilisateur.solde)

                    # Mettre à jour le statut de l'utilisateur
                    utilisateur.status = "CONNECTE"
                    utilisateur.save()

                    return JsonResponse({"status": 0, "url": "/users_epicerie/"})
                else:
                    return JsonResponse(
                        {"status": "Votre mot de passe est incorrect !"}
                    )

            except Utilisateur.DoesNotExist:
                return JsonResponse({"status": "Vous n'êtes pas encore inscrit !"})

    else:
        return render(request, "connexion.html")  # Formulaire de connexion


def inscription(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        pseudo = request.POST.get("pseudo")
        mot_de_passe = request.POST.get("mot_de_passe")
        photo = request.FILES.get("photo")

        # Vérifier si tous les champs sont remplis
        if not all([nom, prenom, telephone, email, pseudo, mot_de_passe, photo]):
            return JsonResponse(
                {"status": "Veuillez remplir correctement tous les champs!"}
            )

        # Convertir nom et prenom en majuscules
        nom = nom.upper()
        prenom = prenom.upper()

        # Vérifier si le pseudo existe déjà
        if Utilisateur.objects.filter(pseudo=pseudo).exists():
            return JsonResponse(
                {"status": "Ce pseudo existe déjà, veuillez en choisir un autre."}
            )

        # Valider l'email
        try:
            EmailValidator()(email)
        except ValidationError:
            return JsonResponse({"status": "Votre email n'est pas valide"})

        # Vérifier l'extension de la photo
        extension_autorisees = [".jpg", ".jpeg", ".png"]
        _, extension = os.path.splitext(photo.name)
        if extension.lower() not in extension_autorisees:
            return JsonResponse({"status": "Veuillez choisir une photo en jpg ou png!"})

        # Générer le mot de passe haché
        mot_de_passe_hache = make_password(mot_de_passe)

        # Enregistrer l'utilisateur dans la base de données
        utilisateur = Utilisateur(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            email=email,
            pseudo=pseudo,
            mot_de_passe=mot_de_passe_hache,
            photo=photo,
        )
        utilisateur.save()

        return JsonResponse({"status": 0})  # Inscription réussie

    return render(request, "connexion.html")
