-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: ai
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

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
-- Table structure for table `ai`
--

DROP TABLE IF EXISTS `ai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ai` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `link` varchar(45) NOT NULL,
  `price` varchar(255) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ai`
--

LOCK TABLES `ai` WRITE;
/*!40000 ALTER TABLE `ai` DISABLE KEYS */;
INSERT INTO `ai` VALUES (1,'ChatGPT','https://openai.com/chatgpt','Free plan available, offering basic access to ChatGPT. Plus plan at $20/month includes access to GPT-4 and faster response times.',5),(2,'DeepSeek','https://www.deepseek.ai','Pricing not publicly available. Custom plans are offered based on enterprise needs.',3),(3,'Google Bard','https://bard.google.com','Free access with premium features expected to be rolled out in the future.',4),(4,'Claude','https://www.anthropic.com/claude','Free access with limited features. Business plans start at $10/month for extended usage and premium features.',4),(5,'Microsoft Bing Chat','https://www.bing.com/chat','Free access with basic features. Premium features available with Microsoft 365 subscription.',3),(6,'LLaMA (Meta)','https://ai.facebook.com/blog/large-language-m','Pricing not publicly available. Typically available through Meta\'s partnership programs or via custom contracts.',4),(7,'Cohere','https://cohere.ai','Free tier offers limited API usage. Paid plans start at $0.25 per 1,000 tokens for smaller businesses, with custom enterprise plans.',3),(8,'HuggingChat (Hugging Face)','https://huggingface.co/chat/','Free access with limited API usage. Pro plans start at $9/month, offering enhanced performance and additional API calls.',3),(9,'Perplexity AI','https://www.perplexity.ai','Free access with limited functionality. Premium plans available for enhanced usage, pricing on request.',4),(10,'Jasper AI','https://www.jasper.ai','Starts at $39/month for the Starter plan, with Professional plans offering additional features for $99/month.',3),(11,'Character.AI','https://beta.character.ai','Free basic access, with additional features available through paid subscription starting at $5/month.',4),(12,'Replika','https://replika.ai','Free plan with limited interactions. Paid plans range from $7.99/month for the Pro version, to $22.99/month for the Premium version.',2),(13,'OpenAssistant','https://open-assistant.io','Pricing not publicly disclosed, expected to have both free and enterprise-level plans.',3),(14,'Sparrow (DeepMind)','https://www.deepmind.com/research/publication','Free access for research purposes. Custom enterprise plans available upon request.',3),(15,'EleutherAI','https://www.eleuther.ai/','Free open-source access with no paid plans currently.',3),(16,'DoNotPay','https://donotpay.com','Starts at $3/month for the basic plan. Higher-tier plans at $10/month for expanded services like legal consultations.',3),(17,'Kira Systems','https://www.kirasystems.com','Pricing is custom and based on the scale of the client?s business.',3),(18,'Casetext','https://casetext.com','Free trial available, with subscription plans starting at $65/month for individuals, with higher pricing for businesses.',3),(19,'Luminance','https://www.luminance.com/','Custom pricing based on enterprise use cases, typically starting from $10,000/year.',3),(20,'AIVA (AI Music Composition)','https://www.aiva.ai','Free plan with limited tracks. Premium plans start at $11.99/month, with business plans available.',2),(21,'Runway ML','https://runwayml.com','Free plan with limited model usage. Pro plans start at $12/month for extended features.',4),(22,'Sudowrite','https://www.sudowrite.com','Starts at $10/month for the basic plan, with additional features at $25/month for the Pro plan.',3),(23,'Artbreeder','https://www.artbreeder.com','Free access with limited creation. Premium plans start at $8.99/month for extended features and higher resolution images.',2),(24,'Jukebox (OpenAI)','https://openai.com/blog/jukebox/','Free access, with no announced pricing for paid plans as of now.',2),(25,'DeepArt','https://deepart.io','Free plan with low-resolution outputs. Paid plans start at $5 for high-resolution images.',2),(26,'NovelAI','https://novelai.net','Starts at $10/month for the basic plan, with additional features at $25/month for the Pro plan.',4),(27,'Google Cloud AI Predictions','https://cloud.google.com/ai-platform/predicti','Custom pricing based on usage; pay-as-you-go model for API calls.',3),(28,'IBM Watson Predictive Analytics','https://www.ibm.com/products/spss-statistics','Starts at $99/month for the base plan with enterprise pricing available.',3),(29,'RapidMiner','https://rapidminer.com','Free plan with limited functionality. Paid plans start at $2,500/year for additional features and services.',3),(30,'DataRobot','https://www.datarobot.com','Custom pricing based on enterprise use; typically starts from $10,000/year.',3),(31,'H2O.ai','https://www.h2o.ai','Free plan available. Paid plans for enterprise users typically start at $8,000/year.',3),(32,'Alteryx','https://www.alteryx.com','Starts at $5,195/year for the Designer license. Enterprise pricing available for teams.',3),(33,'Netflix Recommendations','https://help.netflix.com/en/node/100639','Free access, integrated directly with Netflix.',4),(34,'Spotify Recommendations','https://developer.spotify.com/documentation/w','Free access for developers with API usage limits.',4),(35,'Amazon Personalize','https://aws.amazon.com/personalize/','Pay-as-you-go pricing with costs based on the volume of usage.',4),(36,'Siri','https://www.apple.com/siri/','Free access with all Apple devices.',3),(37,'Alexa','https://www.amazon.com/alexa','Free for basic use, with premium features available through Amazon services.',3),(38,'Google Assistant','https://assistant.google.com','Free access across all Google devices.',4),(39,'Hound (SoundHound)','https://www.soundhound.com/hound','Free access with basic features. Premium features available for specific partners.',2),(40,'Open Voice OS','https://openvoiceos.com','Free access for basic use; enterprise pricing available.',2),(41,'DALL-E (OpenAI)','https://openai.com/dall-e-2/','Free plan available with limited image generations. Paid plans start at $15/month for more usage.',5),(42,'MidJourney','https://www.midjourney.com','Subscription plans start at $10/month for basic access, with higher-tier plans offering more generations for $30/month.',5),(43,'DeepMind Gemini','https://deepmind.google/','Custom pricing based on usage, typically available through partnerships with large enterprises.',4),(44,'OpenAI GPT-4V','https://openai.com/gpt-4','Access to GPT-4 available at $20/month (via ChatGPT Plus), with API usage priced separately based on usage.',5),(45,'CLIP (OpenAI)','https://openai.com/research/clip','Free access to the research version; API usage is pay-as-you-go.',4),(46,'Imagen','https://research.google/','Pricing not publicly disclosed. Typically available via API with pay-as-you-go model.',4),(47,'OpenAI Five (Dota 2 AI)','https://openai.com/research/openai-five','Free access for research projects. Enterprise plans available for specific use cases.',3),(48,'DeepMind AlphaGo','https://deepmind.com/research/highlighted-res','Free access for research purposes, with enterprise-level partnerships for access.',5),(49,'Nvidia GameGAN','https://www.nvidia.com/en-us/research/ai-play','Custom pricing for enterprise-level access and usage.',3),(50,'AI Dungeon','https://play.aidungeon.io','Free plan with limited story generation. Paid plans start at $10/month for more features.',3),(51,'Modl.ai','https://www.modl.ai','Custom pricing available based on enterprise needs and API usage.',3),(52,'GitHub Copilot','https://github.com/features/copilot','$10/month for individual users; enterprise plans available for teams.',5),(53,'Tabnine','https://www.tabnine.com','Free for basic usage; paid plans start at $12/month for individuals and scale for teams.',3),(54,'CodeT5','https://huggingface.co/Salesforce/codet5','Free access with API limits. Paid plans available for more usage, pricing varies based on usage.',3),(55,'Code Llama','https://www.llama.com/','Free access for basic use, with premium plans available for larger scale usage.',4),(56,'Cogram','https://cogram.com','Pricing not publicly available. Typically based on enterprise needs.',3),(57,'Amazon CodeWhisperer','https://aws.amazon.com/codewhisperer/','Free for basic use; paid plans start at $10/month for additional usage.',3),(58,'Stable Diffusion','https://stablediffusionweb.com','Custom pricing based on scale and usage; typically starts from $100/month for individuals.',5),(59,'Runway Gen-2','https://runwayml.com','Free for basic use. Premium features available at $5/month.',5),(60,'Pika Labs','https://pika.art','Pricing starts at $30/month for individual users, with enterprise pricing available.',4),(61,'Leonardo AI','https://leonardo.ai','Custom pricing based on usage and business needs.',5),(62,'Dream by Wombo (Wombo Dream)','https://www.wombo.art','Free for basic use. Premium features available at $5/month.',4),(63,'Synthesia','https://www.synthesia.io','Pricing starts at $30/month for individual users, with enterprise pricing available.',4),(64,'DeepBrain AI','https://www.deepbrain.io','Custom pricing based on usage and enterprise needs.',3),(65,'Boston Dynamics','https://www.bostondynamics.com','Custom enterprise pricing based on contract details.',5),(66,'Tesla Autopilot','https://www.tesla.com/autopilot','Available as part of Tesla\'s Full Self-Driving package, priced at $15,000 for lifetime access or $199/month for subscription.',4),(67,'MuJoCo','https://mujoco.org','Starts at $850/year for individual use, with pricing available for teams and enterprises.',3);
/*!40000 ALTER TABLE `ai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ai_has_description`
--

DROP TABLE IF EXISTS `ai_has_description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ai_has_description` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ai_id` int(11) NOT NULL,
  `description_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_id` (`ai_id`),
  KEY `description_id` (`description_id`),
  CONSTRAINT `ai_has_description_ibfk_1` FOREIGN KEY (`ai_id`) REFERENCES `ai` (`id`),
  CONSTRAINT `ai_has_description_ibfk_2` FOREIGN KEY (`description_id`) REFERENCES `description` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ai_has_description`
--

LOCK TABLES `ai_has_description` WRITE;
/*!40000 ALTER TABLE `ai_has_description` DISABLE KEYS */;
INSERT INTO `ai_has_description` VALUES (1,1,2),(2,1,4),(3,1,5),(4,2,2),(5,2,1),(6,3,4),(7,4,2),(8,4,5),(9,4,7),(10,5,4),(11,6,2),(12,6,1),(13,7,2),(14,7,7),(15,8,2),(16,8,4),(17,9,4),(18,10,6),(19,11,4),(20,11,5),(21,12,4),(22,13,2),(23,13,1),(24,14,1),(25,15,1),(26,16,6),(27,17,6),(28,18,6),(29,19,6),(30,20,4),(31,20,5),(32,21,7),(33,22,6),(34,23,4),(35,24,2),(36,25,4),(37,26,4),(38,27,5),(39,28,2),(40,29,6),(41,30,6),(42,31,2),(43,32,6),(44,33,4),(45,34,4),(46,35,6),(47,36,4),(48,37,4),(49,38,4),(50,39,4),(51,40,7),(52,41,5),(53,42,6),(54,43,1),(55,44,5),(56,45,1),(57,46,7),(58,47,5),(59,48,5),(60,49,5),(61,50,4),(62,51,6),(63,52,5),(64,53,5),(65,54,2),(66,55,2),(67,56,6),(68,57,2),(69,58,7),(70,59,7),(71,60,7),(72,61,6),(73,62,4),(74,63,6),(75,64,6),(76,65,7),(77,66,6),(78,67,1);
/*!40000 ALTER TABLE `ai_has_description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ai_has_pricingmodel`
--

DROP TABLE IF EXISTS `ai_has_pricingmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ai_has_pricingmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ai_id` int(11) NOT NULL,
  `pricingModel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_id` (`ai_id`),
  KEY `pricingModel_id` (`pricingModel_id`),
  CONSTRAINT `ai_has_pricingmodel_ibfk_1` FOREIGN KEY (`ai_id`) REFERENCES `ai` (`id`),
  CONSTRAINT `ai_has_pricingmodel_ibfk_2` FOREIGN KEY (`pricingModel_id`) REFERENCES `pricingmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ai_has_pricingmodel`
--

LOCK TABLES `ai_has_pricingmodel` WRITE;
/*!40000 ALTER TABLE `ai_has_pricingmodel` DISABLE KEYS */;
INSERT INTO `ai_has_pricingmodel` VALUES (1,1,3),(2,1,3),(3,2,1),(4,3,1),(5,4,3),(6,5,1),(7,6,1),(8,7,3),(9,8,1),(10,9,1),(11,10,2),(12,11,1),(13,12,3),(14,13,1),(15,14,1),(16,15,1),(17,16,2),(18,17,2),(19,18,2),(20,19,2),(21,20,3),(22,21,3),(23,22,2),(24,23,1),(25,24,1),(26,25,2),(27,26,2),(28,27,2),(29,28,2),(30,29,2),(31,30,2),(32,31,1),(33,32,2),(34,33,1),(35,34,1),(36,35,2),(37,36,1),(38,37,1),(39,38,1),(40,39,1),(41,40,1),(42,41,3),(43,42,2),(44,43,1),(45,44,2),(46,45,1),(47,46,1),(48,47,1),(49,48,1),(50,49,1),(51,50,1),(52,51,2),(53,52,2),(54,53,3),(55,54,1),(56,55,1),(57,56,2),(58,57,1),(59,58,1),(60,59,3),(61,60,3),(62,61,2),(63,62,1),(64,63,2),(65,64,2),(66,65,1),(67,66,2),(68,67,1);
/*!40000 ALTER TABLE `ai_has_pricingmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ai_has_targetgroup`
--

DROP TABLE IF EXISTS `ai_has_targetgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ai_has_targetgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ai_id` int(11) NOT NULL,
  `targetgroup_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_id` (`ai_id`),
  KEY `targetgroup_id` (`targetgroup_id`),
  CONSTRAINT `ai_has_targetgroup_ibfk_1` FOREIGN KEY (`ai_id`) REFERENCES `ai` (`id`),
  CONSTRAINT `ai_has_targetgroup_ibfk_2` FOREIGN KEY (`targetgroup_id`) REFERENCES `targetgroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ai_has_targetgroup`
--

LOCK TABLES `ai_has_targetgroup` WRITE;
/*!40000 ALTER TABLE `ai_has_targetgroup` DISABLE KEYS */;
INSERT INTO `ai_has_targetgroup` VALUES (1,1,1),(2,1,7),(3,1,2),(4,2,4),(5,2,1),(6,3,7),(7,3,2),(8,4,1),(9,4,7),(10,4,4),(11,5,7),(12,6,4),(13,6,1),(14,7,1),(15,7,3),(16,8,1),(17,8,4),(18,9,7),(19,9,2),(20,10,5),(21,10,3),(22,11,6),(23,11,7),(24,12,7),(25,13,4),(26,13,1),(27,14,4),(28,15,4),(29,15,1),(30,16,7),(31,16,3),(32,17,3),(33,18,3),(34,19,3),(35,20,5),(36,20,6),(37,21,5),(38,21,3),(39,22,5),(40,23,5),(41,23,6),(42,24,4),(43,24,5);
/*!40000 ALTER TABLE `ai_has_targetgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ai_has_type`
--

DROP TABLE IF EXISTS `ai_has_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ai_has_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ai_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_id` (`ai_id`),
  KEY `type_id` (`type_id`),
  CONSTRAINT `ai_has_type_ibfk_1` FOREIGN KEY (`ai_id`) REFERENCES `ai` (`id`),
  CONSTRAINT `ai_has_type_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ai_has_type`
--

LOCK TABLES `ai_has_type` WRITE;
/*!40000 ALTER TABLE `ai_has_type` DISABLE KEYS */;
INSERT INTO `ai_has_type` VALUES (3,1,1),(4,2,1),(5,3,1),(6,4,1),(7,5,1),(8,6,1),(9,7,1),(10,8,1),(11,9,1),(12,10,1),(13,11,1),(14,12,1),(15,13,1),(16,14,1),(17,15,1),(18,16,11),(19,17,11),(20,18,11),(21,19,11),(22,20,10),(23,21,10),(24,22,10),(25,23,10),(26,24,10),(27,25,10),(28,26,10),(29,27,9),(30,28,9),(31,29,9),(32,30,9),(33,31,9),(34,32,9),(35,33,6),(36,34,6),(37,35,6),(38,36,5),(39,37,5),(40,38,5),(41,39,5),(42,40,5),(43,41,2),(44,42,2),(45,43,2),(46,44,2),(47,45,2),(48,46,2),(49,47,7),(50,48,7),(51,49,7),(52,50,7),(53,51,7),(54,52,3),(55,53,3),(56,54,3),(57,55,3),(58,56,3),(59,57,3),(60,58,4),(61,59,4),(62,60,4),(63,61,4),(64,62,4),(65,63,4),(66,64,4),(67,65,5),(68,66,5),(69,67,5);
/*!40000 ALTER TABLE `ai_has_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `description`
--

