CREATE SCHEMA IF NOT EXISTS `boilerplate` DEFAULT CHARACTER SET utf8mb4;
USE `boilerplate`;

DROP TABLE IF EXISTS `boilerplate`.`boilerplate`;
CREATE TABLE IF NOT EXISTS `boilerplate`.`boilerplate` (
	`id` INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`id`)
) ENGINE = InnoDB;
