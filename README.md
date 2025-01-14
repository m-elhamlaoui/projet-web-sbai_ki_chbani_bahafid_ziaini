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
![Diagramme de cas d'utilisation](https://www.plantuml.com/plantuml/svg/VLHBRjim4Dtx58Diicc0-1zlYXXU55qKAEBc0AmqZgUbI9KpD7ebdKCNAodRf9YaMHXu7hpFu7deHnRbn3Twel4W81OSlHm5Qd9O2LapKPLO1pjDQ0GKm-uosTODcJZONWPxtxQ1vU9iFvdSmZCZL8gHuP0S9funpk1vDut4cs-sfaDKwS0Z4vYDYhaCDKBhx87qpKWq6qHFM1tHnKzWSQJLdYG0vKAYzDsBTOHWFJHMxYhTTsEF-U2n_MMzl3PGFdWOGZVcBmR-TyKSwDuWLBPfbAbnJ5eMfjw0EX43-uYl_c1z_1PiJbGLwjMWtbd3NaUzLg291UDsAOx7YlMW-DgqZfhBMWTLYNV1j-p--bkDn0-3-4lVkPWrBW0b5rW6RbwlEDuCMiNSTwLYUl-EX4K9iT0VZmmdKc48jUBZJwjSNQYdRvPKX0qQuQ6LlXDVap9IPkO3KUvb409RNL-Qr8Il1VEpeEzQQsg7eFpV2o_j5xpaJQlvuCTkY_4PV8BcUjtM0mUwewOykNANvSSTM--0_wTTbNK1Ywr-0meuhF1awHohD3h1Khc-LfPfnahOkyelyRsJdvxFw4VVwRwxzkqDEDMsribWT48Jus9vks1X3VXhXsEdT5oYAa5N5fzvi_D5xM_9SEN88Q10zBF6O1GEGK-epuiVgIt-UtPmT_SvnYKqIsYUq2AXPKAhXDRPPPDjxj_cvdUtlR0U4jeaDBtFS9hXBCDvXa7sSM0-oVrLiyXmcU4gmtM63nbk4WnHZsXgt-X_)

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


