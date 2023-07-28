---
title: "SQL Notebook"
output: html_notebook
---

# SQL Baseball Project

This is my project for my CS2550 Relational Database & SQL Course

__I was given an ERD by the instructor:
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/Baseball_ERD.PNG?raw=true)

##I was instructed to create a database and tables, per the model. 

##I began by creating the database:
```{sql connection=}
DROP DATABASE IF EXISTS BaseballDatabase;
CREATE DATABASE IF NOT EXISTS BaseballDatabase;
USE BaseballDatabase;
```
##I then created the tables, starting with the tables that had no foreign keys:
```{sql connection=}
CREATE TABLE IF NOT EXISTS Player (
    PlayerID SMALLINT PRIMARY KEY NOT NULL,
    PlayerName VARCHAR(30) NOT NULL,
    PlayerDOB DATE
);
CREATE TABLE IF NOT EXISTS Team (
    TeamID SMALLINT PRIMARY KEY NOT NULL,
    TeamName VARCHAR(50) NOT NULL,
    TeamCity VARCHAR(50),
    TeamManager VARCHAR(50) NOT NULL
);
```

##I then created the tables with foreign keys:
```{sql connection=}
CREATE TABLE IF NOT EXISTS Bat (
    BatSerialNumber SMALLINT NOT NULL,
    BatManufacturer VARCHAR(50),
    TeamID SMALLINT NOT NULL,
    FOREIGN KEY (TeamID)
        REFERENCES Team (TeamID),
    PRIMARY KEY (BatSerialNumber)
);
CREATE TABLE IF NOT EXISTS PlayerHistory (
    PlayerHistoryID SMALLINT NOT NULL,
    TeamID SMALLINT NOT NULL,
    PlayerID SMALLINT NOT NULL,
    PlayerBatingAverage DECIMAL(6 , 2 ),
    PlayerStartDate DATE,
    PlayerEndDate DATE,
    PlayerPosition VARCHAR(10),
    FOREIGN KEY (TeamID)
        REFERENCES Team (TeamID),
    FOREIGN KEY (PlayerID)
        REFERENCES Player (PlayerID),
    PRIMARY KEY (PlayerHistoryID)
);
CREATE TABLE IF NOT EXISTS Coach (
    CoachID SMALLINT NOT NULL,
    CoachName VARCHAR(30),
    CoachPhoneNumber VARCHAR(20),
    CoachSalary DECIMAL(8 , 2 ),
    TeamID SMALLINT NOT NULL,
    FOREIGN KEY (TeamID)
        REFERENCES Team (TeamID),
    PRIMARY KEY (CoachID)
);
CREATE TABLE IF NOT EXISTS UnitsOfWork (
    UnitsNumber SMALLINT NOT NULL,
    NumberOfYears TINYINT,
    ExperienceType VARCHAR(30),
    CoachID SMALLINT NOT NULL,
    FOREIGN KEY (CoachID)
        REFERENCES Coach (CoachID),
    PRIMARY KEY (UnitsNumber)
);
```

##Next, I was instructed to insert data for four Teams using one statement:
```{sql connection=}
INSERT INTO Team (TeamID, TeamName, TeamCity, TeamManager)
VALUES  (1234, 'Red Sox', 'Boston', 'Homer Simpson'),
		(4321, 'Giants', 'San Francisco', 'Albert Einstein'),
		(2222, 'Athletics', 'Oakland', 'Ewan McGregor'),
		(9876, 'Mariners', 'Seattle', 'Ru Paul');
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/Team_Table.PNG?raw=true)

##I was then instructed to insert data for six Players using one statement:
```{sql connection=}
INSERT INTO Player (PlayerID, PlayerName, PlayerDOB)
VALUES  (20357, 'Larry Hansen', '1975-06-08'),
		(20159, 'Sebastian Garcia', '2000-02-27'),
		(20687, 'Jose Canseco', '1960-10-21'),
		(20654, 'Babe Ruth', '1900-01-01'),  
        (20158, 'Steve Rogers', '1920-07-04'),
        (20475, 'Chuck Berry', '1932-05-11');
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/Player_Table.PNG?raw=true)

