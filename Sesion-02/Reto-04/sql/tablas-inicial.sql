-- MySQL dump 10.17  Distrib 10.3.15-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: BeduTravels
-- ------------------------------------------------------
-- Server version	10.3.15-MariaDB-1:10.3.15+maria~bionic

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
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `apellidos` varchar(60) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,'Hugo','Mac Rico',10,'M'),
    (2,'Paco','Mac Rico',15,'M'),
    (3,'Daisy','Mac Rico',18,'H'),
    (4,'Luis','Mac Rico',19,'M'),
    (5,'Goku','Saiyajin',47,'M'),
    (6,'Vegeta','Saiyajin',50,'M'),
    (7,'Chabelo',NULL,100,'M');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Lugar`
--

DROP TABLE IF EXISTS `Lugar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Lugar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) NOT NULL,
  `ubicacion` varchar(256) DEFAULT NULL,
  `comentarios` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Lugar`
--

LOCK TABLES `Lugar` WRITE;
/*!40000 ALTER TABLE `Lugar` DISABLE KEYS */;
INSERT INTO `Lugar` VALUES (1,'CDMX','https://www.google.com/maps/place/Mexico+City,+CDMX/@19.3910036,-99.2840426,11z/data=!3m1!4b1!4m5!3m4!1s0x85ce0026db097507:0x54061076265ee841!8m2!3d19.4326077!4d-99.133208',NULL),
    (2,'Puebla','https://www.google.com/maps/place/Puebla/@19.0446137,-98.2593042,13z/data=!4m5!3m4!1s0x85cfc0dd57a33fb5:0x89eef8cae756b4fb!8m2!3d19.0420124!4d-98.1995607',NULL),
    (3,'Guadalajara','https://www.google.com/maps/place/Guadalajara,+Jalisco/@20.6739383,-103.4056254,12z/data=!3m1!4b1!4m5!3m4!1s0x8428b18cb52fd39b:0xd63d9302bf865750!8m2!3d20.6596988!4d-103.3496092',NULL),
    (4,'Michoacán','https://www.google.com/maps/place/Michoac%C3%A1n/@19.153927,-103.0219365,8z/data=!3m1!4b1!4m5!3m4!1s0x842a5f3e1eb35cb7:0x3bc7650cf34be0d4!8m2!3d19.5665192!4d-101.7068294',NULL),
    (5,'Veracruz','https://www.google.com/maps/place/Veracruz/@19.7955207,-98.3891361,7z/data=!3m1!4b1!4m5!3m4!1s0x85c355d0af54526d:0x2d777f0a6710b9b3!8m2!3d19.2601605!4d-96.5783387',NULL),
    (6,'Yucatán','https://www.google.com/maps/place/Yucatan/@21.0728661,-92.1740721,7z/data=!3m1!4b1!4m5!3m4!1s0x8f540ff8aad604ed:0xcccc217531083d0a!8m2!3d20.7098786!4d-89.0943377',NULL),
    (7,'Oaxaca','https://www.google.com/maps/place/Oaxaca/@17.156289,-98.4545407,7z/data=!3m1!4b1!4m5!3m4!1s0x85c0d84f3a0e5c51:0x44c60c433dd90bc9!8m2!3d17.0542297!4d-96.7132304',NULL);
/*!40000 ALTER TABLE `Lugar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Viaje`
--

DROP TABLE IF EXISTS `Viaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Viaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idOrigen` int(11) NOT NULL,
  `idDestino` int(11) NOT NULL,
  `costo` decimal(11,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Viaje`
--

LOCK TABLES `Viaje` WRITE;
/*!40000 ALTER TABLE `Viaje` DISABLE KEYS */;
INSERT INTO `Viaje` VALUES (1,1,3,NULL),
    (2,1,2,400.00),
    (3,2,4,600.00),
    (4,2,7,800.00),
    (5,3,5,NULL),
    (6,4,2,550.00),
    (7,3,1,680.00);
/*!40000 ALTER TABLE `Viaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reserva`
--

DROP TABLE IF EXISTS `Reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reserva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idUsuario` int(11) NOT NULL,
  `idViaje` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `fechaSalida` date DEFAULT NULL,
  `fechaRegreso` date DEFAULT NULL,
  `numPers` int(11) DEFAULT NULL,
  `costo` decimal(11,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reserva`
--

LOCK TABLES `Reserva` WRITE;
/*!40000 ALTER TABLE `Reserva` DISABLE KEYS */;
INSERT INTO `Reserva` VALUES (1,3,1,'2019-06-05','2019-06-05','2019-06-12',1,NULL),
    (2,5,4,'2019-06-09','2019-06-10',NULL,4,NULL),
    (3,3,4,'2019-06-09','2019-06-10',NULL,1,NULL),
    (4,7,3,'2019-06-10','2019-06-15',NULL,2,NULL);
/*!40000 ALTER TABLE `Reserva` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-05 22:09:10
