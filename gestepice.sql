-- MySQL dump 10.13  Distrib 9.0.1, for macos15.1 (arm64)
--
-- Host: localhost    Database: gestepice
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id_admin` int NOT NULL AUTO_INCREMENT,
  `nom_admin` varchar(255) NOT NULL,
  `prenom_admin` varchar(255) NOT NULL,
  `pseudo_admin` varchar(255) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `photo` longtext NOT NULL,
  `status` varchar(255) NOT NULL,
  `derniere_date_connexion` datetime(6) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Admin','Admin','Admin','Admin','AdminAdmin.png','DECONNECTE','2025-01-12 22:29:16.227437');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add admin',7,'add_admin'),(26,'Can change admin',7,'change_admin'),(27,'Can delete admin',7,'delete_admin'),(28,'Can view admin',7,'view_admin'),(29,'Can add categorie',8,'add_categorie'),(30,'Can change categorie',8,'change_categorie'),(31,'Can delete categorie',8,'delete_categorie'),(32,'Can view categorie',8,'view_categorie'),(33,'Can add commande',9,'add_commande'),(34,'Can change commande',9,'change_commande'),(35,'Can delete commande',9,'delete_commande'),(36,'Can view commande',9,'view_commande'),(37,'Can add utilisateur',10,'add_utilisateur'),(38,'Can change utilisateur',10,'change_utilisateur'),(39,'Can delete utilisateur',10,'delete_utilisateur'),(40,'Can view utilisateur',10,'view_utilisateur'),(41,'Can add produit',11,'add_produit'),(42,'Can change produit',11,'change_produit'),(43,'Can delete produit',11,'delete_produit'),(44,'Can view produit',11,'view_produit'),(45,'Can add note',12,'add_note'),(46,'Can change note',12,'change_note'),(47,'Can delete note',12,'delete_note'),(48,'Can view note',12,'view_note'),(49,'Can add messages',13,'add_messages'),(50,'Can change messages',13,'change_messages'),(51,'Can delete messages',13,'delete_messages'),(52,'Can view messages',13,'view_messages'),(53,'Can add facture',14,'add_facture'),(54,'Can change facture',14,'change_facture'),(55,'Can delete facture',14,'delete_facture'),(56,'Can view facture',14,'view_facture'),(57,'Can add community',15,'add_community'),(58,'Can change community',15,'change_community'),(59,'Can delete community',15,'delete_community'),(60,'Can view community',15,'view_community'),(61,'Can add avis service',16,'add_avisservice'),(62,'Can change avis service',16,'change_avisservice'),(63,'Can delete avis service',16,'delete_avisservice'),(64,'Can view avis service',16,'view_avisservice'),(65,'Can add avis produit',17,'add_avisproduit'),(66,'Can change avis produit',17,'change_avisproduit'),(67,'Can delete avis produit',17,'delete_avisproduit'),(68,'Can view avis produit',17,'view_avisproduit'),(69,'Can add ligne commande',18,'add_lignecommande'),(70,'Can change ligne commande',18,'change_lignecommande'),(71,'Can delete ligne commande',18,'delete_lignecommande'),(72,'Can view ligne commande',18,'view_lignecommande'),(73,'Can add recommandation',19,'add_recommandation'),(74,'Can change recommandation',19,'change_recommandation'),(75,'Can delete recommandation',19,'delete_recommandation'),(76,'Can view recommandation',19,'view_recommandation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$TuRAgAcat0T2qwVBGJMuik$FGJkHdaj5gcCluTJ+Osaqu1sMLPKUU72j11octTr+tg=','2025-01-12 22:29:31.047756',1,'alidou','','','kialidou1@gmail.com',1,1,'2024-12-27 22:32:44.798278');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avis_produit`
--

