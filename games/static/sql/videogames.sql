
-- DROP DATABASE VideoGames;

-- CREATE DATABASE VideoGames;
-- USE VideoGames;
--
-- 1.0 Setup. Delete tables after every build iteration.
--
DROP TABLE IF EXISTS VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating;

-- 2.0 ENTITIES
-- Serve as lookup tables
-- 2.1 AgeRating
CREATE TABLE IF NOT EXISTS AgeRating (
  AgeRatingID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  AgeRating VARCHAR(250) NOT NULL,
  PRIMARY KEY (AgeRatingID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT INTO AgeRating VALUES ('Everyone','Everyone10+','Teen13+','Mature17+','Adult18+');

-- 2.2 GenreCateogry
CREATE TABLE IF NOT EXISTS GenreCategory (
  GenreCategoryID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  GenreCategory VARCHAR(250) NOT NULL,
  PRIMARY KEY (GenreCategoryID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT INTO temp_GenreCategory VALUES ('Cozy','Horror','FPS','Adventure/RPG','Puzzle/Word','City Builder','Racing','Third-person Shooter','Fighting','Sports');

-- 2.3 NumberofPlayers
CREATE TABLE IF NOT EXISTS NumberofPlayers (
  NumberofPlayersID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  NumberofPlayers VARCHAR(250) NOT NULL,
  PRIMARY KEY (NumberofPlayersID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT INTO NumberofPlayers VALUES ('1','2','3-4','5+');


-- 2.4 PopularityRating
CREATE TABLE IF NOT EXISTS PopularityRating (
  PopularityRatingID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  PopularityRating VARCHAR(250) NOT NULL,
  PRIMARY KEY (PopularityRatingID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT INTO PopularityRating VALUES ('Overwhelmingly Positive','Very Positive','Positive','Mostly Positive');


-- 2.5 video games table
 
CREATE TABLE IF NOT EXISTS VideoGames (
  VideoGameID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  VideoGameName VARCHAR(255) NOT NULL,
  PC(Windows) binary(1),
  PC(MAC) binary(1),
  Playstation binary(1),
  NintendoSwitch binary(1),
  Xbox binary(1),
  Phone(Android) binary(1),
  Phone(iPhone) binary(1),
  Description VARCHAR(255),
  YouTubeTrailerLink VARCHAR(255),
  PRIMARY KEY (VideoGameID),
  FOREIGN KEY (AgeRatingID) REFERENCES AgeRating(AgeRatingID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (GenreCategoryID) REFERENCES GenreCategory(GenreCategoryID) ON DELETE CASCADE ON UPDATE CASCADE,  
  FOREIGN KEY (NumberofPlayersID) REFERENCES NumberofPlayers(NumberofPlayersID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (PopularityRatingID) REFERENCES PopularityRating(PopularityRatingID) ON DELETE CASCADE ON UPDATE CASCADE
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

