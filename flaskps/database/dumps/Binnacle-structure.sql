-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema binnacle
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema binnacle
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `binnacle` DEFAULT CHARACTER SET utf8 ;
USE `binnacle` ;

-- -----------------------------------------------------
-- Table `binnacle`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) GENERATED ALWAYS AS (SUBSTRING(email, 1, LOCATE('@', email) - 1)) VIRTUAL,
  `password` VARCHAR(100) NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NULL,
  `bloqued` VARCHAR(45) NOT NULL DEFAULT 'no',
  `confirmed` VARCHAR(45) NOT NULL DEFAULT 'no',
  `id_city` INT NULL,
  `phone_number` BIGINT(20) UNSIGNED NULL,
  `address` VARCHAR(45) NULL,
  `birthday` DATE NULL,
  `document_number` VARCHAR(45) NULL,
  `id_document_type` INT NULL,
  `photo` varchar(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`role` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`user_role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`user_role` (
  `id_user` INT NOT NULL,
  `id_role` INT NOT NULL,
  PRIMARY KEY (`id_user`, `id_role`),
  INDEX `idrole_idx` (`id_role` ASC),
  CONSTRAINT `fk_user_role_user`
    FOREIGN KEY (`id_user`)
    REFERENCES `binnacle`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_role_role`
    FOREIGN KEY (`id_role`)
    REFERENCES `binnacle`.`role` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `public_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`role_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`role_permission` (
  `id_role` INT NOT NULL,
  `id_permission` INT NOT NULL,
  PRIMARY KEY (`id_role`, `id_permission`),
  INDEX `idpermission_idx` (`id_permission` ASC),
  CONSTRAINT `fk_role_permission_role`
    FOREIGN KEY (`id_role`)
    REFERENCES `binnacle`.`role` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_role_permission_permission`
    FOREIGN KEY (`id_permission`)
    REFERENCES `binnacle`.`permission` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`center`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`center` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `phone_number` VARCHAR(45) NULL,
  `lat` VARCHAR(45) NULL,
  `lng` VARCHAR(45) NULL,

  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `binnacle`.`app_config`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`app_config` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `value` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `binnacle`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`item` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,  
  `description` VARCHAR(255) NULL,
  `id_state` INT NULL,
  `id_user` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `binnacle`.`item_state`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`item_state` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,  
  `description` VARCHAR(255) NULL, 
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `binnacle`.`item_and_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `binnacle`.`item_and_item` (
  `id_item` INT NOT NULL,
  `id_second_item` INT NOT NULL,
  PRIMARY KEY (`id_item`, `id_second_item`),
  INDEX `item_and_item_idx` (`id_second_item` ASC),
  CONSTRAINT `fk_item_and_item`
    FOREIGN KEY (`id_item`)
    REFERENCES `binnacle`.`item` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_and_second_item`
    FOREIGN KEY (`id_second_item`)
    REFERENCES `binnacle`.`item` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
