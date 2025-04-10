# Tabellen erstellen

## Haupttabellen

```sql
create table ai(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,name varchar(45) NOT NULL UNIQUE, link varchar(45) NOT NULL, price varchar(255) NOT NULL, rating INT NOT NULL);
```

```sql
create table description (id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(45) NOT NULL UNIQUE);
```

```sql
create table description (id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(45) NOT NULL UNIQUE);
```


```sql
create table type (id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(45) NOT NULL UNIQUE);
```


```sql
create table targetGroup(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(45) NOT NULL UNIQUE);
```

```sql
create table pricingModel(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(45) NOT NULL UNIQUE);
```

## Hilfstables

```sql
create table ai_has_description(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, ai_id INT NOT NULL, description_id INT NOT NULL, FOREIGN KEY (ai_id) references ai(id), FOREIGN KEY(description_id) references description(id));
```

```sql
create table ai_has_type(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, ai_id INT NOT NULL, type_id INT NOT NULL, FOREIGN KEY (ai_id) references ai(id), FOREIGN KEY(type_id) references type(id));
```

```sql
create table ai_has_targetgroup(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, ai_id INT NOT NULL, targetgroup_id INT NOT NULL, FOREIGN KEY (ai_id) references ai(id), FOREIGN KEY(targetgroup_id) references targetgroup(id));
```

```sql
create table ai_has_pricingModel(id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT, ai_id INT NOT NULL, pricingModel_id INT NOT NULL, FOREIGN KEY (ai_id) references ai(id), FOREIGN KEY(pricingModel_id) references pricingModel(id));
```

## Eigenschaften einfügen

Typ
```sql
INSERT INTO type (name) VALUES ('NLP');
INSERT INTO type (name) VALUES ('Multimodal');
INSERT INTO type (name) VALUES ('Code-Generation');
INSERT INTO type (name) VALUES ('Image- and Video-Generation');
INSERT INTO type (name) VALUES ('Language Assistant');
INSERT INTO type (name) VALUES ('Reccomendation Systems');
INSERT INTO type (name) VALUES ('Game-AI');
INSERT INTO type (name) VALUES ('Robotics and Automation');
INSERT INTO type (name) VALUES ('Predictive Analytics');
INSERT INTO type (name) VALUES ('Creative Tools');
INSERT INTO type (name) VALUES ('Legal Tech');
```

Zielgruppe
```sql
INSERT INTO targetgroup (name) VALUES ('Developer');
INSERT INTO targetgroup (name) VALUES ('Educational Institution');
INSERT INTO targetgroup (name) VALUES ('Commercial');
INSERT INTO targetgroup (name) VALUES ('Research and Science');
INSERT INTO targetgroup (name) VALUES ('Contenct Creator');
INSERT INTO targetgroup (name) VALUES ('Gamer & Entertainment');
INSERT INTO targetgroup (name) VALUES ('Consumer');
```

Beschreibung
```sql
INSERT INTO description (name) VALUES ('Basic');
INSERT INTO description (name) VALUES ('Efficient');
INSERT INTO description (name) VALUES ('Cheap');
INSERT INTO description (name) VALUES ('User friendly');
INSERT INTO description (name) VALUES ('Fast');
INSERT INTO description (name) VALUES ('Robust');
INSERT INTO description (name) VALUES ('Innovative');
```


ai
```sql
INSERT INTO ai (name, link, price, rating) VALUES ('ChatGPT', 'https://chatgpt.com/', 'free or 20Eur/Month for premium version', 4);
```




%%

---

Excel to SQL

https://thdoan.github.io/mr-data-converter/

**Code zum Inserts generieren**
https://www.online-python.com/
```py
statements = []

for i in range(16, 20):
    statements.append(f"INSERT INTO ai_has_type(ai_id, type_id) VALUES({i}, 2);")

for i in range(len(statements)):    
    print(statements[i])
```

%%