DROP TABLE IF EXISTS `avis_produit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avis_produit` (
  `id_avis_produit` int NOT NULL AUTO_INCREMENT,
  `avis_produit` longtext NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `id_note_id` int NOT NULL,
  `id_produit_id` int NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id_avis_produit`),
  KEY `avis_produit_id_note_id_8e543b56_fk_note_id_note` (`id_note_id`),
  KEY `avis_produit_id_produit_id_13977a83_fk_produit_id_produit` (`id_produit_id`),
  KEY `avis_produit_id_utilisateur_id_eb5c4883_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `avis_produit_id_note_id_8e543b56_fk_note_id_note` FOREIGN KEY (`id_note_id`) REFERENCES `note` (`id_note`),
  CONSTRAINT `avis_produit_id_produit_id_13977a83_fk_produit_id_produit` FOREIGN KEY (`id_produit_id`) REFERENCES `produit` (`id_produit`),
  CONSTRAINT `avis_produit_id_utilisateur_id_eb5c4883_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avis_produit`
--

LOCK TABLES `avis_produit` WRITE;
/*!40000 ALTER TABLE `avis_produit` DISABLE KEYS */;
INSERT INTO `avis_produit` VALUES (1,'Tres delecieux','2022-12-19 21:20:40.000000',1,12,5),(2,'rafraichissant','2022-12-19 21:21:07.000000',2,18,5),(3,'bon','2022-12-19 21:22:35.000000',3,13,5),(4,'tres bon','2022-12-19 21:23:04.000000',4,16,5),(5,'j&#039;ai vraiment aime','2022-12-19 21:23:26.000000',5,14,5),(6,'tres bon tacos','2022-12-19 21:23:47.000000',6,15,5),(7,'ice','2022-12-19 21:24:07.000000',7,17,5),(8,'tres bon jus','2022-12-19 21:24:28.000000',8,19,5),(9,'delicieux','2022-12-19 21:24:52.000000',9,15,5),(10,'waouh','2022-12-19 21:25:19.000000',10,20,5),(11,'ok','2022-12-19 21:27:47.000000',11,22,5),(12,'cool','2022-12-19 21:28:01.000000',12,23,5),(13,'bon','2022-12-19 21:28:23.000000',13,24,5),(14,'Lavazza humm','2022-12-19 21:28:54.000000',14,25,5),(15,'naturel','2022-12-19 21:29:10.000000',15,26,5),(16,'tres bon Merendina','2022-12-19 21:50:19.000000',16,20,10),(17,'nice','2022-12-19 21:51:31.000000',17,12,10),(18,'hmmm','2022-12-19 21:52:22.000000',18,20,6),(19,'delicieux','2022-12-19 21:53:42.000000',19,16,6),(20,'j aime Tagger','2022-12-20 12:43:30.000000',20,22,11),(23,'tres bon couscous','2022-12-26 16:07:54.000000',23,12,18),(24,'bon','2024-03-21 20:28:57.000000',24,28,19),(28,'j\'aime','2025-01-10 15:04:14.405614',28,12,24);
/*!40000 ALTER TABLE `avis_produit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avisservice`
--

DROP TABLE IF EXISTS `avisservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avisservice` (
  `id_avis_service` int NOT NULL AUTO_INCREMENT,
  `avis_service` longtext NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id_avis_service`),
  KEY `avisservice_id_utilisateur_id_d43994b6_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `avisservice_id_utilisateur_id_d43994b6_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avisservice`
--

LOCK TABLES `avisservice` WRITE;
/*!40000 ALTER TABLE `avisservice` DISABLE KEYS */;
INSERT INTO `avisservice` VALUES (1,'Tres bon service',5),(2,'Je recommande leur service',7),(3,'Je suis epathe',10),(4,'cool service',6),(5,'Cool gestEpice',11),(8,'Tres  bon service',18),(14,'cool',24);
/*!40000 ALTER TABLE `avisservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie` (
  `id_categorie` int NOT NULL AUTO_INCREMENT,
  `nom_categorie` varchar(255) NOT NULL,
  PRIMARY KEY (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie`
--

LOCK TABLES `categorie` WRITE;
/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` VALUES (5,'Semoule'),(6,'Sandwitch'),(7,'Pizza'),(8,'Tacos'),(9,'Jus'),(10,'Boisson'),(11,'Biscuit'),(12,'Cafe');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commande`
--

DROP TABLE IF EXISTS `commande`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commande` (
  `id_commande` int NOT NULL AUTO_INCREMENT,
  `date_commande` datetime(6) NOT NULL,
  `montant_commande` decimal(10,2) NOT NULL,
  `commande_pret` varchar(10) NOT NULL,
  `paye` varchar(5) NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id_commande`),
  KEY `commande_id_utilisateur_id_a57fcc58_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `commande_id_utilisateur_id_a57fcc58_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commande`
--

LOCK TABLES `commande` WRITE;
/*!40000 ALTER TABLE `commande` DISABLE KEYS */;
INSERT INTO `commande` VALUES (1,'2022-12-19 21:22:10.000000',65.00,'OUI','OUI',5),(2,'2022-12-19 21:25:30.000000',38.00,'OUI','OUI',5),(3,'2022-12-19 21:29:40.000000',103.00,'OUI','OUI',5),(4,'2022-12-19 21:47:32.000000',73.00,'OUI','OUI',7),(5,'2022-12-19 21:47:55.000000',44.00,'OUI','OUI',7),(6,'2022-12-19 21:50:38.000000',128.00,'OUI','OUI',10),(7,'2022-12-19 21:52:48.000000',66.00,'OUI','OUI',6),(8,'2022-12-20 12:37:11.000000',38.00,'OUI','OUI',11),(11,'2022-12-26 16:09:39.000000',13.00,'OUI','OUI',18),(12,'2024-03-20 17:47:56.000000',68.00,'OUI','OUI',5),(13,'2024-03-20 18:05:46.000000',60.00,'OUI','NON',5),(14,'2024-03-21 20:14:42.000000',71.00,'OUI','NON',19),(15,'2024-03-21 20:15:08.000000',38.00,'OUI','NON',19),(16,'2024-03-21 20:15:41.000000',65.00,'OUI','NON',19),(17,'2024-03-21 20:24:21.000000',18.00,'OUI','NON',19),(18,'2024-03-25 22:17:23.000000',90.00,'OUI','NON',19),(19,'2024-03-26 13:44:27.000000',36.00,'OUI','NON',19),(20,'2025-01-11 11:02:25.175977',38.00,'NON','NON',24),(21,'2025-01-11 11:26:53.473613',68.00,'OUI','NON',24);
/*!40000 ALTER TABLE `commande` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `community`
--

DROP TABLE IF EXISTS `community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `community` (
  `id_message` int NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_envoi` datetime(6) NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id_message`),
  KEY `community_id_utilisateur_id_e1b7b8c0_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `community_id_utilisateur_id_e1b7b8c0_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `community`
--

LOCK TABLES `community` WRITE;
/*!40000 ALTER TABLE `community` DISABLE KEYS */;
INSERT INTO `community` VALUES (1,'SALUT','2022-12-19 21:41:09.000000',5),(2,'Salut ici\r\n\r\n','2022-12-19 21:54:01.000000',6),(3,'hi community\r\n','2022-12-19 21:54:28.000000',7),(4,'comment allez\r\n','2022-12-19 21:55:05.000000',10),(5,'vous','2022-12-19 21:55:09.000000',10),(6,'?','2022-12-19 21:55:13.000000',10),(7,'Salut c&#039;est Sousou','2022-12-20 12:40:52.000000',11),(11,'hi \r\n','2022-12-26 16:14:23.000000',18);
/*!40000 ALTER TABLE `community` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-12-28 02:35:31.965807','20','Utilisateur object (20)',3,'',10,1),(2,'2024-12-28 02:35:31.965877','1','Utilisateur object (1)',3,'',10,1),(3,'2025-01-09 16:04:41.528588','21','Utilisateur object (21)',3,'',10,1),(4,'2025-01-09 20:25:36.186504','23','Utilisateur object (23)',3,'',10,1),(5,'2025-01-09 20:25:36.186607','22','Utilisateur object (22)',3,'',10,1),(6,'2025-01-10 15:05:16.334115','27','AvisProduit object (27)',3,'',20,1),(7,'2025-01-10 15:05:16.334164','26','AvisProduit object (26)',3,'',20,1),(8,'2025-01-10 15:05:16.334174','25','AvisProduit object (25)',3,'',20,1),(9,'2025-01-10 16:19:11.540328','13','AvisService object (13)',3,'',21,1),(10,'2025-01-10 16:19:11.540381','12','AvisService object (12)',3,'',21,1),(11,'2025-01-10 16:19:11.540403','11','AvisService object (11)',3,'',21,1),(12,'2025-01-10 16:19:11.540421','10','AvisService object (10)',3,'',21,1),(13,'2025-01-10 16:19:11.540438','9','AvisService object (9)',3,'',21,1),(14,'2025-01-12 11:59:28.454668','16','Categorie object (16)',3,'',22,1),(15,'2025-01-12 11:59:28.454757','15','Categorie object (15)',3,'',22,1),(16,'2025-01-12 12:00:16.015998','14','Categorie object (14)',3,'',22,1),(17,'2025-01-12 12:01:28.464321','18','Categorie object (18)',3,'',22,1),(18,'2025-01-12 12:01:28.464382','17','Categorie object (17)',3,'',22,1),(19,'2025-01-12 12:01:47.930714','13','Categorie object (13)',3,'',22,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(22,'admins_epicerie','categorie'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'gestion_epicerie','admin'),(17,'gestion_epicerie','avisproduit'),(16,'gestion_epicerie','avisservice'),(8,'gestion_epicerie','categorie'),(9,'gestion_epicerie','commande'),(15,'gestion_epicerie','community'),(14,'gestion_epicerie','facture'),(18,'gestion_epicerie','lignecommande'),(13,'gestion_epicerie','messages'),(12,'gestion_epicerie','note'),(11,'gestion_epicerie','produit'),(19,'gestion_epicerie','recommandation'),(10,'gestion_epicerie','utilisateur'),(6,'sessions','session'),(20,'users_epicerie','avisproduit'),(21,'users_epicerie','avisservice');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-27 22:26:09.222909'),(2,'auth','0001_initial','2024-12-27 22:26:09.341838'),(3,'admin','0001_initial','2024-12-27 22:26:09.367560'),(4,'admin','0002_logentry_remove_auto_add','2024-12-27 22:26:09.370921'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-27 22:26:09.379839'),(6,'contenttypes','0002_remove_content_type_name','2024-12-27 22:26:09.403932'),(7,'auth','0002_alter_permission_name_max_length','2024-12-27 22:26:09.423594'),(8,'auth','0003_alter_user_email_max_length','2024-12-27 22:26:09.431986'),(9,'auth','0004_alter_user_username_opts','2024-12-27 22:26:09.445256'),(10,'auth','0005_alter_user_last_login_null','2024-12-27 22:26:09.467317'),(11,'auth','0006_require_contenttypes_0002','2024-12-27 22:26:09.467876'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-27 22:26:09.470242'),(13,'auth','0008_alter_user_username_max_length','2024-12-27 22:26:09.489267'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-27 22:26:09.503730'),(15,'auth','0010_alter_group_name_max_length','2024-12-27 22:26:09.510306'),(16,'auth','0011_update_proxy_permissions','2024-12-27 22:26:09.512672'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-27 22:26:09.524945'),(18,'gestion_epicerie','0001_initial','2024-12-27 22:26:09.756942'),(19,'sessions','0001_initial','2024-12-27 22:26:09.763933'),(20,'gestion_epicerie','0002_alter_produit_image_produit_alter_utilisateur_photo','2024-12-28 00:26:44.246860'),(21,'gestion_epicerie','0003_alter_messages_id_envoyeur_and_more','2024-12-28 02:00:15.089721');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9ciwsc7qxf64cvsre46vcq95pvi2o81l','.eJxdjk0KAjEMhe-S9WBnRFzMTjyAC3ElUkobZiL0xzZdyODd7VSR4iKBfO-9JAuk2YdAbpJaRYbxukCI3mTNkgyMMGyh-xGnLBZ2PF3OazVKiKRXad9v-r7hj6wcEz9hHBrz7NkXs1DGkksSQwlHQpFYMWlBVk0oqivJGiJO4r7bBDfB69ZBzUntnUPN5SzHjB04b8vSw6rVD_APJMzGt-D7Rp1r-xx4A9TGX2A:1tWiIe:NfNuCNJUPQ7UuES2HQxV0w6NcrEWbE_KQ6hDfY-2-gs','2025-01-25 20:41:40.783190'),('emg81d1kxekizkg2r6nicdl56w052v6z','.eJxVjEsOwjAMBe-SNYriJm1qluw5Q2XHDi2gROpnhbg7VOoCtm9m3ssMtK3jsC06D5OYswFz-t2Y0kPLDuRO5VZtqmWdJ7a7Yg-62GsVfV4O9-9gpGX81rnnTD0yspPosuuQgvfgE2LoooagObFK04h4h9D6pBxEI0ALsSU07w_zuTgK:1tX6SZ:vylo76C6yIJkCdIMrsXZg59UedyKj4zke6mgUX9E8Ac','2025-01-26 22:29:31.049539');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facture`
--

DROP TABLE IF EXISTS `facture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facture` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qte` int NOT NULL,
  `prix_produit` decimal(10,0) NOT NULL,
  `num_facture` varchar(255) NOT NULL,
  `id_commande_id` int NOT NULL,
  `id_produit_id` int NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `facture_id_commande_id_43ddeb56_fk_commande_id_commande` (`id_commande_id`),
  KEY `facture_id_produit_id_78680c3d_fk_produit_id_produit` (`id_produit_id`),
  KEY `facture_id_utilisateur_id_32561fa7_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `facture_id_commande_id_43ddeb56_fk_commande_id_commande` FOREIGN KEY (`id_commande_id`) REFERENCES `commande` (`id_commande`),
  CONSTRAINT `facture_id_produit_id_78680c3d_fk_produit_id_produit` FOREIGN KEY (`id_produit_id`) REFERENCES `produit` (`id_produit`),
  CONSTRAINT `facture_id_utilisateur_id_32561fa7_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=543 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facture`
--

LOCK TABLES `facture` WRITE;
/*!40000 ALTER TABLE `facture` DISABLE KEYS */;
INSERT INTO `facture` VALUES (498,1,60,'FAC12181',1,12,5),(499,1,5,'FAC12181',1,18,5),(500,1,7,'FAC1915202',2,19,5),(501,1,25,'FAC1915202',2,15,5),(502,2,6,'FAC1915202',2,20,5),(503,1,6,'FAC232425163',3,23,5),(504,1,4,'FAC232425163',3,24,5),(505,1,85,'FAC232425163',3,25,5),(506,1,8,'FAC232425163',3,16,5),(507,1,8,'FAC1612184',4,16,7),(508,1,60,'FAC1612184',4,12,7),(509,1,5,'FAC1612184',4,18,7),(510,3,39,'FAC13185',5,13,7),(511,1,5,'FAC13185',5,18,7),(512,2,120,'FAC1218206',6,12,10),(513,1,5,'FAC1218206',6,18,10),(514,1,3,'FAC1218206',6,20,10),(515,1,60,'FAC12207',7,12,6),(516,2,6,'FAC12207',7,20,6),(517,1,30,'FAC14168',8,14,11),(518,1,8,'FAC14168',8,16,11),(519,1,8,'FAC161811',11,16,18),(520,1,5,'FAC161811',11,18,18),(521,1,60,'FAC122212',12,12,5),(522,1,8,'FAC122212',12,22,5),(523,2,60,'FAC1413',13,14,5),(524,1,3,'FAC20161214',14,20,19),(525,1,8,'FAC20161214',14,16,19),(526,1,60,'FAC20161214',14,12,19),(527,1,30,'FAC141615',15,14,19),(528,1,8,'FAC141615',15,16,19),(529,1,5,'FAC181216',16,18,19),(530,1,60,'FAC181216',16,12,19),(531,1,18,'FAC2817',17,28,19),(532,1,60,'FAC12181518',18,12,19),(533,1,5,'FAC12181518',18,18,19),(534,1,25,'FAC12181518',18,15,19),(535,1,8,'FAC16201519',19,16,19),(536,1,3,'FAC16201519',19,20,19),(537,1,25,'FAC16201519',19,15,19),(538,1,13,'FAC13201620',20,13,24),(539,3,9,'FAC13201620',20,20,24),(540,2,16,'FAC13201620',20,16,24),(541,1,60,'FAC121621',21,12,24),(542,1,8,'FAC121621',21,16,24);
/*!40000 ALTER TABLE `facture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ligne_commande`
--

DROP TABLE IF EXISTS `ligne_commande`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ligne_commande` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qte` int NOT NULL,
  `id_commande_id` int NOT NULL,
  `id_produit_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ligne_commande_id_commande_id_id_produit_id_923f35ef_uniq` (`id_commande_id`,`id_produit_id`),
  KEY `ligne_commande_id_produit_id_ad0667b5_fk_produit_id_produit` (`id_produit_id`),
  CONSTRAINT `ligne_commande_id_commande_id_a8f43c88_fk_commande_id_commande` FOREIGN KEY (`id_commande_id`) REFERENCES `commande` (`id_commande`),
  CONSTRAINT `ligne_commande_id_produit_id_ad0667b5_fk_produit_id_produit` FOREIGN KEY (`id_produit_id`) REFERENCES `produit` (`id_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=486 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ligne_commande`
--

LOCK TABLES `ligne_commande` WRITE;
/*!40000 ALTER TABLE `ligne_commande` DISABLE KEYS */;
INSERT INTO `ligne_commande` VALUES (441,1,1,12),(442,1,1,18),(443,1,2,15),(444,1,2,19),(445,2,2,20),(446,1,3,16),(447,1,3,23),(448,1,3,24),(449,1,3,25),(450,1,4,12),(451,1,4,16),(452,1,4,18),(453,3,5,13),(454,1,5,18),(455,2,6,12),(456,1,6,18),(457,1,6,20),(458,1,7,12),(459,2,7,20),(460,1,8,14),(461,1,8,16),(462,1,11,16),(463,1,11,18),(464,1,12,12),(465,1,12,22),(466,2,13,14),(467,1,14,12),(468,1,14,16),(469,1,14,20),(470,1,15,14),(471,1,15,16),(472,1,16,12),(473,1,16,18),(474,1,17,28),(475,1,18,12),(476,1,18,15),(477,1,18,18),(478,1,19,15),(479,1,19,16),(480,1,19,20),(481,1,20,13),(482,3,20,20),(483,2,20,16),(484,1,21,12),(485,1,21,16);
/*!40000 ALTER TABLE `ligne_commande` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id_message` int NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_envoi` datetime(6) NOT NULL,
  `id_envoyeur` int NOT NULL,
  `id_recepteur` int NOT NULL,
  PRIMARY KEY (`id_message`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (22,'cc','2024-03-20 21:45:47.000000',0,5),(23,'cc aussi\r\n','2024-03-20 21:54:10.000000',5,0),(26,'salut','2024-03-26 13:45:43.000000',19,0),(27,'ccc','2024-03-26 13:48:45.000000',0,19),(28,'Bonjour','2025-01-11 15:05:16.150784',24,0),(29,'comment vas-tu ?','2025-01-12 22:14:06.848843',0,19),(30,'mzyan ?\r\n','2025-01-12 22:15:43.793684',0,5);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `note`
--

DROP TABLE IF EXISTS `note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `note` (
  `id_note` int NOT NULL AUTO_INCREMENT,
  `note` decimal(10,2) NOT NULL,
  `id_produit_id` int NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id_note`),
  KEY `note_id_produit_id_c0e6da29_fk_produit_id_produit` (`id_produit_id`),
  KEY `note_id_utilisateur_id_b8905927_fk_utilisateurs_id_utilisateur` (`id_utilisateur_id`),
  CONSTRAINT `note_id_produit_id_c0e6da29_fk_produit_id_produit` FOREIGN KEY (`id_produit_id`) REFERENCES `produit` (`id_produit`),
  CONSTRAINT `note_id_utilisateur_id_b8905927_fk_utilisateurs_id_utilisateur` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `note`
--

LOCK TABLES `note` WRITE;
/*!40000 ALTER TABLE `note` DISABLE KEYS */;
INSERT INTO `note` VALUES (1,3.60,12,5),(2,4.70,18,5),(3,3.30,13,5),(4,2.90,16,5),(5,2.60,14,5),(6,3.80,15,5),(7,4.50,17,5),(8,2.40,19,5),(9,2.40,15,5),(10,4.40,20,5),(11,3.60,22,5),(12,2.60,23,5),(13,2.60,24,5),(14,3.40,25,5),(15,2.30,26,5),(16,4.60,20,10),(17,4.50,12,10),(18,3.40,20,6),(19,4.60,16,6),(20,3.70,22,11),(23,3.80,12,18),(24,4.00,28,19),(25,3.50,12,24),(26,3.50,12,24),(27,3.40,12,24),(28,3.50,12,24);
/*!40000 ALTER TABLE `note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produit`
--

DROP TABLE IF EXISTS `produit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produit` (
  `id_produit` int NOT NULL AUTO_INCREMENT,
  `nom_produit` varchar(255) NOT NULL,
  `qte_en_stock` int NOT NULL,
  `seuil_min` int NOT NULL,
  `prix` decimal(10,2) NOT NULL,
  `prix_promotion` decimal(10,2) NOT NULL,
  `image_produit` varchar(255) DEFAULT NULL,
  `description` longtext NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `admin` varchar(5) NOT NULL,
  `auteur` varchar(255) NOT NULL,
  `id_categorie_id` int NOT NULL,
  PRIMARY KEY (`id_produit`),
  KEY `produit_id_categorie_id_cb28aa99_fk_categorie_id_categorie` (`id_categorie_id`),
  CONSTRAINT `produit_id_categorie_id_cb28aa99_fk_categorie_id_categorie` FOREIGN KEY (`id_categorie_id`) REFERENCES `categorie` (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produit`
--

LOCK TABLES `produit` WRITE;
/*!40000 ALTER TABLE `produit` DISABLE KEYS */;
INSERT INTO `produit` VALUES (12,'COUSCOUS',8,6,60.00,60.00,'admins_epicerie/static/image/photos_produits/j4.png','Ingredient: \r\ntomates\r\n pilons de poulet (fermier de préférence).-de pois chiches -courgettes\r\n- carottes-tomate\r\n\r\n','2022-12-10 20:24:11.000000','NON','ASMAE',5),(13,'Sandwitch',1,4,350.00,13.00,'admins_epicerie/static/image/photos_produits/p3-removebg-preview.png','Ingredient :\r\nviande \r\nhache\r\nfromage\r\n Concombre\r\ntomate','2022-12-17 20:28:47.000000','NON','BAWBA',6),(14,'Pizza Poulet',2,1,30.00,30.00,'admins_epicerie/static/image/photos_produits/j3.png','Ingredient :\r\npoulet\r\n fromage\r\nConcombre\r\ntomate ','2022-12-09 20:32:55.000000','NON','Alassane',7),(15,'Tacos Poulet',0,10,25.00,25.00,'admins_epicerie/static/image/photos_produits/j1.png','Ingredient :\r\npoulet\r\nfromage \r\nTime : 15 min ','2022-12-14 20:35:48.000000','OUI','',8),(16,'jus d orange',40,1,10.00,8.00,'admins_epicerie/static/image/photos_produits/p8.png','Time : 5 min ','2022-12-16 20:38:08.000000','OUI','',9),(17,'jus citron',27,1,18.00,13.00,'admins_epicerie/static/image/photos_produits/j.png','Time : 5 min ','2022-12-19 20:39:05.000000','OUI','',9),(18,'Fanta',23,1,6.00,5.00,'admins_epicerie/static/image/photos_produits/GD_SD01106-Untitled-1.png','Fun et décalée, Fanta est la boisson pétillante au goût fruité qui met une touche de fraîcheur et de couleur dans le quotidien de chacun','2022-12-15 20:49:24.000000','OUI','',10),(19,'Poms',14,3,8.00,7.00,'admins_epicerie/static/image/photos_produits/poms.png','Un jus de pomme pétillant','2022-12-19 20:52:15.000000','OUI','',10),(20,'Merendina',104,2,3.00,3.00,'admins_epicerie/static/image/photos_produits/merendina.png','Merendina, la génoise gourmande, généreuse et délicieusement enrobée de cacao','2022-12-20 20:53:59.000000','OUI','',11),(22,'Tagger',4,7,8.00,8.00,'admins_epicerie/static/image/photos_produits/tagger.png','Biscuit Gaufrette Tagger au Cacao Bimo 10x24 g','2022-12-19 20:56:45.000000','OUI','',11),(23,'Sprite',37,6,8.00,6.00,'admins_epicerie/static/image/photos_produits/sprite.png','Boisson fraiche','2022-12-21 20:57:30.000000','OUI','',10),(24,'Okey',0,7,5.00,4.00,'admins_epicerie/static/image/photos_produits/okey.png','OKEY Biscuits Fourrés et Enrobés au Cacao','2022-12-10 20:58:36.000000','OUI','',11),(25,'Lavazza',10,1,15.00,10.00,'admins_epicerie/static/image/photos_produits/j1.jpg','Café torréfié moulu en capsules\r\n\r\nLa douceur et les notes fruitées des Arabicas d\'Asie et d\'Amérique latine','2022-12-11 21:03:45.000000','OUI','',12),(26,'Les Cafés Duluxe',13,1,110.00,98.00,'admins_epicerie/static/image/photos_produits/j2.jpg','Conditionnement : 1 Kg Espresso de meilleur goût et excellente crema.\r\nMélange 100% Robusta\r\nGrains de Qualité Prémium\r\n100 % Naturel','2022-12-16 21:05:27.000000','OUI','',12),(28,'Tajine',5,2,20.00,18.00,'admins_epicerie/static/image/photos_produits/23.png',' Tajine Tajine Tajine  Tajine Tajine Tajine','2024-03-21 20:22:10.000000','NON','Zahira',5),(29,'grenadine',15,5,10.00,10.00,'admins_epicerie/static/image/photos_produits/images.jpeg','grenadine','2025-01-12 12:16:49.845717','OUI','',9);
/*!40000 ALTER TABLE `produit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recommandation`
--

DROP TABLE IF EXISTS `recommandation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recommandation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `id_produit_id` int NOT NULL,
  `id_utilisateur_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `recommandation_id_produit_id_id_utilisateur_id_b1c349c6_uniq` (`id_produit_id`,`id_utilisateur_id`),
  KEY `recommandation_id_utilisateur_id_4a135617_fk_utilisate` (`id_utilisateur_id`),
  CONSTRAINT `recommandation_id_produit_id_9ec6b266_fk_produit_id_produit` FOREIGN KEY (`id_produit_id`) REFERENCES `produit` (`id_produit`),
  CONSTRAINT `recommandation_id_utilisateur_id_4a135617_fk_utilisate` FOREIGN KEY (`id_utilisateur_id`) REFERENCES `utilisateurs` (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=357 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommandation`
--

LOCK TABLES `recommandation` WRITE;
/*!40000 ALTER TABLE `recommandation` DISABLE KEYS */;
INSERT INTO `recommandation` VALUES (321,12,6),(322,12,7),(323,12,10),(324,12,18),(353,12,24),(325,13,5),(326,13,10),(327,13,19),(355,13,24),(328,14,5),(329,14,18),(354,14,24),(330,15,5),(356,15,24),(331,16,5),(332,16,6),(333,16,7),(334,16,10),(335,17,5),(336,18,5),(337,18,7),(338,18,18),(339,18,19),(340,19,5),(341,19,19),(342,20,5),(343,20,6),(344,20,10),(345,20,19),(346,22,5),(347,23,5),(348,24,5),(349,25,5),(350,26,5),(352,28,19);
/*!40000 ALTER TABLE `recommandation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateurs` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pseudo` varchar(255) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `derniere_connexion` datetime(6) NOT NULL,
  `solde` decimal(10,2) NOT NULL,
  `date_inscription` datetime(6) NOT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateurs`
--

LOCK TABLES `utilisateurs` WRITE;
/*!40000 ALTER TABLE `utilisateurs` DISABLE KEYS */;
INSERT INTO `utilisateurs` VALUES (5,'AYA','MOUKIL','+212 06 45 45 54','aya123@gmail.com','Aya11','$2y$10$FqBIl6ywdTbBxemtcLDlbOrLCiNdNuCze45OVSGEm8TbH9SlgsI2O','users_epicerie/static/image/photos_utilisateurs/Aya1165f4f6d7-dab4-480e-868c-044e66cf3f92_alta-libre-aspect-ratio_default_0.jpg','DECONNECTE','2024-03-21 07:40:43.000000',60.00,'2023-12-19 21:10:46.000000'),(6,'ABDELGHAFOUR','NAIM','+212 06 45 45 54','naim@gmail.com','Naim12','$2y$10$q/a6itRDepB7xvxVeeJe5OKi99a2xOZNKkPnsn1ZOh3Zjo2eeseam','users_epicerie/static/image/photos_utilisateurs/Naim120_e2FeM-WKmvdXJs9W.jpg','DECONNECTE','2024-03-21 01:17:50.000000',160.00,'2022-12-19 21:12:28.000000'),(7,'MOHAMED','AMINE','+212 06 45 45 54','mohamed@gmail.com','Mohamed12','$2y$10$zu/rfKG0Q201pD7Qi97AwOjZUcd79Gt8DxrFQdy7t.bhhwqxhNnza','users_epicerie/static/image/photos_utilisateurs/Mohamed12271b25d30396b0eba2d2fc3d57fa2a58.jpg','DECONNECTE','2024-03-21 01:21:53.000000',127.00,'2021-12-19 21:13:31.000000'),(10,'MEGZARI','AMINA','+212 06 45 45 54','amina@gmail.com','Amina11','$2y$10$wzSDi7S/CMSDDGR.dp5NqeiTBY2KMoSE9ScX5RyfcmHD2Yhpl4DB6','users_epicerie/static/image/photos_utilisateurs/Zahira11Zahira11zahira.PNG','DECONNECTE','2024-03-21 07:50:42.000000',2.00,'2022-12-19 21:18:21.000000'),(11,'MHAREK','YASMINE','+212 06 45 45 54','yasmine@gmail.com','Yasmine11','$2y$10$xcyZpnJ0k/q1vKxYFJFyzeCYXlVLwmOP6YERJpk7BMVkp36jCl1IK','users_epicerie/static/image/photos_utilisateurs/Yasmine11download.jpeg','DECONNECTE','2024-03-21 01:25:01.000000',82.00,'2022-12-19 21:19:11.000000'),(18,'SALTANI','AMINE','+212 06 45 45 54','amine@gmal.com','A12','$2y$10$KARY5JovQQ3JDzUrdkeDXuPxypbHrYxXKpjpllpiSI55ozLAVJ7He','users_epicerie/static/image/photos_utilisateurs/A12ts.jpg','DECONNECTE','2022-12-26 04:20:52.000000',107.00,'2022-12-26 16:04:55.000000'),(19,'SALMA','MARRAKCHI','+212 0675234','salma@inpt.com','Salma11','$2y$10$POl87kL4agRRkCiCzzyd8.oEjqRsUsiQZDQM4LBPjL85ThVcyreNG','users_epicerie/static/image/photos_utilisateurs/Salma11pngtree-anime-girl-with-bright-eyes-and-a-long-dark-hair-picture-image_3158232.jpg','DECONNECTE','2024-03-26 01:45:51.000000',100.00,'2024-03-21 19:55:14.000000'),(24,'KI','ALIDOU','0674521757','alidou@gmail.com','alidou12','pbkdf2_sha256$870000$0xoYbpdEoAM9kFZkkfnY0G$hfUd1G9SRNW/RopPuK8YCwUinIlSoHPD12KUM7MAcdc=','users_epicerie/static/image/photos_utilisateurs/alidou12_4670751.jpg','DECONNECTE','2025-01-11 17:35:53.312637',20.00,'2025-01-09 20:33:45.913711');
/*!40000 ALTER TABLE `utilisateurs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-12 23:41:25
