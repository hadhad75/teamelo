CREATE DATABASE  IF NOT EXISTS `baseCE` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `baseCE`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: exemple.cuxvnracjvrw.us-east-2.rds.amazonaws.com    Database: baseCE
-- ------------------------------------------------------
-- Server version	5.5.5-10.2.21-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activite`
--

DROP TABLE IF EXISTS `activite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activite`
--

LOCK TABLES `activite` WRITE;
/*!40000 ALTER TABLE `activite` DISABLE KEYS */;
INSERT INTO `activite` VALUES (1,'Zumba'),(2,'Course'),(3,'Golf'),(4,'Velo'),(5,'Yoga'),(6,'Salle de sport'),(7,'Sauna'),(8,'Massage');
/*!40000 ALTER TABLE `activite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Daniel Abnett','dabnett@compagnie.fr','dabnett'),(2,'Nina Locke','nlocke@compagnie.fr','nlocke'),(4,'Pierre Pasquier','ppasquier@compagnie.fr','ppasquier'),(5,'François Odin','fodin@compagnie.fr','fodin'),(6,'Vincent Paris','vparis@compagnie.fr','vparis'),(7,'François Enaud','fenaud@compagnie.fr','fenaud'),(8,'Jean Carteron','jcarteron@compagnie.fr','jcarteron'),(9,'François Mazon','fmazon@compagnie.fr','fmazon'),(10,'Olivier Vallet','ovallet@compagnie.fr','ovallet'),(11,'Laurent Giovachini','lgiovachini@compagnie.fr','lgiovachini'),(12,'John Torrie','jtorrie@compagnie.fr','jtorrie');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_activite`
--

DROP TABLE IF EXISTS `user_activite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_activite` (
  `user_id` int(255) NOT NULL,
  `activite_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`activite_id`),
  KEY `fk_user_has_activite_activite1_idx` (`activite_id`),
  KEY `fk_user_has_activite_user_idx` (`user_id`),
  CONSTRAINT `fk_user_has_activite_activite1` FOREIGN KEY (`activite_id`) REFERENCES `activite` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_activite_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_activite`
--

LOCK TABLES `user_activite` WRITE;
/*!40000 ALTER TABLE `user_activite` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_activite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-02  9:40:39
