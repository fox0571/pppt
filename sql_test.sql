-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: service
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add partsinv',1,'add_partsinv'),(2,'Can change partsinv',1,'change_partsinv'),(3,'Can delete partsinv',1,'delete_partsinv'),(4,'Can add unit basic info',2,'add_unitbasicinfo'),(5,'Can change unit basic info',2,'change_unitbasicinfo'),(6,'Can delete unit basic info',2,'delete_unitbasicinfo'),(7,'Can add part request',3,'add_partrequest'),(8,'Can change part request',3,'change_partrequest'),(9,'Can delete part request',3,'delete_partrequest'),(10,'Can add users',4,'add_users'),(11,'Can change users',4,'change_users'),(12,'Can delete users',4,'delete_users'),(13,'Can add log entry',5,'add_logentry'),(14,'Can change log entry',5,'change_logentry'),(15,'Can delete log entry',5,'delete_logentry'),(16,'Can add permission',6,'add_permission'),(17,'Can change permission',6,'change_permission'),(18,'Can delete permission',6,'delete_permission'),(19,'Can add group',7,'add_group'),(20,'Can change group',7,'change_group'),(21,'Can delete group',7,'delete_group'),(22,'Can add user',8,'add_user'),(23,'Can change user',8,'change_user'),(24,'Can delete user',8,'delete_user'),(25,'Can add content type',9,'add_contenttype'),(26,'Can change content type',9,'change_contenttype'),(27,'Can delete content type',9,'delete_contenttype'),(28,'Can add session',10,'add_session'),(29,'Can change session',10,'change_session'),(30,'Can delete session',10,'delete_session'),(31,'Can add time record',11,'add_timerecord'),(32,'Can change time record',11,'change_timerecord'),(33,'Can delete time record',11,'delete_timerecord'),(34,'Can add invoice',12,'add_invoice'),(35,'Can change invoice',12,'change_invoice'),(36,'Can delete invoice',12,'delete_invoice');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$VDBsZqdQzn1R$igFVjh5QIcqI3B9TX6BGk27Q/K6IyEUfaAOIzsWD2rc=','2018-06-17 18:50:18.481045',1,'fox','','','ben.h@smartkitchenservice.com',1,1,'2018-06-11 16:12:38.059528');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-06-11 16:58:50.152205','1','Jane',1,'[{\"added\": {}}]',4,1),(2,'2018-06-11 16:59:08.386596','2','Yesi',1,'[{\"added\": {}}]',4,1),(3,'2018-06-11 16:59:25.042859','3','Chloe',1,'[{\"added\": {}}]',4,1),(4,'2018-06-11 16:59:49.683507','4','Christina',1,'[{\"added\": {}}]',4,1),(5,'2018-06-11 17:00:57.386696','5','Daniela',1,'[{\"added\": {}}]',4,1),(6,'2018-06-11 17:01:15.777328','6','Samantha',1,'[{\"added\": {}}]',4,1),(7,'2018-06-11 17:01:35.902365','7','Katrina',1,'[{\"added\": {}}]',4,1),(8,'2018-06-11 17:01:52.949233','8','Amanda',1,'[{\"added\": {}}]',4,1),(9,'2018-06-11 17:02:07.199250','9','Randi',1,'[{\"added\": {}}]',4,1),(10,'2018-06-11 17:02:27.089889','10','Brandon',1,'[{\"added\": {}}]',4,1),(11,'2018-06-11 17:02:44.855529','11','Anna',1,'[{\"added\": {}}]',4,1),(12,'2018-06-11 17:02:59.339923','12','Jackie',1,'[{\"added\": {}}]',4,1),(13,'2018-06-11 17:03:25.652442','13','Warranty Check',1,'[{\"added\": {}}]',4,1),(14,'2018-06-11 17:04:05.621221','14','ADMIN',1,'[{\"added\": {}}]',4,1),(15,'2018-06-11 17:04:21.730609','15','Parts',1,'[{\"added\": {}}]',4,1),(16,'2018-06-11 20:47:32.896560','1','MBF800407716120700C40016',2,'[{\"changed\": {\"fields\": [\"businessName\", \"phone\", \"email\", \"location_add2\", \"location_city\", \"location_state\", \"location_zip\", \"warrantyNote\", \"tsq\", \"techNote\", \"followup_customer\", \"followup_tech\"]}}]',2,1),(17,'2018-06-11 21:06:17.053755','3','SKS062018-D5-1',2,'[{\"changed\": {\"fields\": [\"location_add2\", \"pre_diagnosis\"]}}]',3,1),(18,'2018-06-11 23:12:00.169395','2','Yesi',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(19,'2018-06-11 23:12:07.481900','3','Chloe',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(20,'2018-06-11 23:12:17.325656','4','Christina',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(21,'2018-06-11 23:12:26.841291','5','Daniela',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(22,'2018-06-11 23:12:37.481957','6','Samantha',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(23,'2018-06-11 23:12:47.403843','7','Katrina',2,'[{\"changed\": {\"fields\": [\"code\"]}}]',4,1),(24,'2018-06-11 23:56:30.921629','2','MBF8001GRAUS100318010100C40001',3,'',2,1),(25,'2018-06-12 14:29:29.356200','4','MBF850707717010400C40031',3,'',2,1),(26,'2018-06-12 14:29:29.387446','3','MBF8507AUS100317031400C43738',3,'',2,1),(27,'2018-06-12 14:29:29.403014','1','MBF800407716120700C40016',3,'',2,1),(28,'2018-06-12 14:29:41.668712','5','SKS062018-D1-1',3,'',3,1),(29,'2018-06-12 14:29:41.699984','4','SKS062018-D1-1',3,'',3,1),(30,'2018-06-12 14:29:41.699984','3','SKS062018-D5-1',3,'',3,1),(31,'2018-06-12 14:29:41.699984','2','SKS062018-D5-1',3,'',3,1),(32,'2018-06-12 14:29:41.715525','1','SKS062018-D5-1',3,'',3,1),(33,'2018-06-12 22:51:39.975146','8','MBF850407916062700C40006',3,'',2,1),(34,'2018-06-13 16:02:40.500148','10','ds1233544',3,'',2,1),(35,'2018-06-13 16:02:40.531400','9','ds1233544',3,'',2,1),(36,'2018-06-13 18:43:15.648878','20','123123123',3,'',2,1),(37,'2018-06-13 18:43:15.695756','19','asdasdasdddddddddd',3,'',2,1),(38,'2018-06-13 18:43:15.758246','18','asdasdasdddddddddd',3,'',2,1),(39,'2018-06-13 19:47:02.714575','16','MGF8406160130C4008',2,'[{\"changed\": {\"fields\": [\"sksid\"]}}]',2,1),(40,'2018-06-13 19:59:51.168350','21','TTTTTTTTTT',3,'',2,1),(41,'2018-06-13 20:02:45.340370','22','ttttttttttttt',3,'',2,1),(42,'2018-06-13 20:04:53.418607','23','ttttttttt',3,'',2,1),(43,'2018-06-13 21:47:56.189412','16','MGF8406160130C4008',2,'[{\"changed\": {\"fields\": [\"tech_add1\", \"tech_city\", \"tech_state\", \"tech_zip\", \"techNote\"]}}]',2,1),(44,'2018-06-13 22:00:55.049376','6','SKS062018-D1-2',2,'[{\"changed\": {\"fields\": [\"sn\"]}}]',3,1),(45,'2018-06-13 22:01:38.783828','7','SKS062018-D1-5',2,'[{\"changed\": {\"fields\": [\"sn\"]}}]',3,1),(46,'2018-06-13 22:02:04.565059','8','SKS062018-D1-7',2,'[{\"changed\": {\"fields\": [\"sn\"]}}]',3,1),(47,'2018-06-13 22:02:32.205744','9','SKS062018-D1-6',2,'[{\"changed\": {\"fields\": [\"sn\"]}}]',3,1),(48,'2018-06-13 22:03:32.190169','10','SKS062018-D1-8',2,'[{\"changed\": {\"fields\": [\"sn\"]}}]',3,1),(49,'2018-06-13 22:44:55.173874','11','SKS062018-D1-6',2,'[]',3,1),(50,'2018-06-13 22:45:04.017596','11','SKS062018-D1-6',3,'',3,1),(51,'2018-06-13 22:46:43.314616','12','SKS062018-D1-2',3,'',3,1),(52,'2018-06-14 16:27:32.981245','17','MPF820204216122800C40016',2,'[{\"changed\": {\"fields\": [\"tech_add1\", \"tech_city\", \"tech_state\", \"tech_zip\", \"tsq\", \"techNote\"]}}]',2,1),(53,'2018-06-14 19:14:41.036486','24','MBF800107716112900C40009',2,'[{\"changed\": {\"fields\": [\"location_add1\", \"tsq\", \"techNote\"]}}]',2,1),(54,'2018-06-14 19:38:39.819001','26','123123',3,'',2,1),(55,'2018-06-14 19:38:39.850252','25','123456',3,'',2,1),(56,'2018-06-14 19:56:40.632405','28','TEST',3,'',2,1),(57,'2018-06-14 19:58:54.366894','4','Christina',2,'[{\"changed\": {\"fields\": [\"group\"]}}]',4,1),(58,'2018-06-14 20:04:27.179615','29','10bbbwqd',3,'',2,1),(59,'2018-06-14 20:13:10.851988','30','0000',3,'',2,1),(60,'2018-06-14 20:38:14.056372','31','000000',3,'',2,1),(61,'2018-06-14 20:49:01.322511','32','55555555',3,'',2,1),(62,'2018-06-14 20:50:57.111204','33','111111',3,'',2,1),(63,'2018-06-14 20:55:39.830854','34','22222',3,'',2,1),(64,'2018-06-15 17:01:55.918571','16','Account',1,'[{\"added\": {}}]',4,1),(65,'2018-06-15 20:48:23.222068','36','ATO-2B24GAUS200317021500c40010',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"sksid\", \"followup_customer\"]}}]',2,1),(66,'2018-06-15 20:52:32.612880','37','MSF830204217011300C40007',2,'[{\"changed\": {\"fields\": [\"tsq\", \"sksid\"]}}]',2,1),(67,'2018-06-15 20:52:40.659704','38','MGF8452AUS100317031500C40001',2,'[{\"changed\": {\"fields\": [\"tsq\", \"sksid\"]}}]',2,1),(68,'2018-06-15 20:52:47.597212','39','MBF800307917020600C40001',2,'[{\"changed\": {\"fields\": [\"sksid\"]}}]',2,1),(69,'2018-06-15 20:53:57.862896','35','MBF8006150207C4015',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"sksid\", \"followup_customer\"]}}]',2,1),(70,'2018-06-15 21:02:55.017040','40','mbg1111111',2,'[{\"changed\": {\"fields\": [\"warranty\"]}}]',2,1),(71,'2018-06-15 21:04:20.454424','40','mbg1111111',2,'[{\"changed\": {\"fields\": [\"location_state\", \"warranty\"]}}]',2,1),(72,'2018-06-15 21:08:58.272573','40','mbg1111111',2,'[{\"changed\": {\"fields\": [\"warranty\"]}}]',2,1),(73,'2018-06-15 21:09:44.028441','40','mbg1111111',3,'',2,1),(74,'2018-06-15 21:12:05.841064','39','MBF800307917020600C40001',2,'[{\"changed\": {\"fields\": [\"sksid\"]}}]',2,1),(75,'2018-06-15 21:23:06.607183','16','SKS062018-D1-10',3,'',3,1),(76,'2018-06-15 21:23:12.622814','15','SKS062018-D1-10',3,'',3,1),(77,'2018-06-15 22:05:03.781224','23','SKS062018-D1-13',3,'',3,1),(78,'2018-06-15 22:05:09.406231','22','SKS062018-D1-16',3,'',3,1),(79,'2018-06-15 22:46:01.752032','12','MCF8707151008C4006',2,'[{\"changed\": {\"fields\": [\"tsq\", \"finished\"]}}]',2,1),(80,'2018-06-15 23:35:03.801377','39','MBF800307917020600C40001',2,'[{\"changed\": {\"fields\": [\"tech_add1\", \"tech_city\", \"tech_state\", \"tech_zip\", \"techName\", \"techPhone\", \"techEmail\", \"scheDate\", \"techNote\"]}}]',2,1),(81,'2018-06-15 23:36:35.973324','39','MBF800307917020600C40001',2,'[{\"changed\": {\"fields\": [\"scheDate\"]}}]',2,1),(82,'2018-06-15 23:45:33.051905','7','Katrina',2,'[{\"changed\": {\"fields\": [\"group\"]}}]',4,1),(83,'2018-06-17 18:50:29.309180','5','10BAUS100318032200C40018',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1),(84,'2018-06-17 18:50:48.340413','7','mbf850407916062700c40006',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"pre_diagnosis_flag\", \"followup_customer\", \"followup_tech\"]}}]',2,1),(85,'2018-06-17 18:50:57.512296','11','MBF8508AUS100318011100C40005',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"pre_diagnosis_flag\", \"followup_customer\", \"followup_tech\"]}}]',2,1),(86,'2018-06-17 18:51:20.652937','13','MSF830604216050400C40008',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"pre_diagnosis_flag\", \"followup_tech\"]}}]',2,1),(87,'2018-06-17 18:51:29.324819','14','MSF8301AUS100317031900C45251',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"pre_diagnosis_flag\", \"followup_customer\"]}}]',2,1),(88,'2018-06-17 18:51:41.043580','15','MPF8201150209C4003',2,'[{\"changed\": {\"fields\": [\"techNote\", \"finished\", \"followup_customer\"]}}]',2,1),(89,'2018-06-17 18:51:56.121720','38','MGF8452AUS100317031500C40001',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1),(90,'2018-06-17 18:52:15.543611','36','ATO-2B24GAUS200317021500c40010',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1),(91,'2018-06-17 18:52:24.809273','35','MBF8006150207C4015',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1),(92,'2018-06-17 18:52:31.152997','27','MSF830204216072100C40017',2,'[{\"changed\": {\"fields\": [\"tsq\", \"techNote\", \"pre_diagnosis_flag\"]}}]',2,1),(93,'2018-06-17 18:52:37.934252','24','MBF800107716112900C40009',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1),(94,'2018-06-17 18:52:45.621759','17','MPF820204216122800C40016',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\", \"followup_customer\", \"followup_tech\"]}}]',2,1),(95,'2018-06-17 18:53:37.934302','16','MGF8406160130C4008',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\", \"followup_customer\", \"followup_tech\"]}}]',2,1),(96,'2018-06-17 18:55:41.715695','39','MBF800307917020600C40001',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis\", \"pre_diagnosis_flag\"]}}]',2,1),(97,'2018-06-17 18:58:22.012723','15','MPF8201150209C4003',2,'[{\"changed\": {\"fields\": [\"pre_diagnosis_flag\"]}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'auth','user'),(9,'contenttypes','contenttype'),(3,'request','partrequest'),(1,'request','partsinv'),(11,'request','timerecord'),(2,'request','unitbasicinfo'),(10,'sessions','session'),(4,'users','users'),(12,'warranty','invoice');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'request','0001_initial','2018-06-11 15:57:14.470503'),(2,'request','0002_unitbasicinfo','2018-06-11 15:57:14.595502'),(3,'request','0003_auto_20180524_1713','2018-06-11 15:57:14.861161'),(4,'request','0004_auto_20180524_1718','2018-06-11 15:57:15.298662'),(5,'request','0005_auto_20180526_1658','2018-06-11 15:57:15.361162'),(6,'request','0006_auto_20180526_1709','2018-06-11 15:57:15.454916'),(7,'request','0007_unitbasicinfo_warrantynote','2018-06-11 15:57:15.595538'),(8,'request','0008_auto_20180526_2254','2018-06-11 15:57:16.220537'),(9,'request','0009_auto_20180527_2255','2018-06-11 15:57:16.298667'),(10,'request','0010_unitbasicinfo_finished','2018-06-11 15:57:16.392416'),(11,'request','0011_auto_20180528_0022','2018-06-11 15:57:16.470537'),(12,'request','0012_auto_20180529_1449','2018-06-11 15:57:16.595599'),(13,'request','0013_auto_20180530_1008','2018-06-11 15:57:16.673665'),(14,'request','0014_partrequest_code','2018-06-11 15:57:16.783039'),(15,'users','0001_initial','2018-06-11 15:57:23.564260'),(16,'users','0002_auto_20180527_0158','2018-06-11 15:57:23.673644'),(17,'users','0003_users_group','2018-06-11 15:57:23.751794'),(18,'users','0004_auto_20180527_2255','2018-06-11 15:57:24.017417'),(19,'users','0005_auto_20180528_0259','2018-06-11 15:57:24.033046'),(20,'users','0006_auto_20180529_1445','2018-06-11 15:57:24.048671'),(21,'users','0007_auto_20180611_1051','2018-06-11 15:57:24.064294'),(22,'contenttypes','0001_initial','2018-06-11 15:58:00.376792'),(23,'auth','0001_initial','2018-06-11 15:58:01.267509'),(24,'admin','0001_initial','2018-06-11 15:58:01.517451'),(25,'admin','0002_logentry_remove_auto_add','2018-06-11 15:58:01.548705'),(26,'contenttypes','0002_remove_content_type_name','2018-06-11 15:58:01.736168'),(27,'auth','0002_alter_permission_name_max_length','2018-06-11 15:58:01.845608'),(28,'auth','0003_alter_user_email_max_length','2018-06-11 15:58:01.939330'),(29,'auth','0004_alter_user_username_opts','2018-06-11 15:58:01.970543'),(30,'auth','0005_alter_user_last_login_null','2018-06-11 15:58:02.095574'),(31,'auth','0006_require_contenttypes_0002','2018-06-11 15:58:02.111201'),(32,'auth','0007_alter_validators_add_error_messages','2018-06-11 15:58:02.142454'),(33,'auth','0008_alter_user_username_max_length','2018-06-11 15:58:02.298668'),(34,'auth','0009_alter_user_last_name_max_length','2018-06-11 15:58:02.408081'),(35,'sessions','0001_initial','2018-06-11 15:58:02.486202'),(36,'request','0015_auto_20180610_0234','2018-06-11 16:14:24.497039'),(37,'request','0016_timerecord','2018-06-11 16:14:24.559574'),(38,'users','0007_auto_20180610_0234','2018-06-11 16:14:24.575197'),(39,'users','0008_merge_20180611_1114','2018-06-11 16:14:24.590827'),(40,'request','0017_auto_20180611_1316','2018-06-11 18:20:20.953513'),(41,'request','0018_auto_20180611_1443','2018-06-11 19:43:31.424573'),(42,'request','0019_auto_20180611_1530','2018-06-11 20:30:45.598843'),(43,'request','0020_auto_20180611_1547','2018-06-11 20:47:18.990248'),(44,'request','0021_partrequest_pre_diagnosis','2018-06-11 21:05:24.866188'),(45,'request','0022_auto_20180612_1627','2018-06-12 21:27:20.080307'),(46,'request','0023_auto_20180613_1558','2018-06-13 20:59:13.780708'),(47,'request','0024_partrequest_sn','2018-06-13 21:54:41.658497'),(48,'request','0025_auto_20180614_1425','2018-06-14 19:26:10.068316'),(49,'warranty','0001_initial','2018-06-15 15:32:34.914071'),(50,'request','0026_auto_20180617_1117','2018-06-17 18:45:39.027651'),(51,'users','0009_auto_20180617_1345','2018-06-17 18:45:39.058963'),(52,'warranty','0002_auto_20180617_1345','2018-06-17 18:45:39.121469');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('155nkbmylato5e7vlefi3alc6apt6gcc','NjcyNjE1MDhkMTZjMGMxYTgyZWM1ODc4MzFjMjE2ZTRiOGU3ZGE2Nzp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxMyIsInVzZXJfbmFtZSI6IldhcnJhbnR5IENoZWNrIiwidXNlcl9ncm91cCI6IndhcnJhbnR5In0=','2018-06-29 21:01:17.671323'),('492ljye0zykqh546afsg5a7lf526bzd2','ZWI2YzdlNWM3MDNlMWNhNGJiNDQ2MzNhMTBjYzJhZTJhZGY4OTVhOTp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxIiwidXNlcl9uYW1lIjoiSmFuZSIsInVzZXJfZ3JvdXAiOiJkaXNwYXRjaGVyIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJiNjNkNzA1ODVmZDg5ZGUyYjM4MGU1OTRmZThmNDZjZTY2YWQ0ZDYifQ==','2018-07-01 18:50:18.512316'),('cjztu1li0g3bmcrjjz8da3r9or3cwgyi','MjQzNzJmNzMzZGU0MDczODQ5NGFjZDU3YzQ5ZWQwYzcxMzdhZWU0Yjp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxMiIsInVzZXJfbmFtZSI6IkphY2tpZSIsInVzZXJfZ3JvdXAiOiJvcGVyYXRvciJ9','2018-06-29 16:58:59.246546'),('e9mkzdy74vlp8l04drfadj4wkhj9nzsi','NmZiZWQ1MzQ4YmZlYWJlNTU5NjExMmU2OTY2N2RkZTAyZDNmNmM2ODp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIyIiwidXNlcl9uYW1lIjoiQ2hsb2UiLCJ1c2VyX2dyb3VwIjoiZGlzcGF0Y2hlciJ9','2018-06-29 19:18:58.623747'),('fcvrtcx2k4w93o7gmxzoseb9bsc48g3q','OGI1OTFkNzA5MjgwODk5NTMxMTUzYWEwNDM3ZmI0MjlkNTM0NTUwNjp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiI3IiwidXNlcl9uYW1lIjoiQ2hyaXN0aW5hIiwidXNlcl9ncm91cCI6Im9wZXJhdG9yIn0=','2018-06-28 19:59:48.757564'),('hstgz48a0yy2ecn7vmqsh2f5z6s6fmii','ZjA2N2FlNjNkNjkzYjNlNTRkNDlkYmQxMTZlNTg2Mzc5YWU4NjhkMzp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxNSIsInVzZXJfbmFtZSI6IlBhcnRzIiwidXNlcl9ncm91cCI6InBhcnRzIn0=','2018-06-29 16:23:11.057252'),('htze31qvcqzg9snkaejifd2ry3ydktci','MjU3Yzg5MzBjYjRhNTI4OTk0OWY4NTUwMmMxZjJhNWE0Yjc5YzIxYjp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIwIiwidXNlcl9uYW1lIjoiQURNSU4iLCJ1c2VyX2dyb3VwIjoiYWRtaW4ifQ==','2018-06-29 21:18:57.888282'),('kjk5ytlj6fvjs4mixkrx5j4oej78dncj','NTQ3YTcxMDQxYzEzZTViMTk0ODdkYmQ0MzU1NGZhZGUyOGU1ZWUzMTp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxMCIsInVzZXJfbmFtZSI6IkJyYW5kb24iLCJ1c2VyX2dyb3VwIjoib3BlcmF0b3IiLCJ1bml0X3R5cGUiOiJDT0xEIiwidW5pdF9zbiI6Ik1HRjg0NTJBVVMxMDAzMTcwMzE1MDBDNDAwMDEifQ==','2018-06-29 20:29:52.096095'),('o54aj408ct0w2dcbzvq0b1hfqyoelolg','YWFhMzY3MmNlMDI3YmUyNGExOWRlZmQxZTkxZWM1Mjc4M2RiZTFlODp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiI0IiwidXNlcl9uYW1lIjoiWWVzaSIsInVzZXJfZ3JvdXAiOiJkaXNwYXRjaGVyIn0=','2018-06-29 19:41:29.234313'),('r88i9cd0pz5mzl3yflo03wb87on5jirn','NWYwZjUyZDNlNGQxNTlmMGM0N2NiMjdmMTk4YzA4Y2NlYjQ2NTVhMjp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxMSIsInVzZXJfbmFtZSI6IkFubmEiLCJ1c2VyX2dyb3VwIjoib3BlcmF0b3IiLCJ1bml0X3R5cGUiOiJDT0xEIiwidW5pdF9zbiI6Ik1CRjgwMDMwNzkxNzAyMDYwMEM0MDAwMSJ9','2018-06-29 20:38:06.190289'),('sp02dbkmuv9b56jr3t95q70ierjyr67d','NjcyNjE1MDhkMTZjMGMxYTgyZWM1ODc4MzFjMjE2ZTRiOGU3ZGE2Nzp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxMyIsInVzZXJfbmFtZSI6IldhcnJhbnR5IENoZWNrIiwidXNlcl9ncm91cCI6IndhcnJhbnR5In0=','2018-06-29 19:35:59.234032'),('vq8s7nv7ltm8em9jcdqxq7s1cl4rqfoq','OTE0MWNhN2M3N2M5ZTlkMmFhOTg4MzFkYmQ0ZTRkN2M4ODUyOTI0YTp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxIiwidXNlcl9uYW1lIjoiSmFuZSIsInVzZXJfZ3JvdXAiOiJkaXNwYXRjaGVyIn0=','2018-06-29 20:39:20.455908'),('ybo7jmqo03lpld5c2z068hhdvrl798z7','Y2EwMTA5ODA2ZjRjZjAyYWU0OWI5Zjc0NDJhZWU0NGIyMDM0YWY1NTp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiIxNiIsInVzZXJfbmFtZSI6IkFjY291bnQiLCJ1c2VyX2dyb3VwIjoiYWNjb3VudCJ9','2018-06-29 17:18:38.122535'),('z0vudgk3jhxg3lh6wcba7fx4566yq2fh','YzI2ZTAwNWY2MzEwMGQ3ZDAzYjE2N2E2MTkxYTQ2ZDAxNzRlZjNjZDp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2NvZGUiOiI4IiwidXNlcl9uYW1lIjoiQW1hbmRhIiwidXNlcl9ncm91cCI6ImFkbWluZHAifQ==','2018-06-29 18:06:14.593618');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_partrequest`
--

DROP TABLE IF EXISTS `request_partrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `request_partrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sksid` varchar(30) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `number` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `shipping_method` varchar(20) NOT NULL,
  `qty` int(11) NOT NULL,
  `request_time` date NOT NULL,
  `tracking` varchar(50) DEFAULT NULL,
  `approved` tinyint(1) NOT NULL,
  `location_add1` varchar(200) NOT NULL,
  `location_add2` varchar(200) DEFAULT NULL,
  `location_city` varchar(20) NOT NULL,
  `location_state` varchar(30) NOT NULL,
  `location_zip` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `pre_diagnosis` longtext,
  `sn` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_partrequest`
--

LOCK TABLES `request_partrequest` WRITE;
/*!40000 ALTER TABLE `request_partrequest` DISABLE KEYS */;
INSERT INTO `request_partrequest` VALUES (6,'SKS062018-D1-2','Mike Smith','WO302162','digital temp controller','',1,'2018-06-13','1Z140R560199416783',0,'8235 North Orange Blossom Trail',NULL,'Orlando','FL',32810,1,'Dispatch Micheal&Charlie to check if the compressor working.','MBF8508AUS100318011100C40005'),(7,'SKS062018-D1-5','Tye','W0401100','Handle, Lid','',1,'2018-06-13','1Z140R560199153610',0,'159 N Hiatus Rd, Pembroke Pines, FL 33026',NULL,'Pembroke Pines','FL',33026,1,'Send new lid handle to the customer.\r\n W0401100	Handle, Lid','MSF8301AUS100317031900C45251'),(8,'SKS062018-D1-7','Mike Ritchie Refrigeration','W0302164','temp controller','',1,'2018-06-13','1Z140R560198437002',0,'4714 Woodward Place',NULL,'Sarasota','FL',34233,1,'Dispatch a tech to replace the temp controller. Explain to the customer that when cleaning they can not get water on the controller. This is the 2nd time this year to replace the controller. We will not replace a 3rd time','MPF8201150209C4003'),(9,'SKS062018-D1-6','Mike Ritchie Refrigeration','W0302018','temp controller','',1,'2018-06-13','1Z140R560198437002',0,'4714 Woodward Place',NULL,'Sarasota','FL',34233,1,'Have customer make sure there is no clog in the drain. If tech(since he will be there for the other 2 units) finds a clog customer needs to be charged for the service call. If not clog seal around the drain pan with silicon and replace the probe.','MPF820204216122800C40016'),(10,'SKS062018-D1-8','Mike Ritchie Refrigeration','W0302018','control board','',1,'2018-06-13','1Z140R560198437002',0,'4714 Woodward Place',NULL,'Sarasota','FL',34233,1,'Dispatch a tech to replace the temp controller. Explain to the customer that when cleaning they can not get water on the controller. This is the 2nd time this year to replace the controller.','MGF8406160130C4008'),(13,'SKS062018-D1-6','Mike Ritchie Refrigeration','W0302018','temp controller','',1,'2018-06-14','1Z140R560199644698',0,'4714 Woodward Place','','Sarasota','FL',34233,1,'Have customer make sure there is no clog in the drain. If tech(since he will be there for the other 2 units) finds a clog customer needs to be charged for the service call. If not clog seal around the drain pan with silicon and replace the probe.','MPF820204216122800C40016'),(14,'SKS062018-D1-6','Mike Ritchie Refrigeration','W0308001','switch, power','',1,'2018-06-14','1Z140R560199644698',0,'4714 Woodward Place','','Sarasota','FL',34233,1,'Have customer make sure there is no clog in the drain. If tech(since he will be there for the other 2 units) finds a clog customer needs to be charged for the service call. If not clog seal around the drain pan with silicon and replace the probe.',NULL),(17,'SKS062018-D1-11','SSI Services','301030039','Safety Valve','',1,'2018-06-15','1Z140R560192017913',0,'333 N. Falkenburg Rd. Unit B-223','','Tampa','FL',33619,1,'Dispatch a tech to replace the safety valve(301030039 ) and the Thermocouple(301030040).','ATO-2B24GAUS200317021500c40010'),(18,'SKS062018-D1-11','SSI Services','301030040','Thermocouple','',1,'2018-06-15','1Z140R560192017913',0,'333 N. Falkenburg Rd. Unit B-223','','Tampa','FL',33619,1,'Dispatch a tech to replace the safety valve(301030039 ) and the Thermocouple(301030040).',NULL),(19,'SKS062018-D1-10','Robert Hill ( Inhouse Tech)','W0204003','filter drier','',1,'2018-06-15','1Z140R560292414527',0,'7575-A Ponce De Leon Circle','','Doraville','GA',30340,1,'Dispatch in house tech to check the unit for a leak near the evap coil','MSF830204216072100C40017'),(20,'SKS062018-D1-10','Robert Hill ( Inhouse Tech)','W0201612','compressor','',1,'2018-06-15','1Z140R560292414527',0,'7575-A Ponce De Leon Circle','','Doraville','GA',30340,1,'Dispatch in house tech to check the unit for a leak near the evap coil',NULL),(21,'SKS062018-D1-16','Sisk Restaurant Repair Services','W0302162','CONTROLLER','',1,'2018-06-15','1Z140R564495122286',0,'2791 Eagle Lake Drive','','Clermont','FL',34711,1,'','MBF800307917020600C40001');
/*!40000 ALTER TABLE `request_partrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_timerecord`
--

DROP TABLE IF EXISTS `request_timerecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `request_timerecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref` int(11) NOT NULL,
  `call` datetime(6) NOT NULL,
  `pre_diagnosis` datetime(6) NOT NULL,
  `tech` datetime(6) NOT NULL,
  `part` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_timerecord`
--

LOCK TABLES `request_timerecord` WRITE;
/*!40000 ALTER TABLE `request_timerecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `request_timerecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_unitbasicinfo`
--

DROP TABLE IF EXISTS `request_unitbasicinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `request_unitbasicinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `businessName` varchar(100) NOT NULL,
  `contactName` varchar(50) NOT NULL,
  `serialNumber` varchar(50) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `location_add1` varchar(200) NOT NULL,
  `location_add2` varchar(200) DEFAULT NULL,
  `location_city` varchar(20) NOT NULL,
  `location_state` varchar(30) NOT NULL,
  `location_zip` int(11) NOT NULL,
  `issue` longtext NOT NULL,
  `warranty` tinyint(1) DEFAULT NULL,
  `tsq` longtext,
  `techName` varchar(50) DEFAULT NULL,
  `techPhone` varchar(15) DEFAULT NULL,
  `techEmail` varchar(254) DEFAULT NULL,
  `scheDate` date DEFAULT NULL,
  `callTime` datetime(6) NOT NULL,
  `warrantyNote` longtext,
  `areaCode` int(11) NOT NULL,
  `receiver` varchar(50) DEFAULT NULL,
  `techNote` longtext,
  `sksid` varchar(20) DEFAULT NULL,
  `finished` tinyint(1) NOT NULL,
  `pre_diagnosis` longtext,
  `followup_customer` longtext,
  `followup_customer_time` datetime(6),
  `followup_tech` longtext,
  `followup_tech_time` datetime(6),
  `tech_add1` varchar(200) DEFAULT NULL,
  `tech_add2` varchar(200) DEFAULT NULL,
  `tech_city` varchar(20) DEFAULT NULL,
  `tech_state` varchar(30) DEFAULT NULL,
  `tech_zip` int(11) DEFAULT NULL,
  `business_hour` varchar(80) DEFAULT NULL,
  `pre_diagnosis_flag` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_unitbasicinfo`
--

LOCK TABLES `request_unitbasicinfo` WRITE;
/*!40000 ALTER TABLE `request_unitbasicinfo` DISABLE KEYS */;
INSERT INTO `request_unitbasicinfo` VALUES (5,'Atlanta Breakfast Club','cyrus','10BAUS100318032200C40018','(305) 753-3688',NULL,'249 Ivan Allen Jr Blvd NW,',NULL,'Atlanta','GA',30313,'(Unit installed 2 hrs ago) Customer lights the left side pilot, every thing is working fine but every time he lights the right side there is a big flame on the oven..Since this is a brand new Unit that’s having a problem , customer asking if He can replace the unit.',1,'The pilot can be lighted on: YES<br>The pilot can stay on: YES<br>The burner can be turned on: YES',NULL,NULL,NULL,NULL,'2018-06-12 16:06:18.079813','6/11/2018, ATLANTA, 3017141\r\nBilled To: Mr. V\'s Restaurant Equipment\r\nDealer picked up the unit',4,'Anna','','SKS062018-D4-1',0,'Customer or dealer drilled screws on the bottom to install casters. and made holes on the gas pipe.\r\nSo it is not  under warranty.   The person who drilled holes should take the responsibility.','','2018-06-17 18:50:29.293553','','2018-06-17 18:50:29.293553',NULL,NULL,NULL,NULL,NULL,NULL,1),(6,'Dairy Queen','Hany','MSF8302AUS100317021500C40021','(727) 946-3558','','3101 66th St N','','St. Petersburg','FL',33710,'TEMP TOO HOT',0,'Filter Clean: Within 1 month\nDisplay Temperature: 58\nReal Temperature: 59\nController: Digital\nSnowflake Icon: ON\nFan Icon: ON\nIce on Evap: NO\nCond Fan Running: YES\nEvap Fan Running: YES\nCompressor running: NO\nDoor issue: NONE\n',NULL,NULL,NULL,NULL,'2018-06-12 20:50:38.297238','MSF8302AUS100317021500C40021 \r\nOUT OF WARRANTY\r\nOriginal serial: MSF8302150712C4007',4,'Anna',NULL,'SKS062018-D4-2',0,NULL,NULL,'2018-06-12 21:18:04.720487',NULL,'2018-06-12 21:18:04.720487',NULL,NULL,NULL,NULL,NULL,NULL,0),(7,'Sammy\'s Italian Restaurant','Taulie','mbf850407916062700c40006','(352) 361-5534',NULL,'9668 N, US-301',NULL,'Wildwood','FL',34785,'running in a hot temp.. It wont run below 30.. Little bit icey at the back where the drain pipes drip water..',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 33\r\nReal Temperature: UNKNOWN\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','United Refrigeration, Inc. (URI)','(352) 629-1187','ahodges@unitedrefrigerationocala.com','2018-06-14','2018-06-12 21:16:58.204810','11/21/2017, ORLANDO, ATFL8807\r\nBilled to: Bay Area Wholesale\r\nDealer picked up the unit',1,'Anna','Scheduled Time: 2018-06-12 10:00:00-05:00\r\nName: United Refrigeration, Inc. (URI)\r\nPhone (352) 629-1187\r\nEmail kroberts@unitedrefrigerationocala.com\r\nNote 3730 NE 44th Street, Ocala FL 34479  -25.5 MILES / 44 MINUTES\r\n\r\nScheduled Time: 2018-06-14 17:00:00-05:00\r\nName: United Refrigeration, Inc. (URI)\r\nPhone (352) 629-1187\r\nEmail ahodges@unitedrefrigerationocala.com\r\nNote 3730 NE 44th Street, Ocala FL 34479 \r\n\r\n-25.5 MILES / 44 MINUTES  \r\n\r\nOPERATOR PLEASE NOTE: Scheduled service time is approximate  for sometime today or tomorrow.','SKS062018-D1-1',1,'Dispatch a tech to bypass the general relay (see service Bulletin)','2018-06-15 13:02:18.593452\r\ntechnician completed service  request. The unit is up and running for now. Will call back if there are any other issues.','2018-06-17 18:50:48.340413','2018-06-14 11:35:05.356662\r\nTech has been in touch with the customer and has the work order request on the schedule. Tech is trying to get to them today, but he has also arranged a morning appt as a backup.\r\n2018-06-15 10:10:12.319204\r\nAs of 10:00 Am - Tech on site working on preliminary diagnosis.  Will notify and update when complete.','2018-06-17 18:50:48.340413',NULL,NULL,NULL,NULL,NULL,NULL,1),(11,'New York Pizza Baby','Mike','MBF8508AUS100318011100C40005','(407) 876-2459',NULL,'380 Semoran Commerce Pl A104,',NULL,'Apopka','FL',32703,'NEW UNIT- JUST INSTALLED THIS MORNING. TEMPERATURE WON\'T GO DOWN BELOW 90.. TECH/DEALER WANTS TO WORK ON IT ASAP: CHARLIES RESTAURANT EQUIPMENT- 407-521-1861',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 90\r\nReal Temperature: UNKNOWN\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Charlie\'s Restaurant Equipment','(407) 521-1861','mikescw1@gmail.com','2018-06-13','2018-06-13 14:48:11.887053','6/11/2018, ORLANDO, 3017261\r\nBilled To: Charlie\'s Restaurant Equipment\r\nDealer picked up the unit',1,'Anna','Scheduled Time: 2018-06-13 10:49:00-05:00\r\nName: Charlie\'s Restaurant Equipment\r\nPhone (407) 521-1861\r\nEmail mikescw1@gmail.com\r\nNote TECH ADDRESS: 8235 North Orange Blossom Trail, Orlando FL \r\n\r\n3.9 mi. About 8 mins','SKS062018-D1-2',1,'Dispatch Micheal&Charlie to check if the compressor working.','2018-06-15 10:00:22.459349\r\nCorrect telephone number for the restaurant.  # (407) 464-7157.  Confirmed with employee that the service has been completed and the unit is working as it should.','2018-06-17 18:50:57.512296','2018-06-14 11:38:28.966188\r\nTech found the controller to be bad.\r\nTech just received overnighted part and  will install it within the hour.\r\n2018-06-15 09:55:09.318452\r\nTech states: All done.  Working great!','2018-06-17 18:50:57.512296',NULL,NULL,NULL,NULL,NULL,NULL,1),(12,'Safety Harbor Resort','Esti','MCF8707151008C4006','(727) 252-3804',NULL,'105 N Bayshore Dr, Safety Harbor, FL 34695',NULL,'Safety Harbor','FL',34695,'Not cooling. BAD COMPRESSOR TURNS ON AND OFF.',0,'Filter Clean: Within 1 month\r\nDisplay Temperature: 50\r\nReal Temperature: 50\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: NO\r\nDoor issue: NONE',NULL,NULL,NULL,NULL,'2018-06-13 15:59:32.078148','OUT OF WARRANTY\r\n2/5/2016, ORLANDO, ATFL3912\r\nBilled and Shipped To; \r\nNew and NEarly New Rest. Equipment',1,'Brandon','','SKS062018-D1-3',1,'','','2018-06-15 22:46:01.736408','','2018-06-15 22:46:01.736408',NULL,NULL,NULL,NULL,NULL,NULL,0),(13,'POPPY\'S ITALIANO','lOROS','MSF830604216050400C40008','(904) 891-2801',NULL,'832-1 A1A N','SUIT #1','Ponte Vedra Beach','FL',32082,'CUSTOMER CLEANED THE DRAIN PIPES, NOTHING IS CLOGGED, CHECKED THE PAN NOTHING IS WRONG, BUT THERE IS LOT OF WATER INSIDE THE UNIT. EVERY MORNING THE CUSTOMER COMES IN THE UNIT IS FILLED WITH WATER. NO OTHER REFRIGERATION PROBLEM',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 38\r\nReal Temperature: 38\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Cline Commercial Services','(904) 356-7986','clinecommercial@gmail.com','2018-06-14','2018-06-13 16:39:46.377043','6/16/2016, \r\nHOUSTON, \r\nATHS1365\r\nBilled and Shipped To: \r\nG&S Restaurant Equipment',1,'Anna','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: Cline Commercial Services\r\nPhone (904) 356-7986\r\nEmail clinecommercial@gmail.com\r\nNote 923 West Forsyth Street Jacksonville FL 32204\r\n\r\n24.0 mi. About 28 mins\r\n\r\nAPPROXIMATE ETA FOR SOMETIME TOMORROW','SKS062018-D1-4',0,'Dispatch tech to check the unit for a clog in the drain. If found they will need to charge the customer. If there is not clog ask them  to replace the probe and put silicon around the edge of the drain pan.','','2018-06-17 18:51:20.652937','2018-06-14 11:41:40.450743\r\n\'Loris\' at Poppy\'s said he isn\'t going to pay for tech to come to tell him that whatever the problem is won\'t be under warranty. He is going to call B&B and see if they will pay for it if not under warranty,  so no call is scheduled right now til I hear back from him.','2018-06-17 18:51:20.652937',NULL,NULL,NULL,NULL,NULL,NULL,1),(14,'Submarine crab','Tye','MSF8301AUS100317031900C45251','(954) 736-8062','KFCMA2@AOL.COM','159 N Hiatus Rd, Pembroke Pines, FL 33026',NULL,'Pembroke Pines','FL',33026,'lid handle broke. Does not need a tech',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 36\r\nReal Temperature: 36\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: UNKNOWN\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','SUBMARINE CRAB (CUSTOMER)','(954) 736-8062','KFCMA2@AOL.COM','2018-06-14','2018-06-13 17:27:39.566940','MSF8301AUS100317031900C45251\r\n9/28/2017, ORLANDO, ATFL8329\r\nBilled To: Hollywood Rest. Equipment',1,'Brandon','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: SUBMARINE CRAB (CUSTOMER)\r\nPhone (954) 736-8062\r\nEmail KFCMA2@AOL.COM\r\nNote 159 N HIATUS RD, PEMBROKE PINES, FL 33026 PEMBROKE PINES FL 33026\r\n\r\n\r\n\r\nCUSTOMER TO INSTALL LID HANDLE','SKS062018-D1-5',1,'Send new lid handle to the customer.\r\n W0401100	Handle, Lid','2018-06-14 11:46:06.794716\r\nCustomer received and installed the lid handle today. Everything is working just fine.','2018-06-17 18:51:29.324819','','2018-06-17 18:51:29.324819',NULL,NULL,NULL,NULL,NULL,NULL,1),(15,'IL CONTE','maleda / alfredo','MPF8201150209C4003','(856) 283-5522',NULL,'8209 Natures Way','Suite103','Lakewood Ranch','FL',34202,'UNIT IS NOT COOLING.. Prefered Tech: Coast Line Heating and Cooling: 941-388-8060.. TECH IS WAITING FOR OUR WORK ORDER SO THAT THEY CAN GO AND WORK AT THE CUSTOMERS LOCATION',1,'','Mike Ritchie Refrigeration','(941) 926-1739','mike_ritchie@verizon.net','2018-06-14','2018-06-13 17:56:03.240252','MPF8201150209C4003\r\n1/24/2017, ORLANDO, ATFL6311\r\nBilled and Shipped To: \r\nFox Restaurant Equipment',1,'Anna','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: Mike Ritchie Refrigeration\r\nPhone (941) 926-1739\r\nEmail mike_ritchie@verizon.net\r\nNote 4714 Woodward Place, Sarasota, FL 34233\r\n\r\n\r\nAPPROXIMATE ETA  IS UNKNOWN. TECH TO CALL AND UPDATE.','SKS062018-D1-7',0,'Dispatch a tech to replace the temp controller. Explain to the customer that when cleaning they can not get water on the controller. This is the 2nd time this year to replace the controller. We will not replace a 3rd time','2018-06-15 13:10:29.015768\r\nCalled customer to follow up on service request. left a VM message to return my call.','2018-06-17 18:58:21.997043','','2018-06-17 18:58:21.997043',NULL,NULL,NULL,NULL,NULL,NULL,1),(16,'IL Conte Ristorante & Pizzeria','alfredo','MGF8406160130C4008','(856) 283-5522',NULL,'8209 Natures Way','Suite103','Lakewood Ranch','FL',34202,'it shows 99 and HA on the display- Prefered Tech: Coast Line Heating and Cooling: 941-388-8060',1,'','Mike Ritchie Refrigeration','(941) 926-1739','mike_ritchie@verizon.net','2018-06-14','2018-06-13 18:03:18.459362','MGF8406160130C4008\r\n4/27/2017, ORLANDO, ATFL7122\r\nBilled and Shipped To: \r\nFox Restaurant Equipment',1,'Anna','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: Mike Ritchie Refrigeration\r\nPhone (941) 926-1739\r\nEmail mike_ritchie@verizon.net\r\nNote 4714 Woodward Place, Sarasota, FL 34233\r\n\r\n10.5 mi. About 18 mins\r\n\r\nAPPROXIMATE ETA IS UNKNOWN. TECH TO CALL AND UPDATE.','SKS062018-D1-8',0,'Dispatch a tech to replace the temp controller. Explain to the customer that when cleaning they can not get water on the controller. This is the 2nd time this year to replace the controller.','2018-06-15 13:10:13.578270\r\nCalled customer to follow up on service request. left a VM message to return my call.','2018-06-17 18:53:37.918711','2018-06-14 12:05:00.358153\r\nTech scheduled service for today and is on site. Will have to return tomorrow to follow up and install parts on another unit for the same customer.','2018-06-17 18:53:37.918711','4714 Woodward Place',NULL,'Sarasota','FL',34233,NULL,1),(17,'IL Conte Ristorante & Pizzeria','alfredo','MPF820204216122800C40016','(856) 283-5522',NULL,'8209 Natures Way','Suite103','Lakewood Ranch','FL',34202,'LEAKING A LOT OF WATER. CUSTOMER IS OKAY EVEN IF THEY GET CHARGED IF ITS A MAINTENANCE ISSUE, Preferred Tech: Coast Line Heating and Cooling: 941-388-8060',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 39\r\nReal Temperature: NONE\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Mike Ritchie Refrigeration','(941) 926-1739','mike_ritchie@verizon.net','2018-06-15','2018-06-13 18:07:34.943953','MPF820204216122800C40016\r\n3/31/2017, ORLANDO, ATFL6865\r\nBilled and Shipped To:\r\nFox Restaurant Equipment\r\n\r\nLASKS0917-S9-126\r\nMike Ritchie Refrigeration \r\nPOWER SWITCH IS BROKEN AND UNIT DOES NOT TURN ON\r\nREPLACED AND INSTALLED NEW CONTROLLER AND POWER SWITCH\r\n$135.00',1,'Anna','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: Mike Ritchie Refrigeration\r\nPhone (941) 926-1739\r\nEmail mike_ritchie@verizon.net\r\nNote 4714 Woodward Place, Sarasota, FL 34233\r\n\r\n\r\n\r\n\r\n\r\nAPPROXIMATE ETA IS UNKNOWN. TECH TO CALL AND UPDATE.\r\n\r\nScheduled Time: 2018-06-15 10:30:00-05:00\r\nName: Mike Ritchie Refrigeration\r\nPhone (941) 926-1739\r\nEmail mike_ritchie@verizon.net\r\nNote Re-sending necessary parts requested by tech','SKS062018-D1-6',0,'Have customer make sure there is no clog in the drain. If tech(since he will be there for the other 2 units) finds a clog customer needs to be charged for the service call. If not clog seal around the drain pan with silicon and replace the probe.','2018-06-15 13:09:10.953216\r\nCalled customer to follow up on service request. left a VM message to return my call.','2018-06-17 18:52:45.621759','2018-06-14 11:55:17.982680\r\nTech scheduled service for today. Requested temp controller and a power switch be overnighted. Tech will go out there again tomorrow when parts are received to install.','2018-06-17 18:52:45.621759','4714 Woodward Place',NULL,'Sarasota','FL',34233,NULL,1),(24,'SHABANG CATERING','jackson','MBF800107716112900C40009','(786) 273-2165',NULL,'3015 NW 79TH ST',NULL,'Miami','FL',33142,'not cooling',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 68\r\nReal Temperature: 68\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Miami Restaurant Repair','(305) 863-6200','mrralbert@aol.com','2018-06-14','2018-06-14 16:36:30.247346','3/22/2017, ORLANDO, ATFL6766\r\nBilled and Shipped To:\r\nS4L Restaurant Equipment',1,'Brandon','Scheduled Time: 2018-06-14 00:00:00-05:00\r\nName: Miami Restaurant Repair\r\nPhone: (305) 863-6200\r\nEmail: mrralbert@aol.com\r\nNote: 5.9 mi. About 19 mins\r\n\r\nWill schedule service for tomorrow but does not have a specific ETA.','SKS062018-D1-9',0,'Dispatch a tech to check if all parts running like customer said, if so, please check leaking and compressor.','','2018-06-17 18:52:37.934252','','2018-06-17 18:52:37.934252','7150 NW Terrace',NULL,'Miami','FL',33166,NULL,1),(27,'JONHHY\'S PIZZA','DOUG','MSF830204216072100C40017','(770) 568-5856',NULL,'1050 RICHARD D SAILORS PKWY',NULL,'POWDER SPRINGS','GA',30127,'UNIT WAS SERVICED VIA SKS0518-D1-184 and now no longer keeping temperature.',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 64\r\nReal Temperature: NA\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Robert Hill ( Inhouse Tech)','(909) 541-1437','Tech1.GA@SmartKitchenService.com','2018-06-15','2018-06-14 19:40:01.772192','10/19/2016, ATLANTA< ATGA2914\r\nBilled and Shipped To: \r\nRestaurnat Solutions',1,'Jackie','Scheduled Time: 2018-06-15 00:00:00-05:00\r\nName: Robert Hill ( Inhouse Tech)\r\nPhone: (909) 541-1437\r\nEmail: Tech1.GA@SmartKitchenService.com\r\nNote: Scheduled ETA for sometime today. No specific time has been given.','SKS062018-D1-10',0,'Dispatch in house tech to check the unit for a leak near the evap coil','','2018-06-17 18:52:31.152997','','2018-06-17 18:52:31.152997','7575-A Ponce De Leon Circle',NULL,'Doraville','GA',30340,'11AM-9PM',1),(35,'Cactus','Ruben','MBF8006150207C4015','(239) 370-6498',NULL,'30 Hancock Bridge Pkwy',NULL,'Cape Coral','FL',33991,'Unit is not cooling properly is at 85 deg',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 80\r\nReal Temperature: NONE\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: YES\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE','Commercial Appliance Repair','(239) 275-9939','dispatchercar@jc.comcastbiz.net','2018-06-18','2018-06-15 16:54:51.105714','4/28/2016, ORLANDO, ATFL4565\r\nBilled and Shipped To: \r\nAmeChef',1,'Jackie','Scheduled Time: 2018-06-18 00:00:00-05:00\r\nName: Commercial Appliance Repair\r\nPhone: (239) 275-9939\r\nEmail: dispatchercar@jc.comcastbiz.net\r\nNote: Approximate ETA for Monday 6/18/2018.  No specific time was given \r\n12.7 mi. About 22 mins','SKS062018-D1-15',0,'Dispatch a tech to  check the compressor is running.(bring 3 in 1 capacitor to check the compressor) If the compressor is running  Check the unit for a Freon leak.','2018-06-15 12:58:53.234001\r\nCustomer was notified of ETA for Monday 6/18/2018. No specific time was available.','2018-06-17 18:52:24.793617','','2018-06-17 18:52:24.793617','10880 Metro Parkway #A',NULL,'Ft. Myers','FL',33966,'11AM-9PM',1),(36,'THE SURLY MERMAID (FOOD TRUCK)','MR. THOMAS','ATO-2B24GAUS200317021500c40010','(813) 335-6885',NULL,'1311 Oak Pond St',NULL,'Ruskin','FL',33570,'THE PILOT FOR THE OVEN DOES NOT LITE AT ALL…Since it is a food truck customer is willing to  take the whole truck to the  service guy\'s/ technicians location --',1,'The pilot can be lighted on: NO\r\nThe pilot can stay on: NO\r\nThe burner can be turned on: UNKNOWN','SSI Services','(800) 263-2206','INEEDHELP@SSISERVICES.COM​','2018-06-18','2018-06-15 17:42:33.826861','5/23/2017, ATLANTA, ATGA4422\r\nBilled and Shipped To; \r\nFlorida Restaurant Equipment',1,'Anna','Scheduled Time: 2018-06-18 00:00:00-05:00\r\nName: Whaley Foodservice - Tampa\r\nPhone: (888) 337-8889\r\nEmail: SERVICE-ORLANDO@WHALEYFOODSERVICE.COM\r\nNote: APPROXIMATE ETA SCHEDULED FOR 06/18/2018 -6/19/2018  WHEN PARTS ARE RECEIVED. \r\n\r\n21.0 mi. About 24 mins\r\n\r\nScheduled Time: 2018-06-18 00:00:00-05:00\r\nName: SSI Services\r\nPhone: (800) 263-2206\r\nEmail: INEEDHELP@SSISERVICES.COM​\r\nNote: Joey will schedule service once parts are received. No Specific ETA at this time. \r\n\r\n19.9 mi. About 24 mins','SKS062018-D1-11',0,'Dispatch a tech to replace the safety valve(301030039 ) and the Thermocouple(301030040).','2018-06-15 15:30:29.393025\r\nCustomer is aware parts will need to be sent to fix the unit. ETA for service  will be scheduled when parts are received.  Mon or Tues 06/18-06/19/2018','2018-06-17 18:52:15.543611','','2018-06-17 18:52:15.543611','333 N. Falkenburg Rd. Unit B-223',NULL,'Tampa','FL',33619,'food truck- call for appointment',1),(37,'Sports Grill South Miami','Spike','MSF830204217011300C40007','(305) 582-9141',NULL,'1559 Sunset Dr,',NULL,'Miami','FL',33143,'Temperature is reading 38 not the actual temp',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 38\r\nReal Temperature: 50\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: NO\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE',NULL,NULL,NULL,NULL,'2018-06-15 17:59:16.577710','11/2/2017, ORLANDO, ATFL8660\r\nBilled and Shipped To; \r\nMiami Restaurant Repair',1,'Christina','','SKS062018-D1-12',0,'','','2018-06-15 20:52:32.597266','','2018-06-15 20:52:32.597266',NULL,NULL,NULL,NULL,NULL,'11am-12am',0),(38,'Bare Roots','Olivia','MGF8452AUS100317031500C40001','(407) 506-6905','Olivia@barerootspharmacy.com','105 12h st',NULL,'Columbus','GA',31901,'tracks on both of the drawers are broken',1,'Filter Clean: Within 1 month\r\nDisplay Temperature: 0\r\nReal Temperature: 0\r\nController: Digital\r\nSnowflake Icon: ON\r\nFan Icon: ON\r\nIce on Evap: YES\r\nCond Fan Running: YES\r\nEvap Fan Running: YES\r\nCompressor running: YES\r\nDoor issue: NONE',NULL,NULL,NULL,NULL,'2018-06-15 20:29:51.955431','MGF8452AUS100317031500C40001\r\n5/10/2017, ATLANTA, ATGA4311\r\nBilled and Shipped To:\r\nMobile Fixture and Equipment Company',1,'Brandon','','SKS062018-D1-13',0,'Dispatch a tech to replace broken slides only, Send 1 right, 1 left, and 2 rollers  Ask them to tighten up call the rollers and slide, use lock tight on all screw.','','2018-06-17 18:51:56.121720','','2018-06-17 18:51:56.121720',NULL,NULL,NULL,NULL,NULL,'11am-10pm',1),(39,'Diginos Italian Restaurant','Stephen pegues','MBF800307917020600C40001','(407) 595-4482',NULL,'1271 Semoran Blvd Ste 151',NULL,'Casselberry','FL',32707,'PER CHARLIE:\r\n\r\n Part request:\r\nController W0302162 x1.\r\nShip to customer and deliver on Saturday.',1,'',NULL,NULL,NULL,'2018-06-16','2018-06-15 20:38:06.080907','11/10/2017, ORLANDO, ATFL8730\r\nBilled To; Restaurant Furnishing and Supplies\r\nDealer picked up the unit',1,'Anna','Scheduled Time: 2018-06-16 00:00:00-05:00\r\nName: Sisk Restaurant Repair Services\r\nPhone: (407) 616-3542\r\nEmail: Siskrepair@gmail.com\r\nNote: Ship to customer and deliver on Saturday.\r\n\r\nController shows P3 P4.--- need new controller','SKS062018-D1-16',0,'PER CHARLIE:\r\n\r\n Part request:\r\nController W0302162 x1.\r\nShip to customer and deliver on Saturday.','','2018-06-17 18:55:41.700034','','2018-06-17 18:55:41.700034',NULL,NULL,NULL,NULL,NULL,'10:30 am- 11PM',1);
/*!40000 ALTER TABLE `request_unitbasicinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_users`
--

DROP TABLE IF EXISTS `users_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `code` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL,
  `group` varchar(15) NOT NULL,
  `current_month` int(11) NOT NULL,
  `current_tasks` int(11) NOT NULL,
  `total_tasks` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_users`
--

LOCK TABLES `users_users` WRITE;
/*!40000 ALTER TABLE `users_users` DISABLE KEYS */;
INSERT INTO `users_users` VALUES (1,'Jane','1','654321','dispatcher',1,0,0),(2,'Yesi','4','123456','dispatcher',1,0,0),(3,'Chloe','2','123456','dispatcher',1,0,0),(4,'Christina','7','123456','operator',1,0,0),(5,'Daniela','3','123456','dispatcher',1,0,0),(6,'Samantha','5','123456','dispatcher',1,0,0),(7,'Katrina','6','123456','dispatcher',1,0,0),(8,'Amanda','8','123456','admindp',1,0,0),(9,'Randi','9','123456','operator',1,0,0),(10,'Brandon','10','123456','operator',1,0,0),(11,'Anna','11','123456','operator',1,0,0),(12,'Jackie','12','123456','operator',1,0,0),(13,'Warranty Check','13','123456','warranty',1,0,0),(14,'ADMIN','0','Admin','admin',1,0,0),(15,'Parts','15','123456','parts',1,0,0),(16,'Account','16','Account123','account',1,0,0);
/*!40000 ALTER TABLE `users_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warranty_invoice`
--

DROP TABLE IF EXISTS `warranty_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `warranty_invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice` varchar(20) DEFAULT NULL,
  `travel_t` decimal(5,2) DEFAULT NULL,
  `labor_t` decimal(5,2) DEFAULT NULL,
  `travel_c` decimal(7,2) DEFAULT NULL,
  `labor_c` decimal(7,2) DEFAULT NULL,
  `material_c` decimal(7,2) DEFAULT NULL,
  `total_c` decimal(7,2) DEFAULT NULL,
  `sksid` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty_invoice`
--

LOCK TABLES `warranty_invoice` WRITE;
/*!40000 ALTER TABLE `warranty_invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `warranty_invoice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-17 14:03:00
