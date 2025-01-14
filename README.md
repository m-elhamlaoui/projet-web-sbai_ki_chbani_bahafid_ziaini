# Projet e-Commerce

## Objectif Principal
Créer une plateforme e-commerce complète et professionnelle en appliquant les bonnes pratiques de développement logiciel et en respectant les principes de conception orientée objet. Le projet doit inclure une architecture robuste et modulaire qui garantit l'évolutivité, la maintenabilité et la sécurité.

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
   - Support des bases relationnelles comme PostgreSQL.

6. **Documentation** :
   - README détaillé comprenant la description, les instructions d'installation, et un guide utilisateur.

---

## Stack Technique

- **Frontend** : HTML, CSS, JavaScript (optionnellement, intégrer Bootstrap pour le design responsive).
- **Backend** : Python avec Django.
- **Base de Données** : PostgreSQL (ou SQLite en mode développement).
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