DROP TABLE IF EXISTS `description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `description` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `description`
--

LOCK TABLES `description` WRITE;
/*!40000 ALTER TABLE `description` DISABLE KEYS */;
INSERT INTO `description` VALUES (1,'Basic'),(3,'Cheap'),(2,'Efficient'),(5,'Fast'),(7,'Innovative'),(6,'Robust'),(4,'User friendly');
/*!40000 ALTER TABLE `description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pricingmodel`
--

DROP TABLE IF EXISTS `pricingmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pricingmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pricingmodel`
--

LOCK TABLES `pricingmodel` WRITE;
/*!40000 ALTER TABLE `pricingmodel` DISABLE KEYS */;
INSERT INTO `pricingmodel` VALUES (1,'free'),(2,'paid'),(3,'paid or free');
/*!40000 ALTER TABLE `pricingmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `targetgroup`
--

DROP TABLE IF EXISTS `targetgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `targetgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `targetgroup`
--

LOCK TABLES `targetgroup` WRITE;
/*!40000 ALTER TABLE `targetgroup` DISABLE KEYS */;
INSERT INTO `targetgroup` VALUES (3,'Commercial'),(7,'Consumer'),(5,'Contenct Creator'),(1,'Developer'),(2,'Educational Institution'),(6,'Gamer & Entertainment'),(4,'Research and Science');
/*!40000 ALTER TABLE `targetgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (3,'Code-Generation'),(10,'Creative Tools'),(7,'Game-AI'),(4,'Image- and Video-Generation'),(5,'Language Assistant'),(11,'Legal Tech'),(2,'Multimodal'),(1,'NLP'),(9,'Predictive Analytics'),(6,'Reccomendation Systems'),(8,'Robotics and Automation');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-10 11:21:48
