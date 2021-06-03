-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: course_system
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `c`
--

DROP TABLE IF EXISTS `c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `c` (
  `CNO` char(4) NOT NULL,
  `CNAME` char(20) DEFAULT NULL,
  `CREDI` int DEFAULT NULL,
  `CDEPT` char(10) DEFAULT NULL,
  `TNAME` char(8) DEFAULT NULL,
  PRIMARY KEY (`CNO`),
  UNIQUE KEY `CNO` (`CNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `c`
--

LOCK TABLES `c` WRITE;
/*!40000 ALTER TABLE `c` DISABLE KEYS */;
INSERT INTO `c` VALUES ('C1','机器学习',3,'网络空间安全','李晨亮'),('C2','数据库系统',2,'计算机科学','余发江'),('C3','专业英语',2,'网络空间安全','李晨亮'),('C4','操作系统',3,'网络空间安全','严飞'),('C5','法学原理',3,'网络空间安全','丁鹏'),('C6','数据结构',4,'计算机科学','陈刚'),('C7','微观经济学',3,'经济与管理','丁严'),('C8','R语言',3,'经济与管理','文庆森'),('C9','计算机网络',4,'计算机科学','陈刚');
/*!40000 ALTER TABLE `c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s`
--

DROP TABLE IF EXISTS `s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s` (
  `SNO` char(4) NOT NULL,
  `SNAME` char(8) DEFAULT NULL,
  `SEX` char(2) DEFAULT NULL,
  `AGE` char(2) DEFAULT NULL,
  `SDEPT` char(10) DEFAULT NULL,
  `LOGN` char(20) DEFAULT NULL,
  `hash` char(32) DEFAULT NULL,
  PRIMARY KEY (`SNO`),
  UNIQUE KEY `SNO` (`SNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s`
--

LOCK TABLES `s` WRITE;
/*!40000 ALTER TABLE `s` DISABLE KEYS */;
INSERT INTO `s` VALUES ('S1','孔维翰','男','20','网络空间安全','S1','5e5545d38a68148a2d5bd5ec9a89e327'),('S10','宁姚','女','18','网络空间安全','S10','2c62e6068c765179e1aed9bc2bfd4689'),('S11','黄庭','女','20','经济与管理','S11','9cf695ac37ef238e62f6ee874b4b3968'),('S12','陈清都','男','22','网络空间安全','S12','7e941d9a3237b1770effdcb05a0aa2a5'),('S2','姚南华','男','19','经济与管理','S2','213ee683360d88249109c2f92789dbc3'),('S3','姜斛','男','21','计算机科学','S3','8e4947690532bc44a8e41e9fb365b76a'),('S4','陈双','女','20','计算机科学','S4','166a50c910e390d922db4696e4c7747b'),('S5','吴雨晗','女','19','网络空间安全','S5','9fd9280a7aa3578c8e853745a5fcc18a'),('S6','宋珪','女','20','经济与管理','S6','27e062bf3df59edebb5db9f89952c8b3'),('S7','魏羡','男','21','计算机科学','S7','72e8744fc2faa17a83dec9bed06b8b65'),('S8','顾粲','男','19','网络空间安全','S8','8aa7fb36a4efbbf019332b4677b528cf'),('S9','高适','男','20','计算机科学','S9','7c8cd5da17441ff04bf445736964dd16');
/*!40000 ALTER TABLE `s` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sc`
--

DROP TABLE IF EXISTS `sc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sc` (
  `SNO` char(4) NOT NULL,
  `CNO` char(4) NOT NULL,
  `GRADE` int DEFAULT NULL,
  PRIMARY KEY (`SNO`,`CNO`),
  KEY `CNO` (`CNO`),
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`CNO`) REFERENCES `c` (`CNO`),
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`SNO`) REFERENCES `s` (`SNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sc`
--

LOCK TABLES `sc` WRITE;
/*!40000 ALTER TABLE `sc` DISABLE KEYS */;
INSERT INTO `sc` VALUES ('S1','C3',88),('S1','C4',90),('S10','C6',97),('S11','C8',89),('S12','C7',87),('S2','C2',0),('S2','C3',88),('S2','C7',86),('S3','C2',90),('S3','C6',90),('S5','C5',94),('S6','C8',95),('S7','C6',96),('S9','C9',84);
/*!40000 ALTER TABLE `sc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t`
--

DROP TABLE IF EXISTS `t`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t` (
  `TNO` char(4) NOT NULL,
  `TNAME` char(20) DEFAULT NULL,
  `LOGN` char(20) DEFAULT NULL,
  `hash` char(32) DEFAULT NULL,
  PRIMARY KEY (`TNO`),
  UNIQUE KEY `TNO` (`TNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t`
--

LOCK TABLES `t` WRITE;
/*!40000 ALTER TABLE `t` DISABLE KEYS */;
INSERT INTO `t` VALUES ('T1','李晨亮','T1','41c8949aa55b8cb5dbec662f34b62df3'),('T2','余发江','T2','ccffb0bb993eeb79059b31e1611ec353'),('T3','严飞','T3','82470256ea4b80343b27afccbca1015b'),('T4','丁鹏','T4','93dacda950b1dd917079440788af3321'),('T5','陈刚','T5','ea105f0d381e790cdadc6a41eb611c77'),('T6','丁严','T6','ff1643afb67a6edb36ee3f6fea756323'),('T7','文庆森','T7','71e0f8d7d61b45e27b57c62eb8684583');
/*!40000 ALTER TABLE `t` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-02 21:25:09
