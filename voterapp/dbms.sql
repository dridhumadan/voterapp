-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: dbms
-- ------------------------------------------------------
-- Server version	8.0.15

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
-- Table structure for table `candidate`
--

DROP TABLE IF EXISTS `candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `candidate` (
  `cand_id` char(7) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `party_no` int(2) DEFAULT NULL,
  `const_code` char(4) DEFAULT NULL,
  PRIMARY KEY (`cand_id`),
  KEY `party_no` (`party_no`),
  KEY `const_code` (`const_code`),
  CONSTRAINT `candidate_ibfk_1` FOREIGN KEY (`party_no`) REFERENCES `party` (`party_no`),
  CONSTRAINT `candidate_ibfk_2` FOREIGN KEY (`const_code`) REFERENCES `constituency` (`const_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidate`
--

LOCK TABLES `candidate` WRITE;
/*!40000 ALTER TABLE `candidate` DISABLE KEYS */;
INSERT INTO `candidate` VALUES ('CKA0101','Annasaheb','Jolle',1,'KA01'),('CKA0102','Prakash','Hukkeri',2,'KA01'),('CKA0201','Angadi','Suresh',1,'KA02'),('CKA0202','Virupakshi','Sadhunnavar',2,'KA02'),('CKA0301','Parvtagouda','Gaddigoudar',1,'KA03'),('CKA0302','Veena','Kashappanavar',2,'KA03'),('CKA0401','Ramesh','Jigajinagi',1,'KA04'),('CKA0403','Sunita','Chavan',3,'KA04'),('CKA0501','Umesh','Jadhav',1,'KA05'),('CKA0502','Mallikarjun','Kharge',2,'KA05'),('CKA0601','Raja','Nayak',1,'KA06'),('CKA0602','Naik','BV',2,'KA06'),('CKA0701','Bhagwant','Khuba',1,'KA07'),('CKA0702','Eshwar','Khandre',2,'KA07'),('CKA0801','Karadi','Sanganna',1,'KA08'),('CKA0802','Rajashekar','Hintal',2,'KA08'),('CKA0901','Devendrappa','D',1,'KA09'),('CKA0902','Ugrappa','VS',2,'KA09'),('CKA1001','Shivakumar','Udasi',1,'KA10'),('CKA1002','Patil','DR',2,'KA10'),('CKA1101','Prahlad','Joshi',1,'KA11'),('CKA1102','Vinay','Kulkarni',2,'KA11'),('CKA1201','Anantkumar','Hegde',1,'KA12'),('CKA1203','Anand','Asnotikar',3,'KA12'),('CKA1301','Siddeshwar','GM',1,'KA13'),('CKA1302','Manjappa','HB',2,'KA13'),('CKA1401','Raghavendra','BY',1,'KA14'),('CKA1403','Madhu','Bangarappa',3,'KA14'),('CKA1501','Shobha','Karandlaje',1,'KA15'),('CKA1503','Pramod','Madhwaraj',3,'KA15'),('CKA1601','Manju','A',1,'KA16'),('CKA1603','Prajwal','Revanna',3,'KA16'),('CKA1701','Nalin Kumar','Kateel',1,'KA17'),('CKA1702','Mithun','Rai',2,'KA17'),('CKA1801','Narayana','Swamy',1,'KA18'),('CKA1802','Chandrappa','BN',2,'KA18'),('CKA1901','Basavaraj','GS',1,'KA19'),('CKA1903','Devegowda','HD',3,'KA19'),('CKA2003','Nikhil','Kumaraswamy',3,'KA20'),('CKA2007','Sumalatha','Ambareesh',7,'KA20'),('CKA2101','Pratap','Simha',1,'KA21'),('CKA2102','Vijayashankar','CN',2,'KA21'),('CKA2201','Srinivas','Prasad',1,'KA22'),('CKA2202','Dhurva','Narayana',2,'KA22'),('CKA2301','Ashwath','Narayan',1,'KA23'),('CKA2302','Suresh','DK',2,'KA23'),('CKA2401','Sadananda','Gowda',1,'KA24'),('CKA2402','Krishna Byre','Gowda',2,'KA24'),('CKA2501','Mohan','PC',1,'KA25'),('CKA2502','Rizwan','Arshad',2,'KA25'),('CKA2507','Prakash','Raj',7,'KA25'),('CKA2601','Tejaswi','Surya',1,'KA26'),('CKA2602','Hariprasad','BK',2,'KA26'),('CKA2701','Bacche','Gowda',1,'KA27'),('CKA2702','Veerappa','Moily',2,'KA27'),('CKA2801','Muniswamy','S',1,'KA28'),('CKA2802','Muniyappa','KH',2,'KA28'),('CKAXXNO','NOTA','NOTA',8,'KAXX');
/*!40000 ALTER TABLE `candidate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constituency`
--

DROP TABLE IF EXISTS `constituency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `constituency` (
  `const_code` char(4) NOT NULL,
  `const_name` varchar(30) NOT NULL,
  PRIMARY KEY (`const_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constituency`
--

LOCK TABLES `constituency` WRITE;
/*!40000 ALTER TABLE `constituency` DISABLE KEYS */;
INSERT INTO `constituency` VALUES ('KA01','Chikkodi'),('KA02','Belagavi'),('KA03','Bagalkot'),('KA04','Bijapur'),('KA05','Kalburgi'),('KA06','Raichur'),('KA07','Bidar'),('KA08','Koppal'),('KA09','Bellary'),('KA10','Haveri'),('KA11','Dharwad'),('KA12','Uttara Kannada'),('KA13','Davangere'),('KA14','Shimoga'),('KA15','Udupi'),('KA16','Hassan'),('KA17','Dakshina Kannada'),('KA18','Chitradurga'),('KA19','Tumkur'),('KA20','Mandya'),('KA21','Mysore'),('KA22','Chamarajnagar'),('KA23','Bengaluru Rural'),('KA24','Bengaluru North'),('KA25','Bengaluru Central'),('KA26','Bengaluru South'),('KA27','Chikballapur'),('KA28','Kolar'),('KAXX','NOTA Placeholder');
/*!40000 ALTER TABLE `constituency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `party`
--

DROP TABLE IF EXISTS `party`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `party` (
  `party_no` int(2) NOT NULL,
  `party_name` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `short_name` varchar(10) NOT NULL,
  PRIMARY KEY (`party_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `party`
--

LOCK TABLES `party` WRITE;
/*!40000 ALTER TABLE `party` DISABLE KEYS */;
INSERT INTO `party` VALUES (1,'Bharatiya Janata Party','6-A, Deen Dayal Upadhyaya Marg, New Delhi - 110002','BJP'),(2,'Indian National Congress','24, Akbar Road, New Delhi - 110011','INC'),(3,'Janata Dal (Secular)','5, Safdarjung Lane, New Delhi - 110003','JDS'),(4,'Bahujan Samaj Party','4, Gurudwara Rakabganj Road, New Delhi - 110001','BSP'),(5,'Communist Party of India','Ajoy Bhawan, Kotla Marg, New Delhi - 110002','CPI'),(6,'Aam Aadmi Party','206, Rause Avenue, DDU Marg, New Delhi - 110002','AAP'),(7,'Independent','','IND'),(8,'NOTA','','NOTA');
/*!40000 ALTER TABLE `party` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voter`
--

DROP TABLE IF EXISTS `voter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `voter` (
  `voter_id` char(7) NOT NULL,
  `email_id` varchar(40) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `cand_id` char(7) DEFAULT NULL,
  `const_code` char(4) DEFAULT NULL,
  PRIMARY KEY (`voter_id`),
  UNIQUE KEY `email_id` (`email_id`),
  UNIQUE KEY `email_id_2` (`email_id`),
  UNIQUE KEY `email_id_3` (`email_id`),
  KEY `cand_id` (`cand_id`),
  KEY `const_code` (`const_code`),
  CONSTRAINT `voter_ibfk_1` FOREIGN KEY (`cand_id`) REFERENCES `candidate` (`cand_id`),
  CONSTRAINT `voter_ibfk_2` FOREIGN KEY (`const_code`) REFERENCES `constituency` (`const_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voter`
--

LOCK TABLES `voter` WRITE;
/*!40000 ALTER TABLE `voter` DISABLE KEYS */;
INSERT INTO `voter` VALUES ('KA20001','a@a.com','testing','Sample','User','1990-01-01','Sample Address','CKA2007','KA20'),('KA21001','c@c.com','abcd','Sample','User','1998-01-10','Sample Address','CKA2101','KA21'),('KA23001','dridhumadan@gmail.com','testing','Dridhu','Madan','1997-05-30','#547 6th Cross Nagarbhavi','CKA2301','KA23'),('KA23002','e@e.com','testing','Sample','User','1990-05-30','Sample Address','CKA2302','KA23'),('KA23003','admin@voterapp.com','admin','Admin','User','1997-05-30','Admin','CKA2301','KA23'),('KA23004','f@f.com','abcd','Sample','User','1997-05-30','Sample Address','CKA2302','KA23'),('KA25001','b@b.com','testing','Sample','User','1991-01-01','Sample','CKA2501','KA25');
/*!40000 ALTER TABLE `voter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-13 20:45:15