# Tabellen befüllen
## Type
#### 1 - NLP
```sql
INSERT INTO ai
  (name,link)
VALUES
  ('ChatGPT','https://openai.com/chatgpt'),
  ('DeepSeek','https://www.deepseek.ai'),
  ('Google Bard','https://bard.google.com'),
  ('Claude','https://www.anthropic.com/claude'),
  ('Microsoft Bing Chat','https://www.bing.com/chat'),
  ('LLaMA (Meta)','https://ai.facebook.com/blog/large-language-model-llama-meta-ai/'),
  ('Cohere','https://cohere.ai'),
  ('HuggingChat (Hugging Face)','https://huggingface.co/chat/'),
  ('Perplexity AI','https://www.perplexity.ai'),
  ('Jasper AI','https://www.jasper.ai'),
  ('Character.AI','https://beta.character.ai'),
  ('Replika','https://replika.ai'),
  ('OpenAssistant','https://open-assistant.io'),
  ('Sparrow (DeepMind)','https://www.deepmind.com/research/publications/sparrow-dialogue-agent'),
  ('EleutherAI','https://www.eleuther.ai/');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(1, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(2, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(3, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(4, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(5, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(6, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(7, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(8, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(9, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(10, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(11, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(12, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(13, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(14, 1);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(15, 1);
```


