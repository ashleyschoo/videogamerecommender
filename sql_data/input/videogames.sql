
 --DROP DATABASE IF EXISTS VideoGames;

 --CREATE DATABASE VideoGames;
 USE VideoGames;



-- 1.0 Setup. Delete tables after every build iteration.
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating;
SET FOREIGN_KEY_CHECKS=1;

-- 2.0 ENTITIES
-- Serve as lookup tables
-- 2.1 AgeRating
CREATE TABLE IF NOT EXISTS AgeRating (
  AgeRatingID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  AgeRating VARCHAR(255) NOT NULL,
  PRIMARY KEY (AgeRatingID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/AgeRating.csv'
INTO TABLE AgeRating
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (AgeRating);

--INSERT INTO AgeRating VALUES ('Everyone','Everyone10+','Teen13+','Mature17+','Adult18+');

-- 2.2 GenreCateogry
CREATE TABLE IF NOT EXISTS  GenreCategory (
  GenreCategoryID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  GenreCategory VARCHAR(255) NOT NULL,
  PRIMARY KEY (GenreCategoryID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/GenreCateogry.csv'
INTO TABLE GenreCateogry
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (GenreCateogry);

--INSERT INTO GenreCategory VALUES ('Cozy','Horror','FPS','Adventure/RPG','Puzzle/Word','City Builder','Racing','Third-person Shooter','Fighting','Sports');

-- 2.3 NumberofPlayers
CREATE TABLE IF NOT EXISTS NumberofPlayers (
  NumberofPlayersID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  NumberofPlayers VARCHAR(255) NOT NULL,
  PRIMARY KEY (NumberofPlayersID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/NumberofPlayers.csv'
INTO TABLE NumberofPlayers
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (NumberofPlayers);

--INSERT INTO NumberofPlayers VALUES ('1','2','3-4','5+');


-- 2.4 PopularityRating
CREATE TABLE IF NOT EXISTS PopularityRating (
  PopularityRatingID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  PopularityRating VARCHAR(255) NOT NULL,
  PRIMARY KEY (PopularityRatingID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/PopularityRating.csv'
INTO TABLE PopularityRating
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (PopularityRating);

--INSERT INTO PopularityRating VALUES ('Overwhelmingly Positive','Very Positive','Positive','Mostly Positive');


-- 2.5 video games table
 
 CREATE TEMPORARY TABLE temp_VideoGames 
 (
  VideoGameID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  VideoGameName VARCHAR(255) NOT NULL,
  PC_Windows binary(1),
  PC_MAC binary(1),
  Playstation binary(1),
  NintendoSwitch binary(1),
  Xbox binary(1),
  Phone_Android binary(1),
  Phone_iPhone binary(1),
  Description VARCHAR(255),
  YouTubeTrailerLink VARCHAR(255),
  AgeRating VARCHAR(255),
  GenreCategory VARCHAR(255),
  NumberofPlayers VARCHAR(255),
  PopularityRating VARCHAR(255)
 )
 ENGINE=InnoDB
 CHARACTER SET utf8mb4
 COLLATE utf8mb4_0900_ai_ci;

 LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/video_game_csv_trimmed.csv'
 INTO TABLE temp_VideoGames
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (  
  VideoGameID,
  VideoGameName,
  PC_Windows,
  PC_MAC,
  Playstation,
  NintendoSwitch,
  Xbox,
  Phone_Android,
  Phone_iPhone,
  Description,
  YouTubeTrailerLink,
  AgeRating,
  GenreCategory,
  NumberofPlayers,
  PopularityRating
  );

CREATE TABLE IF NOT EXISTS VideoGames (
  VideoGameID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  VideoGameName VARCHAR(255) NOT NULL,
  PC_Windows binary(1),
  PC_MAC binary(1),
  Playstation binary(1),
  NintendoSwitch binary(1),
  Xbox binary(1),
  Phone_Android binary(1),
  Phone_iPhone binary(1),
  Description VARCHAR(255),
  YouTubeTrailerLink VARCHAR(255),
  PRIMARY KEY (VideoGameID),
  FOREIGN KEY (AgeRatingID) REFERENCES AgeRating(AgeRatingID) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (GenreCategoryID) REFERENCES GenreCategory(GenreCategoryID) ON DELETE RESTRICT ON UPDATE CASCADE,  
  FOREIGN KEY (NumberofPlayersID) REFERENCES NumberofPlayers(NumberofPlayersID) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (PopularityRatingID) REFERENCES PopularityRating(PopularityRatingID) ON DELETE RESTRICT ON UPDATE CASCADE

)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO VideoGames
(
  VideoGameName,
  PC_Windows,
  PC_MAC,
  Playstation,
  NintendoSwitch,
  Xbox,
  Phone_Android,
  Phone_iPhone,
  Description,
  YouTubeTrailerLink,
  AgeRating_ID,
  GenreCategory_ID,
  NumberofPlayers_ID,
  PopularityRating_ID
 )
  SELECT DISTINCT v.*, a.AgeRating_ID, g.GenreCategory_ID, n.NumberofPlayers_ID, p.PopularityRating_ID
  FROM temp_VideoGames as v
  LEFT JOIN AgeRating as a
  ON v.AgeRating = a.AgeRating
  LEFT JOIN GenreCategory as g
  ON v.GenreCategory = g.GenreCategory
  LEFT JOIN NumberofPlayers as n
  ON v.NumberofPlayers = n.NumberofPlayers
  LEFT JOIN PopularityRating as p
  ON v.PopularityRating = p.PopularityRating;

