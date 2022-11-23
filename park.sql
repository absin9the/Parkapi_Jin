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
-- Table structure for table `parkspot`
--

DROP TABLE IF EXISTS `parkspot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkspot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(100) NOT NULL,
  `parkcode` varchar(100) DEFAULT NULL,
  `vchiclecode` varchar(100) DEFAULT NULL,
  `allspot` int(11) DEFAULT NULL,
  `avaliable` int(11) DEFAULT NULL,
  `areacode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_parkcode` (`parkcode`),
  KEY `idx_vchiclecode` (`vchiclecode`),
  KEY `inx_areacode` (`areacode`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkspot`
--

LOCK TABLES `parkspot` WRITE;
/*!40000 ALTER TABLE `parkspot` DISABLE KEYS */;
INSERT INTO `parkspot` VALUES (1,'newyork1','000001','100001',25,0,'a01'),(2,'newyork1','000002','100002',25,0,'a01'),(3,'newyork1','000003','100003',25,0,'a01'),(4,'newyork1','000004','100004',25,0,'a01'),(5,'newyork1','000005','100005',25,0,'a01'),(6,'newyork1','000006','100006',25,0,'a01'),(7,'newyork1','000007','100007',25,0,'a01'),(8,'newyork1','000008','100008',25,0,'a01'),(9,'newyork1','000009','100009',25,0,'a01'),(10,'newyork1','000010','100010',25,0,'a01'),(11,'newyork1','000011','100011',25,0,'a01'),(12,'newyork1','000012','100012',25,0,'a01'),(13,'newyork1','000013','100013',25,0,'a01'),(14,'newyork1','000014','100014',25,0,'a01'),(15,'newyork1','000015','100015',25,0,'a01'),(16,'newyork1','000016','100016',25,0,'a01'),(17,'newyork1','000017','100017',25,0,'a01'),(18,'newyork1','000018','100018',25,0,'a01'),(19,'newyork1','000019','100019',25,0,'a01'),(20,'newyork1','000020','100020',25,0,'a01'),(21,'newyork1','000021','100021',25,0,'a01'),(22,'newyork1','000022','100022',25,0,'a01'),(23,'newyork1','000023','100023',25,0,'a01'),(24,'newyork1','000024','100024',25,0,'a01'),(25,'newyork1','000025','100025',25,0,'a01'),(26,'boston1','000001',NULL,1,-1,'b01');
/*!40000 ALTER TABLE `parkspot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'laowang','123456','15225525635','admin'),(3,'laowang1','123456','15225525635','admin');
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


