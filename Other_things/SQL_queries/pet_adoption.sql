----Creating Database
create database pet_adoption;

use pet_adoption;

----Creating Table
create table adoptions(
animal_id int not null,
name varchar(40),
contact varchar(40)
);

select *from sys.tables;

----Creating Table
create table animals(
id int not null,
name varchar(40),
breed varchar(30),
color varchar(30),
gender varchar(10),
status int
);

---- Storing Data
insert into animals(id,name,breed,color,gender,status) values(501,'Bellyflop','Beagle','Brown','Male',0);
insert into animals(id,name,breed,color,gender,status) values(502,'Snowy','Husky','White','Female',0);
insert into animals(id,name,breed,color,gender,status) values(503,'Princes','Pomarnian','Black','Female',0);
insert into animals(id,name,breed,color,gender,status) values(504,'Cricket','Chihuahua','Brown','Female',0);
insert into animals(id,name,breed,color,gender,status) values(505,'Spot','Dalmation','Black and White','Male',0);

select * from animals;

---- Updating data in table
update animals set color='Brown and red' where name='Spot';
update animals set color='Red' where id=501;
update animals set status=1 where gender='Female';

---- Deleting Data from table
delete animals where id=501;

---- Retrieving specific attributes
select id,name from animals where status=1;

---- Retrieving selected Rows
SELECT TOP 2 * FROM animals;

---- Filtering Data: Where clause
select name,breed from animals where gender='Female';

---- Filtering Data:IN,DISTINCT,AND,OR,IN
SELECT * FROM animals WHERE id IN (501, 502, 503);
SELECT DISTINCT color FROM animals;
SELECT * FROM animals WHERE gender = 'Female' AND breed = 'Husky';
SELECT * FROM animals WHERE breed = 'Husky' OR breed = 'Chihuahua';

---- Filtering Data: BETWEEN,LIKE,Column & table aliases
SELECT * FROM animals WHERE id BETWEEN 502 AND 504;
SELECT * FROM animals WHERE color LIKE '%Brown%';
SELECT name AS AnimalName, breed AS BreedType, color AS FurColor FROM animals;
SELECT a.id, a.name, a.breed FROM animals AS a WHERE a.gender = 'Male';

---- Implementing Data Integrity 
ALTER TABLE animals
ADD CONSTRAINT PK_Animals PRIMARY KEY (id);

ALTER TABLE animals
ADD CONSTRAINT CHK_Animal_Gender CHECK (gender IN ('Male', 'Female'));

ALTER TABLE animals
ADD CONSTRAINT CHK_Animal_Status CHECK (status IN (0, 1));

---- Using Functions to Customize the Result Set
SELECT name, LEN(name) AS NameLength FROM animals;

---- Using String Functions
SELECT CONCAT(name, ' is a ', breed) AS AnimalDescription FROM animals;

---- Using Date Functions
ALTER TABLE animals
ADD date_of_birth DATE;

UPDATE animals SET date_of_birth = '2020-06-25' WHERE id = 502;
UPDATE animals SET date_of_birth = '2019-11-11' WHERE id = 503;
UPDATE animals SET date_of_birth = '2017-01-03' WHERE id = 504;
UPDATE animals SET date_of_birth = '2021-02-10' WHERE id = 505;

SELECT name, 
       YEAR(date_of_birth) AS BirthYear,
       MONTH(date_of_birth) AS BirthMonth,
       DAY(date_of_birth) AS BirthDay
FROM animals;

---- Using Mathematical Functions
ALTER TABLE animals ADD weight DECIMAL(5, 2);

UPDATE animals SET weight = CASE id
    WHEN 502 THEN 45.5
    WHEN 503 THEN 10.2
    WHEN 504 THEN 8.0
    WHEN 505 THEN 50.0
END;

SELECT name, ABS(weight) AS AbsoluteWeight FROM animals;

---- Using System Functions
SELECT @@VERSION AS SqlServerVersion;

SELECT DB_NAME() AS CurrentDatabase;

SELECT GETDATE() AS CurrentDateTime;

---- Summarizing and Grouping Data
SELECT gender, SUM(weight) AS TotalWeight
FROM animals
GROUP BY gender;

---- Summarizing Data by Using Aggregate Functions
SELECT SUM(weight) AS TotalWeight
FROM animals;

---- Grouping Data
SELECT gender, COUNT(*) AS TotalCount
FROM animals
GROUP BY gender;