##Next, I was instructed to insert data for four coaches (one for each of the first three teams, and the last one --assigned to team 3 not team 4), using one statement:
```{sql connection=}
INSERT INTO Coach (CoachID, CoachName, CoachPhoneNumber, CoachSalary, TeamID)
VALUES  (19670, 'Tom Cruise', '801-555-1234', '44681.23', 1234),
		(16546, 'Will Smith', '415-555-7894', '14248.52', 4321),
		(15848, 'Barrack Obama', '510-555-3547', '66478.65', 2222),
		(13673, 'Will Ferrell', '365-555-9846', '48968.54', 2222);
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/Coach_Table.PNG?raw=true)

##I was then instructed to insert data for three UnitsOfWork (for the first three coaches only):
```{sql connection=}
INSERT INTO UnitsOfWork (UnitsNumber, NumberOfYears, ExperienceType, CoachID)
VALUES  (1, 25, 'Head Coach', 19670),
		(2, 8, 'Player', 16546),
		(3, 17, 'Assistant Coach', 15848);
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/UnitsOfWork_Table.PNG?raw=true)

##Next, I was instructed to insert data for Player History for the six Players – assigning half of them to Team 1 and --half to Team 2 - ##leaving EndDate NULL for all 6, and making sure you do not assign any of the Players to Team 3:
```{sql connection=}
INSERT INTO PlayerHistory (PlayerHistoryID, TeamID, PlayerID, PlayerBatingAverage, PlayerStartDate, PlayerEndDate, PlayerPosition)
VALUES  (951, 1234, 20357, '300', '2003-07-21', NULL, 'First Base'),
		(753, 1234, 20159, '251', '1991-12-10', NULL, 'Pitcher'),
		(357, 1234, 20687, '450', '2010-02-08', NULL, 'Third Base'),
		(159, 4321, 20654, '362', '2014-03-11', NULL, 'Pitcher'),  
    (852, 4321, 20158, '156', '1987-04-02', NULL, 'Catcher'),
    (369, 4321, 20475, '276', '2000-08-01', NULL, 'Left Field');
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/PlayerHistory.PNG?raw=true)

##I was then instructed to update the player history (in one statement) for Player's #2, 4, and 6 – making his/her End --date July 7, 2020:
```{sql connection=}
UPDATE PlayerHistory 
SET 
    PlayerEndDate = '2020-07-07'
WHERE
    (PlayerID = '20159')
        OR (PlayerID = '20654')
        OR (PlayerID = '20475')
;
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/gh-pages/Baseball1.PNG?raw=true)

##Next, I was instructed to update the team manager’s name to ‘Vacant’ for all teams without players assigned. I had to --figure out what teams these were within the update statement by using a subquery or JOIN:
```{sql connection=}
UPDATE Team t
        LEFT JOIN
    PlayerHistory p ON p.TeamID = t.TeamID 
SET 
    TeamManager = 'Vacant'
WHERE
    p.PlayerID IS NULL;
;
```

##I was then instructed to update all the coach’s salaries, as long as they have units of Work. I was instructed not to --assume this is Coach 4, but rather use a subquery or JOIN within my statement. Then I was to increase the salary by 2.--55% and round to the nearest whole number – zero cents.
```{sql connection=}
UPDATE Coach c
        LEFT JOIN
    UnitsOfWork u ON c.CoachID = u.CoachID 
SET 
    CoachSalary = FORMAT(CoachSalary + (CoachSalary * .0255),
        0)
WHERE
    u.CoachID IS NULL
;
```

##Next, I was instructed to delete the UnitOfWork for all coaches whose Team’s City does NOT begin with R, S, or T:
```{sql connection=}
DELETE UnitsOfWork FROM UnitsOfWork u
        LEFT JOIN
    Coach c ON c.CoachID = u.CoachID
        LEFT JOIN
    Team t ON t.TeamID = c.TeamID 
WHERE
    TeamCity NOT IN ('r%' , 's%', 't%')
;
```

##Finally, I was instructed to delete the player history of the two players with the lowest batting average using a subquery or JOIN to figure which ones are the lowest:
```{sql connection=}
DELETE FROM PlayerHistory ORDER BY PlayerBatingAverage LIMIT 2
;
```
