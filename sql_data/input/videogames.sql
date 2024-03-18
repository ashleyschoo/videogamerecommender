
-- 1.0 Setup. Delete tables after every build iteration.
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS VideoGames, temp_VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating;
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
  IGNORE 1 LINES
  (AgeRating);


-- 2.2 GenreCateogry
CREATE TABLE IF NOT EXISTS  GenreCategory (
  GenreCategoryID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  GenreCategory VARCHAR(255) NOT NULL,
  PRIMARY KEY (GenreCategoryID)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/Users/ashle/OneDrive/Documents/Software Engineering/videogamerecommender/sql_data/output/GenreCategory.csv'
INTO TABLE GenreCategory
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (GenreCategory);


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
  IGNORE 1 LINES
  (NumberofPlayers);



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
  IGNORE 1 LINES
  (PopularityRating);



-- 2.5 video games temp table
 
 CREATE  TABLE temp_VideoGames 
 (
  VideoGameID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  VideoGameName VARCHAR(255) NOT NULL,
  PC_Windows VARCHAR(1),
  PC_MAC VARCHAR(1),
  Playstation VARCHAR(1),
  NintendoSwitch VARCHAR(1),
  Xbox VARCHAR(1),
  Phone_Android VARCHAR(1),
  Phone_iPhone VARCHAR(1),
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

-- 2.6 video games permanent table
CREATE TABLE IF NOT EXISTS VideoGames (
  VideoGameID INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  VideoGameName VARCHAR(255) NOT NULL,
  PC_Windows VARCHAR(1),
  PC_MAC VARCHAR(1),
  Playstation VARCHAR(1),
  NintendoSwitch VARCHAR(1),
  Xbox VARCHAR(1),
  Phone_Android VARCHAR(1),
  Phone_iPhone VARCHAR(1),
  Description VARCHAR(255),
  YouTubeTrailerLink VARCHAR(255),
  AgeRatingID INTEGER,
  GenreCategoryID INTEGER,
  NumberofPlayersID INTEGER,
  PopularityRatingID INTEGER,
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
  AgeRatingID,
  GenreCategoryID,
  NumberofPlayersID,
  PopularityRatingID
 )
   SELECT DISTINCT v.VideoGameName, v.PC_Windows, v.PC_MAC, v.Playstation, v.NintendoSwitch, v.Xbox, v.Phone_Android, v.Phone_iPhone, v.Description,
  v.YouTubeTrailerLink, a.AgeRatingID, g.GenreCategoryID, n.NumberofPlayersID, p.PopularityRatingID
  FROM temp_VideoGames as v
  LEFT JOIN AgeRating as a
  ON v.AgeRating = REPLACE(a.AgeRating, char(13),'')
  LEFT JOIN GenreCategory as g
  ON v.GenreCategory = REPLACE(g.GenreCategory, char(13),'')
  LEFT JOIN NumberofPlayers as n
  ON v.NumberofPlayers = REPLACE(n.NumberofPlayers, char(13),'')
  LEFT JOIN PopularityRating as p
  ON v.PopularityRating = p.PopularityRating;

