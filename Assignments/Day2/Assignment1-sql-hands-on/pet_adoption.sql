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