### 11 - Legal Tech

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('DoNotPay','https://donotpay.com'),
  ('Kira Systems','https://www.kirasystems.com'),
  ('Casetext','https://casetext.com'),
  ('Luminance','https://www.luminance.com/');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(16, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(17, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(18, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(19, 2);
```

### 10 - Creative Tools

```sql
INSERT INTO ai
  (Name,Link)
VALUES
  ('AIVA (AI Music Composition)','https://www.aiva.ai'),
  ('Runway ML','https://runwayml.com'),
  ('Sudowrite','https://www.sudowrite.com'),
  ('Artbreeder','https://www.artbreeder.com'),
  ('Jukebox (OpenAI)','https://openai.com/blog/jukebox/'),
  ('DeepArt','https://deepart.io'),
  ('NovelAI','https://novelai.net');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(20, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(21, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(22, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(23, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(24, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(25, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(26, 3);
```

### 9 - Predictive Analytics

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('Google Cloud AI Predictions','https://cloud.google.com/ai-platform/prediction'),
  ('IBM Watson Predictive Analytics','https://www.ibm.com/products/spss-statistics'),
  ('RapidMiner','https://rapidminer.com'),
  ('DataRobot','https://www.datarobot.com'),
  ('H2O.ai','https://www.h2o.ai'),
  ('Alteryx','https://www.alteryx.com');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(27, 9);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(28, 9);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(29, 9);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(30, 9);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(31, 9);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(32, 9);
```

### 6 - Recommendation Systems

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('Netflix Recommendations','https://help.netflix.com/en/node/100639'),
  ('Spotify Recommendations','https://developer.spotify.com/documentation/web-api/reference/get-recommendations'),
  ('Amazon Personalize','https://aws.amazon.com/personalize/');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(33, 6);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(34, 6);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(35, 6);
```

### 5 - Language Assistant

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('Siri','https://www.apple.com/siri/'),
  ('Alexa','https://www.amazon.com/alexa'),
  ('Google Assistant','https://assistant.google.com'),
  ('Hound (SoundHound)','https://www.soundhound.com/hound'),
  ('Open Voice OS','https://openvoiceos.com');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(36, 5);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(37, 5);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(38, 5);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(39, 5);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(40, 5);
```

### 2 - Multimodal

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('DALL-E (OpenAI)','https://openai.com/dall-e-2/'),
  ('MidJourney','https://www.midjourney.com'),
  ('DeepMind Gemini','https://deepmind.google/'),
  ('OpenAI GPT-4V','https://openai.com/gpt-4'),
  ('CLIP (OpenAI)','https://openai.com/research/clip'),
  ('Imagen','https://research.google/');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(41, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(42, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(43, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(44, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(45, 2);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(46, 2);
```

### 7 - Game-AI

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('OpenAI Five (Dota 2 AI)','https://openai.com/research/openai-five'),
  ('DeepMind AlphaGo','https://deepmind.com/research/highlighted-research/alphago'),
  ('Nvidia GameGAN','https://www.nvidia.com/en-us/research/ai-playground/'),
  ('AI Dungeon','https://play.aidungeon.io'),
  ('Modl.ai','https://www.modl.ai');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(47, 7);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(48, 7);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(49, 7);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(50, 7);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(51, 7);
```

### 3 - Code-Generation

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('GitHub Copilot','https://github.com/features/copilot'),
  ('Tabnine','https://www.tabnine.com'),
  ('CodeT5','https://huggingface.co/Salesforce/codet5'),
  ('Code Llama','https://www.llama.com/'),
  ('Cogram','https://cogram.com'),
  ('Amazon CodeWhisperer','https://aws.amazon.com/codewhisperer/');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(52, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(53, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(54, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(55, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(56, 3);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(57, 3);
```

### 4 - Image- and Video-Generation

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('Stable Diffusion','https://stablediffusionweb.com'),
  ('Runway Gen-2','https://runwayml.com'),
  ('Pika Labs','https://pika.art'),
  ('Leonardo AI','https://leonardo.ai'),
  ('Dream by Wombo (Wombo Dream)','https://www.wombo.art'),
  ('Synthesia','https://www.synthesia.io'),
  ('DeepBrain AI','https://www.deepbrain.io');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(58, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(59, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(60, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(61, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(62, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(63, 4);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(64, 4);
```

### 8 - Robotics and Automation

```sql
INSERT INTO ai
  (name,link)
VALUES
  ('Boston Dynamics','https://www.bostondynamics.com'),
  ('Tesla Autopilot','https://www.tesla.com/autopilot'),
  ('MuJoCo','https://mujoco.org');
```

```sql
INSERT INTO ai_has_type(ai_id, type_id) VALUES(65, 8);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(66, 8);
INSERT INTO ai_has_type(ai_id, type_id) VALUES(67, 8);
```




## pricing model

```sql
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(1, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(2, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(3, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(4, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(5, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(6, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(7, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(8, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(9, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(10, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(11, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(12, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(13, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(14, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(15, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(16, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(17, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(18, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(19, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(20, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(21, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(22, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(23, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(24, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(25, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(26, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(27, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(28, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(29, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(30, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(31, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(32, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(33, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(34, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(35, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(36, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(37, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(38, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(39, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(40, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(41, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(42, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(43, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(44, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(45, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(46, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(47, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(48, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(49, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(50, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(51, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(52, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(53, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(54, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(55, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(56, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(57, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(58, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(59, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(60, 3);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(61, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(62, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(63, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(64, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(65, 1);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(66, 2);
INSERT INTO ai_has_pricingmodel(ai_id, pricingModel_id) VALUES(67, 1);
```

## targetgroup
https://chatgpt.com/canvas/shared/67ee51bc94e8819191672fdd52049aec

```sql
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (1, 1);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (1, 7);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (1, 2);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (2, 4);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (2, 1);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (3, 7);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (3, 2);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (4, 1);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (4, 7);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (4, 4);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (5, 7);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (6, 4);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (6, 1);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (7, 1);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (7, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (8, 1);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (8, 4);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (9, 7);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (9, 2);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (10, 5);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (10, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (11, 6);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (11, 7);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (12, 7);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (13, 4);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (13, 1);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (14, 4);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (15, 4);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (15, 1);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (16, 7);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (16, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (17, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (18, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (19, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (20, 5);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (20, 6);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (21, 5);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (21, 3);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (22, 5);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (23, 5);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (23, 6);

INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (24, 4);
INSERT INTO ai_has_targetgroup(ai_id, targetgroup_id) VALUES (24, 5);
```

## description

```sql
INSERT INTO ai_has_description(ai_id, description_id) VALUES(1, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(1, 4);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(1, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(2, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(2, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(3, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(4, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(4, 5);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(4, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(5, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(6, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(6, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(7, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(7, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(8, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(8, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(9, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(10, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(11, 4);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(11, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(12, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(13, 2);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(13, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(14, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(15, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(16, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(17, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(18, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(19, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(20, 4);
INSERT INTO ai_has_description(ai_id, description_id) VALUES(20, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(21, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(22, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(23, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(24, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(25, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(26, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(27, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(28, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(29, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(30, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(31, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(32, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(33, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(34, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(35, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(36, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(37, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(38, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(39, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(40, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(41, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(42, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(43, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(44, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(45, 1);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(46, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(47, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(48, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(49, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(50, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(51, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(52, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(53, 5);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(54, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(55, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(56, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(57, 2);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(58, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(59, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(60, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(61, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(62, 4);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(63, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(64, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(65, 7);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(66, 6);

INSERT INTO ai_has_description(ai_id, description_id) VALUES(67, 1);

```

## Rating

```sql
UPDATE ai SET rating = 5 WHERE name = 'ChatGPT';
UPDATE ai SET rating = 4 WHERE name = 'Claude';
UPDATE ai SET rating = 4 WHERE name = 'Google Bard';
UPDATE ai SET rating = 3 WHERE name = 'Microsoft Bing Chat';
UPDATE ai SET rating = 3 WHERE name = 'DeepSeek';
UPDATE ai SET rating = 4 WHERE name = 'LLaMA (Meta)';
UPDATE ai SET rating = 3 WHERE name = 'Cohere';
UPDATE ai SET rating = 3 WHERE name = 'HuggingChat (Hugging Face)';
UPDATE ai SET rating = 4 WHERE name = 'Perplexity AI';
UPDATE ai SET rating = 3 WHERE name = 'Jasper AI';
UPDATE ai SET rating = 4 WHERE name = 'Character.AI';
UPDATE ai SET rating = 2 WHERE name = 'Replika';
UPDATE ai SET rating = 3 WHERE name = 'OpenAssistant';
UPDATE ai SET rating = 3 WHERE name = 'Sparrow (DeepMind)';
UPDATE ai SET rating = 3 WHERE name = 'EleutherAI';
UPDATE ai SET rating = 3 WHERE name = 'DoNotPay';
UPDATE ai SET rating = 3 WHERE name = 'Kira Systems';
UPDATE ai SET rating = 3 WHERE name = 'Casetext';
UPDATE ai SET rating = 3 WHERE name = 'Luminance';
UPDATE ai SET rating = 2 WHERE name = 'AIVA (AI Music Composition)';
UPDATE ai SET rating = 4 WHERE name = 'Runway ML';
UPDATE ai SET rating = 3 WHERE name = 'Sudowrite';
UPDATE ai SET rating = 2 WHERE name = 'Artbreeder';
UPDATE ai SET rating = 2 WHERE name = 'Jukebox (OpenAI)';
UPDATE ai SET rating = 2 WHERE name = 'DeepArt';
UPDATE ai SET rating = 4 WHERE name = 'NovelAI';
UPDATE ai SET rating = 3 WHERE name = 'Google Cloud AI Predictions';
UPDATE ai SET rating = 3 WHERE name = 'IBM Watson Predictive Analytics';
UPDATE ai SET rating = 3 WHERE name = 'RapidMiner';
UPDATE ai SET rating = 3 WHERE name = 'DataRobot';
UPDATE ai SET rating = 3 WHERE name = 'H2O.ai';
UPDATE ai SET rating = 3 WHERE name = 'Alteryx';
UPDATE ai SET rating = 4 WHERE name = 'Netflix Recommendations';
UPDATE ai SET rating = 4 WHERE name = 'Spotify Recommendations';
UPDATE ai SET rating = 4 WHERE name = 'Amazon Personalize';
UPDATE ai SET rating = 3 WHERE name = 'Siri';
UPDATE ai SET rating = 3 WHERE name = 'Alexa';
UPDATE ai SET rating = 4 WHERE name = 'Google Assistant';
UPDATE ai SET rating = 2 WHERE name = 'Hound (SoundHound)';
UPDATE ai SET rating = 2 WHERE name = 'Open Voice OS';
UPDATE ai SET rating = 5 WHERE name = 'DALL-E (OpenAI)';
UPDATE ai SET rating = 5 WHERE name = 'MidJourney';
UPDATE ai SET rating = 4 WHERE name = 'DeepMind Gemini';
UPDATE ai SET rating = 5 WHERE name = 'OpenAI GPT-4V';
UPDATE ai SET rating = 4 WHERE name = 'CLIP (OpenAI)';
UPDATE ai SET rating = 4 WHERE name = 'Imagen';
UPDATE ai SET rating = 3 WHERE name = 'OpenAI Five (Dota 2 AI)';
UPDATE ai SET rating = 5 WHERE name = 'DeepMind AlphaGo';
UPDATE ai SET rating = 3 WHERE name = 'Nvidia GameGAN';
UPDATE ai SET rating = 3 WHERE name = 'AI Dungeon';
UPDATE ai SET rating = 3 WHERE name = 'Modl.ai';
UPDATE ai SET rating = 5 WHERE name = 'GitHub Copilot';
UPDATE ai SET rating = 3 WHERE name = 'Tabnine';
UPDATE ai SET rating = 3 WHERE name = 'CodeT5';
UPDATE ai SET rating = 4 WHERE name = 'Code Llama';
UPDATE ai SET rating = 3 WHERE name = 'Cogram';
UPDATE ai SET rating = 3 WHERE name = 'Amazon CodeWhisperer';
UPDATE ai SET rating = 5 WHERE name = 'Stable Diffusion';
UPDATE ai SET rating = 5 WHERE name = 'Runway Gen-2';
UPDATE ai SET rating = 4 WHERE name = 'Pika Labs';
UPDATE ai SET rating = 5 WHERE name = 'Leonardo AI';
UPDATE ai SET rating = 4 WHERE name = 'Dream by Wombo (Wombo Dream)';
UPDATE ai SET rating = 4 WHERE name = 'Synthesia';
UPDATE ai SET rating = 3 WHERE name = 'DeepBrain AI';
UPDATE ai SET rating = 5 WHERE name = 'Boston Dynamics';
UPDATE ai SET rating = 4 WHERE name = 'Tesla Autopilot';
UPDATE ai SET rating = 3 WHERE name = 'MuJoCo';
```

## price

```sql
UPDATE ai SET price = 'Free plan available, offering basic access to ChatGPT. Plus plan at $20/month includes access to GPT-4 and faster response times.' WHERE id = 1;
UPDATE ai SET price = 'Pricing not publicly available. Custom plans are offered based on enterprise needs.' WHERE id = 2;
UPDATE ai SET price = 'Free access with premium features expected to be rolled out in the future.' WHERE id = 3;
UPDATE ai SET price = 'Free access with limited features. Business plans start at $10/month for extended usage and premium features.' WHERE id = 4;
UPDATE ai SET price = 'Free access with basic features. Premium features available with Microsoft 365 subscription.' WHERE id = 5;
UPDATE ai SET price = 'Pricing not publicly available. Typically available through Meta\'s partnership programs or via custom contracts.' WHERE id = 6;
UPDATE ai SET price = 'Free tier offers limited API usage. Paid plans start at $0.25 per 1,000 tokens for smaller businesses, with custom enterprise plans.' WHERE id = 7;
UPDATE ai SET price = 'Free access with limited API usage. Pro plans start at $9/month, offering enhanced performance and additional API calls.' WHERE id = 8;
UPDATE ai SET price = 'Free access with limited functionality. Premium plans available for enhanced usage, pricing on request.' WHERE id = 9;
UPDATE ai SET price = 'Starts at $39/month for the Starter plan, with Professional plans offering additional features for $99/month.' WHERE id = 10;
UPDATE ai SET price = 'Free basic access, with additional features available through paid subscription starting at $5/month.' WHERE id = 11;
UPDATE ai SET price = 'Free plan with limited interactions. Paid plans range from $7.99/month for the Pro version, to $22.99/month for the Premium version.' WHERE id = 12;
UPDATE ai SET price = 'Pricing not publicly disclosed, expected to have both free and enterprise-level plans.' WHERE id = 13;
UPDATE ai SET price = 'Free access for research purposes. Custom enterprise plans available upon request.' WHERE id = 14;
UPDATE ai SET price = 'Free open-source access with no paid plans currently.' WHERE id = 15;
UPDATE ai SET price = 'Starts at $3/month for the basic plan. Higher-tier plans at $10/month for expanded services like legal consultations.' WHERE id = 16;
UPDATE ai SET price = 'Pricing is custom and based on the scale of the client’s business.' WHERE id = 17;
UPDATE ai SET price = 'Free trial available, with subscription plans starting at $65/month for individuals, with higher pricing for businesses.' WHERE id = 18;
UPDATE ai SET price = 'Custom pricing based on enterprise use cases, typically starting from $10,000/year.' WHERE id = 19;
UPDATE ai SET price = 'Free plan with limited tracks. Premium plans start at $11.99/month, with business plans available.' WHERE id = 20;
UPDATE ai SET price = 'Free plan with limited model usage. Pro plans start at $12/month for extended features.' WHERE id = 21;
UPDATE ai SET price = 'Starts at $10/month for the basic plan, with additional features at $25/month for the Pro plan.' WHERE id = 22;
UPDATE ai SET price = 'Free access with limited creation. Premium plans start at $8.99/month for extended features and higher resolution images.' WHERE id = 23;
UPDATE ai SET price = 'Free access, with no announced pricing for paid plans as of now.' WHERE id = 24;
UPDATE ai SET price = 'Free plan with low-resolution outputs. Paid plans start at $5 for high-resolution images.' WHERE id = 25;
UPDATE ai SET price = 'Starts at $10/month for the basic plan, with additional features at $25/month for the Pro plan.' WHERE id = 26;
UPDATE ai SET price = 'Custom pricing based on usage; pay-as-you-go model for API calls.' WHERE id = 27;
UPDATE ai SET price = 'Starts at $99/month for the base plan with enterprise pricing available.' WHERE id = 28;
UPDATE ai SET price = 'Free plan with limited functionality. Paid plans start at $2,500/year for additional features and services.' WHERE id = 29;
UPDATE ai SET price = 'Custom pricing based on enterprise use; typically starts from $10,000/year.' WHERE id = 30;
UPDATE ai SET price = 'Free plan available. Paid plans for enterprise users typically start at $8,000/year.' WHERE id = 31;
UPDATE ai SET price = 'Starts at $5,195/year for the Designer license. Enterprise pricing available for teams.' WHERE id = 32;
UPDATE ai SET price = 'Free access, integrated directly with Netflix.' WHERE id = 33;
UPDATE ai SET price = 'Free access for developers with API usage limits.' WHERE id = 34;
UPDATE ai SET price = 'Pay-as-you-go pricing with costs based on the volume of usage.' WHERE id = 35;
UPDATE ai SET price = 'Free access with all Apple devices.' WHERE id = 36;
UPDATE ai SET price = 'Free for basic use, with premium features available through Amazon services.' WHERE id = 37;
UPDATE ai SET price = 'Free access across all Google devices.' WHERE id = 38;
UPDATE ai SET price = 'Free access with basic features. Premium features available for specific partners.' WHERE id = 39;
UPDATE ai SET price = 'Free access for basic use; enterprise pricing available.' WHERE id = 40;
UPDATE ai SET price = 'Free plan available with limited image generations. Paid plans start at $15/month for more usage.' WHERE id = 41;
UPDATE ai SET price = 'Subscription plans start at $10/month for basic access, with higher-tier plans offering more generations for $30/month.' WHERE id = 42;
UPDATE ai SET price = 'Custom pricing based on usage, typically available through partnerships with large enterprises.' WHERE id = 43;
UPDATE ai SET price = 'Access to GPT-4 available at $20/month (via ChatGPT Plus), with API usage priced separately based on usage.' WHERE id = 44;
UPDATE ai SET price = 'Free access to the research version; API usage is pay-as-you-go.' WHERE id = 45;
UPDATE ai SET price = 'Pricing not publicly disclosed. Typically available via API with pay-as-you-go model.' WHERE id = 46;
UPDATE ai SET price = 'Free access for research projects. Enterprise plans available for specific use cases.' WHERE id = 47;
UPDATE ai SET price = 'Free access for research purposes, with enterprise-level partnerships for access.' WHERE id = 48;
UPDATE ai SET price = 'Custom pricing for enterprise-level access and usage.' WHERE id = 49;
UPDATE ai SET price = 'Free plan with limited story generation. Paid plans start at $10/month for more features.' WHERE id = 50;
UPDATE ai SET price = 'Custom pricing available based on enterprise needs and API usage.' WHERE id = 51;
UPDATE ai SET price = '$10/month for individual users; enterprise plans available for teams.' WHERE id = 52;
UPDATE ai SET price = 'Free for basic usage; paid plans start at $12/month for individuals and scale for teams.' WHERE id = 53;
UPDATE ai SET price = 'Free access with API limits. Paid plans available for more usage, pricing varies based on usage.' WHERE id = 54;
UPDATE ai SET price = 'Free access for basic use, with premium plans available for larger scale usage.' WHERE id = 55;
UPDATE ai SET price = 'Pricing not publicly available. Typically based on enterprise needs.' WHERE id = 56;
UPDATE ai SET price = 'Free for basic use; paid plans start at $10/month for additional usage.' WHERE id = 57;
UPDATE ai SET price = 'Custom pricing based on scale and usage; typically starts from $100/month for individuals.' WHERE id = 58;
UPDATE ai SET price = 'Free for basic use. Premium features available at $5/month.' WHERE id = 59;
UPDATE ai SET price = 'Pricing starts at $30/month for individual users, with enterprise pricing available.' WHERE id = 60;
UPDATE ai SET price = 'Custom pricing based on usage and business needs.' WHERE id = 61;
UPDATE ai SET price = 'Free for basic use. Premium features available at $5/month.' WHERE id = 62;
UPDATE ai SET price = 'Pricing starts at $30/month for individual users, with enterprise pricing available.' WHERE id = 63;
UPDATE ai SET price = 'Custom pricing based on usage and enterprise needs.' WHERE id = 64;
UPDATE ai SET price = 'Custom enterprise pricing based on contract details.' WHERE id = 65;
UPDATE ai SET price = 'Available as part of Tesla\'s Full Self-Driving package, priced at $15,000 for lifetime access or $199/month for subscription.' WHERE id = 66;
UPDATE ai SET price = 'Starts at $850/year for individual use, with pricing available for teams and enterprises.' WHERE id = 67;

```

# SQL-Statements für die Website

nach was muss gefiltert werden?
1. preis 
2. name
3. rating
4. nutzen

## KI ändern/erstellen

**Neue KI einfügen**
name, link, price sind strings
rating is ne zahl zwischen 1 und 5
```py
f"INSERT INTO ai(name, link, price, rating) values({name}, {link}, {price}, {rating});" 
```

**rating ändern**
name
rating - zahl von 1-5
```py
f"UPDATE ai SET rating={rating} WHERE name={name}"
```

**price ändern**
name - str
price - str
```py
f"UPDATE ai SET price={price} WHERE name={name}"
```

## KIs filtern

**KIs, beginnend mit name**
```py
f"SELECT name, link, price, rating FROM ai WHERE name LIKE '{name_%}'"
```

**KIs nach rating**
absteigendes rating
```py
"SELECT name, link, price, rating FROM ai ORDER BY rating;"
```

rating mind 'x'
x ist eine zahl von 1 bis 5
```py
f"SELECT name, link, price, rating FROM ai WHERE rating>{x}"
```

**nach Preismodell filtern**
pricingModel kann 'free', 'paid' oder 'paid or free' sein `SELECT name FROM pricingModel`
```py
f"""
	SELECT 
	    ai.name, 
	    ai.link, 
	    ai.price, 
	    ai.rating 
	FROM 
	    ai 
	JOIN ai_has_pricingmodel 
	    ON ai.id = ai_has_pricingmodel.ai_id 
	JOIN pricingmodel 
	    ON ai_has_pricingmodel.pricingmodel_id = pricingmodel.id 
	WHERE 
	    pricingmodel.name = '{pricingModel}';
"""
```

**nach type filtern**
type ist einer der werte von `SELECT name FROM type;`
```py
f"""
	SELECT 
	    ai.name, 
	    ai.link, 
	    ai.price, 
	    ai.rating 
	FROM 
	    ai 
	JOIN ai_has_type 
	    ON ai.id = ai_has_type.ai_id 
	JOIN type
	    ON ai_has_type.type_id = type.id 
	WHERE 
	    type.name = '{type}';
"""
```

**nach targetgroup filtern**
```py
f"""
	SELECT 
	    ai.name, 
	    ai.link, 
	    ai.price, 
	    ai.rating 
	FROM 
	    ai 
	JOIN ai_has_targetgroup
	    ON ai.id = ai_has_targetgroup.ai_id 
	JOIN type
	    ON ai_has_targetgroup.targetgroup_id = targetgroup.id 
	WHERE 
	    targetgroup.name = '{targetgroup}';
"""
```

**nach description filtern**

```py
f"""
	SELECT 
	    ai.name, 
	    ai.link, 
	    ai.price, 
	    ai.rating 
	FROM 
	    ai 
	JOIN ai_has_description
	    ON ai.id = ai_has_description.ai_id 
	JOIN type
	    ON ai_has_description.description_id = description.id 
	WHERE 
	    description.name = '{description}';
"""
```