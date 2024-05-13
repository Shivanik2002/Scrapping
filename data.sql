show databases;
create DATABASE Scrap_db;
use Scrap_db;
show tables;
CREATE table scrap_data(Name varchar(100),Description varchar(400),Camera_quality varchar(400),Price varchar(50),Rating int,Image_url varchar(500));
SELECT * from scrap_data;
LOAD DATA INFILE '/home/shivi/Documents/Website/Scrapping.csv'
INTO TABLE scrap_data 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
