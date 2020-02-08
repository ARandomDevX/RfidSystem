-- MySQL dump 10.17  Distrib 10.3.20-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dev
-- ------------------------------------------------------
-- Server version	10.3.20-MariaDB-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `dev`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `dev`;

--
-- Table structure for table `details`
--

DROP TABLE IF EXISTS `details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `details` (
  `id` varchar(50) DEFAULT NULL,
  `email` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  `name` text DEFAULT NULL,
  `lname` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `details`
--

LOCK TABLES `details` WRITE;
/*!40000 ALTER TABLE `details` DISABLE KEYS */;
INSERT INTO `details` VALUES ('0','Admin@management.corp','admin123','admin','administartor'),('2','testadmin@test.com','$2b$12$hFo/Hp4u4NuOWXHlONDAJO.ok6qf5Hq13TtJeLNkaOqD63rt79fHa','testadmin','testadmin'),('3','','$2b$12$hFo/Hp4u4NuOWXHlONDAJOnL1FJUFR0QHQRchqby27GGNGmKAkjTi','',''),('4','resetbot46@gmail.com','$2b$12$hFo/Hp4u4NuOWXHlONDAJOrnDvL784DO8lFpLiczA9BoA1Qj3WFOi','rigbovfdxvv','dfbdfb '),('5','','$2b$12$hFo/Hp4u4NuOWXHlONDAJO/k2DgieCzlNt3DYaCrj9D1jy0WoMz36','rtkfopgbnm,','');
/*!40000 ALTER TABLE `details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `encryption_key`
--

DROP TABLE IF EXISTS `encryption_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `encryption_key` (
  `kev` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `encryption_key`
--

LOCK TABLES `encryption_key` WRITE;
/*!40000 ALTER TABLE `encryption_key` DISABLE KEYS */;
INSERT INTO `encryption_key` VALUES ('CO26StVK7BTDRLvKe2QnrSS_tRaeKWu509AtAG8JyME=');
/*!40000 ALTER TABLE `encryption_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heim`
--

DROP TABLE IF EXISTS `heim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `heim` (
  `Monday` text DEFAULT NULL,
  `Tuesday` text DEFAULT NULL,
  `Wednesday` text DEFAULT NULL,
  `Thursday` text DEFAULT NULL,
  `Friday` text DEFAULT NULL,
  `Saturday` text DEFAULT NULL,
  `Sunday` text DEFAULT NULL,
  `id` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heim`
--

LOCK TABLES `heim` WRITE;
/*!40000 ALTER TABLE `heim` DISABLE KEYS */;
INSERT INTO `heim` VALUES ('16:45','16:30','16:45','Wird Abgeholt','Wird Abgeholt','17:30','16:30','16:30'),('16:30','16:40','16:03','17:10','17:17','12:00','Wird Abgeholt','Kommt nicht');
/*!40000 ALTER TABLE `heim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kids`
--

DROP TABLE IF EXISTS `kids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kids` (
  `name` text DEFAULT NULL,
  `lname` text DEFAULT NULL,
  `id` text DEFAULT NULL,
  `vater` text DEFAULT NULL,
  `mutter` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kids`
--

LOCK TABLES `kids` WRITE;
/*!40000 ALTER TABLE `kids` DISABLE KEYS */;
/*!40000 ALTER TABLE `kids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ort`
--

DROP TABLE IF EXISTS `ort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ort` (
  `id` text DEFAULT NULL,
  `ort` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ort`
--

LOCK TABLES `ort` WRITE;
/*!40000 ALTER TABLE `ort` DISABLE KEYS */;
INSERT INTO `ort` VALUES ('Bob Tester','Hof');
/*!40000 ALTER TABLE `ort` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passwordreset`
--

DROP TABLE IF EXISTS `passwordreset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `passwordreset` (
  `email` text DEFAULT NULL,
  `code` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passwordreset`
--

LOCK TABLES `passwordreset` WRITE;
/*!40000 ALTER TABLE `passwordreset` DISABLE KEYS */;
/*!40000 ALTER TABLE `passwordreset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salt`
--

DROP TABLE IF EXISTS `salt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `salt` (
  `salt` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salt`
--

LOCK TABLES `salt` WRITE;
/*!40000 ALTER TABLE `salt` DISABLE KEYS */;
INSERT INTO `salt` VALUES ('$2b$12$hFo/Hp4u4NuOWXHlONDAJO');
/*!40000 ALTER TABLE `salt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schuler`
--

DROP TABLE IF EXISTS `schuler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schuler` (
  `name` text DEFAULT NULL,
  `lname` text DEFAULT NULL,
  `id` text DEFAULT NULL,
  `n1` text DEFAULT NULL,
  `n2` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schuler`
--

LOCK TABLES `schuler` WRITE;
/*!40000 ALTER TABLE `schuler` DISABLE KEYS */;
INSERT INTO `schuler` VALUES ('Guido','van Rossum','12345','015167834661','015167834661'),('Guido','van Rossum','345','015167834661','015167834661'),('Guido','van Rossum','345345','015167834661','654656554654');
/*!40000 ALTER TABLE `schuler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sonderab`
--

DROP TABLE IF EXISTS `sonderab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sonderab` (
  `id` text DEFAULT NULL,
  `zeit` text DEFAULT NULL,
  `datum` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sonderab`
--

LOCK TABLES `sonderab` WRITE;
/*!40000 ALTER TABLE `sonderab` DISABLE KEYS */;
/*!40000 ALTER TABLE `sonderab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tokens`
--

DROP TABLE IF EXISTS `tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tokens` (
  `id` varchar(50) DEFAULT NULL,
  `token` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tokens`
--

LOCK TABLES `tokens` WRITE;
/*!40000 ALTER TABLE `tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(50) DEFAULT NULL,
  `uname` text DEFAULT NULL,
  `password` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('0','admin','$2b$12$hFo/Hp4u4NuOWXHlONDAJOrnDvL784DO8lFpLiczA9BoA1Qj3WFOi'),('2','testadmin','$2b$12$hFo/Hp4u4NuOWXHlONDAJO.ok6qf5Hq13TtJeLNkaOqD63rt79fHa'),('3','','$2b$12$hFo/Hp4u4NuOWXHlONDAJOnL1FJUFR0QHQRchqby27GGNGmKAkjTi'),('4','Tst3','$2b$12$hFo/Hp4u4NuOWXHlONDAJOrnDvL784DO8lFpLiczA9BoA1Qj3WFOi'),('5','','$2b$12$hFo/Hp4u4NuOWXHlONDAJO/k2DgieCzlNt3DYaCrj9D1jy0WoMz36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-15  9:34:57
