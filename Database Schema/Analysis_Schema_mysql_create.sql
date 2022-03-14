CREATE TABLE `Company_master` (
	`cmp_id` INT NOT NULL AUTO_INCREMENT,
	`cmp_name` varchar NOT NULL AUTO_INCREMENT,
	`Head_office` varchar NOT NULL AUTO_INCREMENT,
	`ceo_name` varchar NOT NULL AUTO_INCREMENT,
	`current_openings` VARCHAR(255) NOT NULL AUTO_INCREMENT,
	`cmp_date_created` DATE NOT NULL AUTO_INCREMENT,
	`cmp_user_created` varchar NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`cmp_id`)
);

CREATE TABLE `Job_master` (
	`job_id` INT NOT NULL AUTO_INCREMENT,
	`cmp_id` INT NOT NULL AUTO_INCREMENT,
	`job_post_id` INT NOT NULL AUTO_INCREMENT,
	`job_title` varchar NOT NULL AUTO_INCREMENT,
	`job_type` varchar NOT NULL AUTO_INCREMENT,
	`job_function` varchar NOT NULL AUTO_INCREMENT,
	`job_level` varchar NOT NULL AUTO_INCREMENT,
	`job_location` varchar NOT NULL AUTO_INCREMENT,
	`job_country` varchar(256) NOT NULL AUTO_INCREMENT,
	`job_apply_link` VARCHAR(255) NOT NULL AUTO_INCREMENT,
	`job_date_posted` DATE NOT NULL AUTO_INCREMENT,
	`job_date_created` DATE NOT NULL AUTO_INCREMENT,
	`job_user_created` varchar NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`job_id`,`job_type`)
);

CREATE TABLE `Job_type_Summary` (
	`job_type` varchar NOT NULL
);

CREATE TABLE `Job_seniority_Summary` (

);

CREATE TABLE `Job_title_Summary` (

);

ALTER TABLE `Job_master` ADD CONSTRAINT `Job_master_fk0` FOREIGN KEY (`cmp_id`) REFERENCES `Company_master`(`cmp_id`);

ALTER TABLE `Job_type_Summary` ADD CONSTRAINT `Job_type_Summary_fk0` FOREIGN KEY (`job_type`) REFERENCES `Job_master`(`job_type`);






