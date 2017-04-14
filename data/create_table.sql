#CREATING DATABASE
DROP DATABASE IF EXISTS `ekatte`;
CREATE DATABASE `ekatte`;
USE `ekatte`;

#CREATING OBLAST TABLE
CREATE TABLE `oblast`(
	`oblast_id` varchar(4) NOT NULL,
	`ekatte` int(11) NOT NULL,
	`name` varchar(45) NOT NULL,
	`region` varchar(4) NOT NULL,
	PRIMARY KEY (`oblast_id`)
);

#IMPORTING DATA INTO OBLAST
LOAD DATA LOCAL INFILE 'Ek_obl.csv'
INTO TABLE `oblast`
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(`oblast_id`,`ekatte`,`name`,`region`,@dummy,@dummy);

#CREATING OBSHTINA TABLE
CREATE TABLE `obshtina`(
	`obshtina_id` varchar(5) NOT NULL,
	`ekatte` int(11) NOT NULL,
	`name` varchar(45) NOT NULL,
	PRIMARY KEY (`obshtina_id`)
);

#IMPORTING DATA INTO OBSHTINA
LOAD DATA LOCAL INFILE 'Ek_obst.csv'
INTO TABLE `obshtina`
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(`obshtina_id`,`ekatte`,`name`,@dummy,@dummy,@dummy);

#CREATING KMETSTVO TABLE
CREATE TABLE `kmetstvo`(
	`kmetstvo_id` varchar(8) NOT NULL,
	`name` varchar(45) NOT NULL,
	PRIMARY KEY (`kmetstvo_id`)
);

#IMPORTING DATA INTO KMETSTVO
LOAD DATA LOCAL INFILE 'Ek_kmet.csv'
INTO TABLE `kmetstvo`
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(`kmetstvo_id`,`name`,@dummy,@dummy,@dummy);

#CREATING SELISHTE TABLE
CREATE TABLE `selishte`(
	`ekatte` int(11) NOT NULL,
	`prefix` varchar(4) NOT NULL,
	`name` varchar(45) NOT NULL,
	`oblast_id` varchar(4) NOT NULL,
	`obshtina_id` varchar(5) NOT NULL,
	`kmetstvo_id` varchar(8) NOT NULL,
	`kind` enum('1','3','7'),
	PRIMARY KEY (`ekatte`)
);

#IMPORTING DATA INTO SELISHTE
LOAD DATA LOCAL INFILE 'Ek_atte.csv'
INTO TABLE `selishte`
FIELDS TERMINATED BY ','
IGNORE 2 LINES
(`ekatte`,`prefix`,`name`,`oblast_id`,`obshtina_id`,`kmetstvo_id`,`kind`,@dummy,@dummy,@dummy,@dummy,@dummy);

#CREATING REFERENES
ALTER TABLE `selishte`
ADD FOREIGN KEY (`oblast_id`) REFERENCES `oblast`(`oblast_id`);

ALTER TABLE `selishte`
ADD FOREIGN KEY (`obshtina_id`) REFERENCES `obshtina`(`obshtina_id`);

ALTER TABLE `oblast`
ADD FOREIGN KEY (`ekatte`) REFERENCES `selishte`(`ekatte`);

ALTER TABLE `obshtina`
ADD FOREIGN KEY (`ekatte`) REFERENCES `selishte`(`ekatte`);
