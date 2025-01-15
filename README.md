<a name="top"></a>

# Projet e-Commerce

## Table des Matières

1. [Introduction](#introduction)
   - [Objectifs du Projet](#objectifs-du-projet)
   - [Description Générale](#description-générale)
2. [Technologies et Outils Utilisés](#technologies-et-outils-utilisés)
3. [Architecture et Design](#architecture-et-design)
   - [Diagramme de Classes](#diagramme-de-classes)
   - [Diagramme de Cas d'Utilisation](#diagramme-de-cas-dutilisation)
4. [Fonctionnalités](#fonctionnalités)
   - [Client](#client)
   - [Administrateur](#administrateur)
   - [Fournisseur](#fournisseur)
5. [Bonnes Pratiques de Développement](#bonnes-pratiques-de-développement)
   - [Patrons de Conception](#patrons-de-conception)
   - [Conformité à SOLID et Clean Code](#conformité-à-solid-et-clean-code)
   - [Conformité à PEP8](#conformité-à-pep8)
   - [Utilisation de Linters](#utilisation-de-linters)
   - [Git Workflow](#git-workflow)
   - [Tests Unitaires](#tests-unitaires)
6. [Structure du Backend](#structure-du-backend)
7. [Prise en Main](#prise-en-main)
   - [Prérequis](#prérequis)
   - [Installation et Configuration](#installation-et-configuration)
8. [Gestion Multilingue](#gestion-multilingue)
9. [Hachage des Mots de Passe](#hachage-des-mots-de-passe)
   - [Fichier `.properties`](#fichier-properties)
   - [Hachage des Utilisateurs](#hachage-des-utilisateurs)
10. [Aperçu de l’Application](#aperçu-de-lapplication)
11. [Base de Données](#base-de-données)
    - [Modèle Conceptuel](#modèle-conceptuel)
    - [Diagramme Entité-Relation (ERD)](#diagramme-entité-relation-erd)
12. [API et Points de Terminaison](#api-et-points-de-terminaison)
    - [Endpoints Client](#endpoints-client)
    - [Endpoints Admin](#endpoints-admin)
    - [Endpoints Fournisseur](#endpoints-fournisseur)
13. [Système de Build](#système-de-build)
14. [Versionnement et Suivi des Issues](#versionnement-et-suivi-des-issues)
15. [Déploiement](#déploiement)
    - [Environnement de Production](#environnement-de-production)
    - [Hébergement](#hébergement)
16. [Limites et Améliorations Futures](#limites-et-améliorations-futures)
17. [Annexes](#annexes)
    - [Ressources Utilisées](#ressources-utilisées)
    - [Références](#références)

   
---


## Introduction

### Objectifs du Projet
Le projet vise à développer une plateforme e-commerce performante et sécurisée, capable de répondre aux besoins de trois types d’utilisateurs principaux : les Clients, les Administrateurs, et les Fournisseurs. Les principaux objectifs sont :
- **Fournir une expérience utilisateur intuitive** grâce à une interface simple et fluide.
- **Automatiser les processus métiers** comme la gestion des produits, commandes et rapports.
- **Assurer la sécurité des données** en utilisant des techniques modernes de chiffrement et de gestion des utilisateurs.
- **Permettre une évolutivité facile** en adoptant une architecture modulaire et conforme aux bonnes pratiques.
- **Faciliter l’intégration multilingue** pour rendre la plateforme accessible à un large public.

### Description Générale
La plateforme e-commerce est une application web complète et modulable conçue pour répondre aux besoins variés des utilisateurs. Elle repose sur :
- **Un backend robuste** développé avec **Django**, couplé à une base de données relationnelle **MySQL**, garantissant la fiabilité des opérations et la gestion des données.
- **Une architecture modulaire** conforme aux principes SOLID, facilitant la maintenabilité et l’extensibilité du projet.
- **Un système multilingue générique**, permettant d’ajouter facilement de nouvelles langues pour une meilleure accessibilité.
- **Un mécanisme de sécurité avancé**, intégrant le hachage des mots de passe et la gestion des rôles utilisateurs (Clients, Administrateurs, Fournisseurs).
- **Des fonctionnalités sur mesure** :
  - **Pour les Clients** : Recherche de produits, gestion des commandes, et suivi des achats.
  - **Pour les Administrateurs** : Gestion des produits et catégories, tableau de bord statistique, et interaction via le chat.
  - **Pour les Fournisseurs** : Ajout de produits, suivi des commandes, et consultation des rapports de vente.

Ce projet est conçu pour être à la fois performant, maintenable et facilement déployable dans un environnement de production.


[⬆️ Back to top](#top)


---


## Technologies et Outils Utilisés

Le projet repose sur une stack technologique moderne et des outils robustes pour assurer sa performance, sa maintenabilité, et sa sécurité. Voici les principaux éléments utilisés :

### Backend
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
- ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

### Frontend
- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)&nbsp;![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)&nbsp;![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

### Sécurité
- **bcrypt** : Utilisé pour le hachage des mots de passe.
- **Validation des entrées utilisateur** : Implémentée pour protéger contre les failles courantes telles que les injections SQL et XSS.

### Outils DevOps et Build
- ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
- ![pip](https://img.shields.io/badge/pip-blueviolet?style=for-the-badge&logo=pypi&logoColor=white)
- ![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
- ![Virtualenv](https://img.shields.io/badge/Virtualenv-red?style=for-the-badge&logo=python&logoColor=white)

### Tests et Qualité
- ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
- ![Flake8](https://img.shields.io/badge/Flake8-blue?style=for-the-badge&logo=python&logoColor=white)

### Outils Supplémentaires
- ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
- ![PlantUML](https://img.shields.io/badge/PlantUML-brightgreen?style=for-the-badge&logo=plantuml&logoColor=white)

Cette combinaison de technologies garantit une application robuste, maintenable et facile à étendre.


---
































## Description Fonctionnelle

### Utilisateurs et Rôles

#### **Client**
Le client peut :
- S'inscrire et se connecter.
- Modifier ses informations de profil.
- Ajouter un avis sur le service Gestepice.
- Ajouter un avis et recommander des produits.
- Rechercher des produits par catégorie et/ou mot-clé.
- Consulter la liste de ses commandes et imprimer les factures.
- Ajouter des produits au panier et passer une commande.
- Contacter l'administrateur via un chat en temps réel.

#### **Administrateur**
L'administrateur peut :
- Consulter les différentes statistiques de l’épicerie via un **dashboard interactif**.
- Ajouter, modifier et supprimer des produits et catégories.
- Consulter la liste des commandes passées.
- Consulter la liste des produits fabriqués par les étudiants de l'INPT et gérer les paiements pour ces derniers.
- Recharger le solde des utilisateurs.
- Répondre aux préoccupations des clients via un chat.

#### **Fournisseur**
Le fournisseur peut :
- S'inscrire et se connecter pour accéder à son espace dédié.
- Ajouter, modifier et supprimer ses produits disponibles sur la plateforme.
- Consulter les commandes des clients pour ses produits spécifiques.
- Suivre l’état de paiement pour les commandes de ses produits.
- Recevoir des notifications pour les commandes des clients.
- Gérer les stocks et voir les alertes en cas de rupture de stock.
- Télécharger un rapport des ventes mensuelles pour ses produits.

---

## Diagramme de Classes

### Description
Le diagramme de classes ci-dessous représente la structure conceptuelle du projet e-commerce, en montrant les principales entités (Client, Admin, Supplier, Product, Order, Review, et Chat) ainsi que leurs relations. Il est essentiel pour comprendre l'organisation des données et des interactions dans le système.

### Diagramme
![Diagramme de classes](https://www.plantuml.com/plantuml/png/jPN1RiCs38RlUGeZbsqOUkWr68eEtMaOrc5z086Lc9YOB7aadI0OzkwpOyQ9DNNe3iqXW7xzfibF5Fqi2gn35pVVD3_XdX8sscBp4WcJDZw2oERoVvN-sZJZx_k6mgwXfBOQ13b1Xxj6b2aTJEv1v9Gv539sGB6qSjvJHDUJru7BG2GE1cqnANbG70E-vnnja_50eiZVVcT2p0TAoshe0oWwUy4YGmYEyKXuMYH1ODzEpZ1ubKMVJ2vpGBvfFLDIH-cOoQ-3QdOUM6_E21xdnnVDjw3kHDew2DqbrxytwnFuST9N1p0hNyK_WBJl6JYu00gxvkUtrr-hE3j8SC05KgbxK3na9gpXApJH8M3IVySQ1OyYDmESEqnt1iQH88-lUuS8oUFTXlGvpOSmCfOAsRUXxoCXh-0kubVnfNJ4f9dFk-ON4ltXjxdcfy_riC5TWlmdMsNmVrIP8HtHfQoq9mzAETrsGpwbc24uWOZY6FlCMg5dUQ_WNRKwkmgtWEAP-Yc3aYYJ7ztxc45D4irZENyEa9JqV1_PUkrSn9XljHZeto-hfxiBQkrM3eXI3XXn9PSeNZcikyYKEWP_cPzkBLfmgJU5PeNeeCj3qf89w215tPuH58E3qJnLfDIXRHqm8O_ITM1LgfavhSenwN_NKweCEcQvUZXtKtD-fe0opvSMLjqt2_KS1LD0BhAnUr3A7Oh0eUnKmQG5q2MoiqVA6sPw2PanpdUkfLuszZdTFcwRXuTcsq4wRwr_TlCdGpRpScsn5XbDFYS5IlLGTdQZxSIaOonRs-xaUxmFnZ2Pva_C1o-q8LHtMGwxPJBBTJJNxIrCPflMuZJNgp0V9LAwP6Xp-cCgFUSZXS9PGJpHA4tbQ-qyPJqoDy-Omj35Vm00)

---

## Diagramme de Cas d'Utilisation

### Description
Le diagramme de cas d'utilisation ci-dessous représente les principales interactions entre les acteurs du système (Client, Admin, Supplier) et les fonctionnalités qu'ils peuvent effectuer. Les cas d'utilisation communs à plusieurs acteurs (comme "S'inscrire et se connecter" et "Contacter via le chat") sont également mis en évidence.

### Diagramme
![Diagramme de cas d'utilisation](https://www.plantuml.com/plantuml/png/dLHBRjim4Dtx58Diicc0o7yNGH33YoAB0aNS782LnZ5RYbJvCNebdKCNwr0VIdGYBR8myCHvxmtvEFIJiKnRbukPm9C5gq3pjxE5Z6jCBLTonbAhD1m4Hsc16JYqA_iivz8lxDk5eoiAOcc_TfpDRk7L8AJCe85JS9WvWtuDNW-99zvyLna_UPKW7fV4p9dlQo13ABGwSN4p4CrhqGkcPzJ-HopZQPdZbW3JrD5MvPlI744vo9MzIqLL3ZqMjSV-jtBsse0vyf0SzP2_hFa_c354Tv8EfVASoGo7f5LawYYP2pTWdCUTFoZdlyZcmjD8lQxL1pgs4rul60XkBFhTXNPcgDZKYkUyq3nljtLYgNMQVEFikxiQYBUr-5jLQjzh603QFi2uuUvwYyETKMh6L6MiIEu_a1ZBB9sC_tNqSU6C5Y5ZvlnBCPr5wkJT9Xd77AKrTIfLQLt66Nr6gdv0c7whXM2KoDea1SThmQ8HL6MXPAOHcFlNyiB-oCk-JpKC_D1jEHo3Bv1tqwqS6A9hdiSZ5-zbDPsnSXhCc7OTnqL1g_IFlq-DALuKRzeoWTfYhDnqaVKqgIpjEmqlySEHJven-bcLzC2wl9q4pOf2QLiRNL3wTZwy0rae2QxBSEWKXikorAAEWn-y_cQYZhTScbHpZVvytaz9YLvODtgMgN0PWaRH7E3CY-W_Y1h2tTrZO_WL7XvuetXyfD9olBGQBwt7IvlnKh8RguqV8pndUiRZphk9flSJjMIYDf-eBJvraF22_CkPS5zDrDOJjQdejv-ybfUngJgqeYIWUK2BW9O1hG9Q1xJfNNPni_Zkzorh6z0keEI-XqaFvprS49pk4Yxcs16NFLprSDt3JG-t0PB_4yhCvU8_)

---

## Description Non-Fonctionnelle

### Exigences Techniques
1. **Architecture** :
   - Basée sur le framework Django (MVC/MVT).
   - Structure modulaire et réutilisable avec des apps Django.

2. **Performance** :
   - Temps de réponse inférieur à 2 secondes pour toutes les requêtes utilisateur.

3. **Sécurité** :
   - Utilisation de Django pour la gestion des sessions et de l’authentification.
   - Prévention des attaques CSRF et XSS via les middlewares Django.

4. **Portabilité** :
   - Compatible avec les principaux navigateurs (Chrome, Firefox, Edge).
   - Déploiement sur des serveurs web comme Nginx ou Apache avec Gunicorn.

5. **Base de Données** :
   - MySQL pour la base relationnelle.

6. **Documentation** :
   - README détaillé comprenant la description, les instructions d'installation, et un guide utilisateur.

---

## Stack Technique

- **Frontend** : HTML, CSS, JavaScript (optionnellement, intégrer Bootstrap pour le design responsive).
- **Backend** : Python avec Django.
- **Base de Données** : MySQL.
- **Serveur Web** : Gunicorn/Nginx.
- **Outils de Build** : Gestion des dépendances avec `pip` et `virtualenv`.
- **Contrôle de Version** : Git (avec utilisation de GitHub/GitLab pour la gestion des issues).

---

## Plan de Développement

1. **Phase 1 : Analyse et Conception** :
   - Création des diagrammes UML : cas d’utilisation, classes, et séquences.
   - Définition de la structure des modèles Django.

2. **Phase 2 : Développement** :
   - Mise en place de l’environnement Django avec un projet initial.
   - Création des apps principales :
     - `users` pour la gestion des utilisateurs.
     - `products` pour les produits.
     - `orders` pour les commandes.
     - `reviews` pour les avis.
     - `chat` pour la messagerie en temps réel.
   - Développement des fonctionnalités principales.

3. **Phase 3 : Tests** :
   - Rédaction et exécution de tests unitaires avec `pytest` ou `Django Test`.
   - Tests fonctionnels pour validation des cas d’utilisation.

4. **Phase 4 : Documentation et Livraison** :
   - Création d’une vidéo démonstrative.
   - Livraison du code source dans un dépôt Git.


