-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema EnergyIndustryDB
-- -----------------------------------------------------
DROP DATABASE IF EXISTS EnergyIndustryDB; 

CREATE DATABASE IF NOT EXISTS EnergyIndustryDB; 

USE EnergyIndustryDB;
-- -----------------------------------------------------
-- Table `Mailing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mailing` ;

CREATE TABLE IF NOT EXISTS `Mailing` (
  `MailingId` INT NOT NULL AUTO_INCREMENT,
  `Address` VARCHAR(255) NOT NULL,
  `DeliveryDate` DATETIME NOT NULL,
  PRIMARY KEY (`MailingId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Employee`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Employee` ;

CREATE TABLE IF NOT EXISTS `Employee` (
  `EmployeeId` INT NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(255) NOT NULL,
  `Position` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`EmployeeId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Partnership`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Partnership` ;

CREATE TABLE IF NOT EXISTS `Partnership` (
  `PartnershipId` INT NOT NULL AUTO_INCREMENT,
  `Duration` DECIMAL(10,2) NOT NULL,
  `StartDate` DATE NOT NULL,
  `PartnerName` VARCHAR(255) NOT NULL,
  `Employee_EmployeeId` INT NOT NULL,
  PRIMARY KEY (`PartnershipId`),
  INDEX `fk_Partnership_Employee1_idx` (`Employee_EmployeeId` ASC) VISIBLE,
  CONSTRAINT `fk_Partnership_Employee1`
    FOREIGN KEY (`Employee_EmployeeId`)
    REFERENCES `Employee` (`EmployeeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `User` ;

CREATE TABLE IF NOT EXISTS `User` (
  `UserId` INT NOT NULL AUTO_INCREMENT,
  `Email` VARCHAR(255) NOT NULL,
  `FullName` VARCHAR(255) NOT NULL,
  `DateOfBirth` DATE NOT NULL,
  `Mailing_MailingId` INT NOT NULL,
  `Partnership_PartnershipId` INT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  INDEX `fk_User_Mailing1_idx` (`Mailing_MailingId` ASC) VISIBLE,
  INDEX `fk_User_Partnership1_idx` (`Partnership_PartnershipId` ASC) VISIBLE,
  CONSTRAINT `fk_User_Mailing1`
    FOREIGN KEY (`Mailing_MailingId`)
    REFERENCES `Mailing` (`MailingId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Partnership1`
    FOREIGN KEY (`Partnership_PartnershipId`)
    REFERENCES `Partnership` (`PartnershipId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Energy Source`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Energy Source` ;

CREATE TABLE IF NOT EXISTS `Energy Source` (
  `SourceId` INT NOT NULL AUTO_INCREMENT,
  `Capacity` DECIMAL(20,5) NOT NULL,
  `SourceType` VARCHAR(255) NOT NULL,
  `SourceName` VARCHAR(255) NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`SourceId`),
  INDEX `fk_Energy Source_User_idx` (`User_UserId` ASC) VISIBLE,
  CONSTRAINT `fk_Energy Source_User`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Campaign`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Campaign` ;

CREATE TABLE IF NOT EXISTS `Campaign` (
  `CampaignId` INT NOT NULL AUTO_INCREMENT,
  `Date` DATE NOT NULL,
  `TargetAudience` VARCHAR(255) NOT NULL,
  `CampaignName` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`CampaignId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Media Outreach`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Media Outreach` ;

CREATE TABLE IF NOT EXISTS `Media Outreach` (
  `Platform` INT NOT NULL AUTO_INCREMENT,
  `ContentType` VARCHAR(45) NOT NULL,
  `CampaignName` VARCHAR(45) NOT NULL,
  `Campaign_CampaignId` INT NOT NULL,
  PRIMARY KEY (`Platform`, `Campaign_CampaignId`),
  INDEX `fk_Media Outreach_Campaign1_idx` (`Campaign_CampaignId` ASC) VISIBLE,
  CONSTRAINT `fk_Media Outreach_Campaign1`
    FOREIGN KEY (`Campaign_CampaignId`)
    REFERENCES `Campaign` (`CampaignId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Feedback` ;

CREATE TABLE IF NOT EXISTS `Feedback` (
  `FeedbackId` INT NOT NULL AUTO_INCREMENT,
  `Rating` VARCHAR(255) NOT NULL,
  `Content` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`FeedbackId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Report`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Report` ;

CREATE TABLE IF NOT EXISTS `Report` (
  `ReportId` INT NOT NULL AUTO_INCREMENT,
  `Duration` DECIMAL(10,2) NOT NULL,
  `ReportType` VARCHAR(255) NOT NULL,
  `GeneratedDate` DATE NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`ReportId`),
  INDEX `fk_Report_User1_idx` (`User_UserId` ASC) VISIBLE,
  CONSTRAINT `fk_Report_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Inventory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Inventory` ;

CREATE TABLE IF NOT EXISTS `Inventory` (
  `InventoryId` INT NOT NULL AUTO_INCREMENT,
  `ProductName` VARCHAR(255) NOT NULL,
  `Quantity` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`InventoryId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Supplier`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Supplier` ;

CREATE TABLE IF NOT EXISTS `Supplier` (
  `SupplierId` INT NOT NULL AUTO_INCREMENT,
  `SupplierName` VARCHAR(255) NOT NULL,
  `ProductType` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`SupplierId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Research Projects`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Research Projects` ;

CREATE TABLE IF NOT EXISTS `Research Projects` (
  `ProjectId` INT NOT NULL AUTO_INCREMENT,
  `ProjectName` VARCHAR(255) NOT NULL,
  `FundingSource` VARCHAR(255) NOT NULL,
  `Dates` DATETIME NOT NULL,
  `Partnership_PartnershipId` INT NULL,
  `Employee_EmployeeId` INT NOT NULL,
  PRIMARY KEY (`ProjectId`),
  INDEX `fk_Research Projects_Partnership1_idx` (`Partnership_PartnershipId` ASC) VISIBLE,
  INDEX `fk_Research Projects_Employee1_idx` (`Employee_EmployeeId` ASC) VISIBLE,
  CONSTRAINT `fk_Research Projects_Partnership1`
    FOREIGN KEY (`Partnership_PartnershipId`)
    REFERENCES `Partnership` (`PartnershipId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Research Projects_Employee1`
    FOREIGN KEY (`Employee_EmployeeId`)
    REFERENCES `Employee` (`EmployeeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Legal Case`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Legal Case` ;

CREATE TABLE IF NOT EXISTS `Legal Case` (
  `Caseid` INT NOT NULL AUTO_INCREMENT,
  `LawyerAssigned` VARCHAR(255) NOT NULL,
  `Status` VARCHAR(255) NOT NULL,
  `Research Projects_ProjectId` INT NULL,
  PRIMARY KEY (`Caseid`),
  INDEX `fk_Legal Case_Research Projects1_idx` (`Research Projects_ProjectId` ASC) VISIBLE,
  CONSTRAINT `fk_Legal Case_Research Projects1`
    FOREIGN KEY (`Research Projects_ProjectId`)
    REFERENCES `Research Projects` (`ProjectId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Participant Feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Participant Feedback` ;

CREATE TABLE IF NOT EXISTS `Participant Feedback` (
  `FeedbackSequence` INT NOT NULL,
  `FullName` VARCHAR(255) NOT NULL,
  `Comments` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`FeedbackSequence`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Asset`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Asset` ;

CREATE TABLE IF NOT EXISTS `Asset` (
  `AssetId` INT NOT NULL AUTO_INCREMENT,
  `AssetType` VARCHAR(255) NOT NULL,
  `Value` DECIMAL(15,2) NOT NULL,
  `DatePurchased` DATE NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`AssetId`),
  INDEX `fk_Asset_User1_idx` (`User_UserId` ASC) VISIBLE,
  CONSTRAINT `fk_Asset_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Facility`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Facility` ;

CREATE TABLE IF NOT EXISTS `Facility` (
  `FacilityId` INT NOT NULL AUTO_INCREMENT,
  `Size` DECIMAL(10,2) NOT NULL,
  `Location` VARCHAR(255) NOT NULL,
  `UsageType` VARCHAR(255) NOT NULL,
  `Asset_AssetId` INT NOT NULL,
  PRIMARY KEY (`FacilityId`),
  INDEX `fk_Facility_Asset1_idx` (`Asset_AssetId` ASC) VISIBLE,
  CONSTRAINT `fk_Facility_Asset1`
    FOREIGN KEY (`Asset_AssetId`)
    REFERENCES `Asset` (`AssetId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Training Program`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Training Program` ;

CREATE TABLE IF NOT EXISTS `Training Program` (
  `TrainingId` INT NOT NULL AUTO_INCREMENT,
  `TrainingName` VARCHAR(255) NOT NULL,
  `Duration` DECIMAL(10,2) NOT NULL,
  `Facility_FacilityId` INT NOT NULL,
  `Employee_EmployeeId` INT NOT NULL,
  PRIMARY KEY (`TrainingId`),
  INDEX `fk_Training Program_Facility1_idx` (`Facility_FacilityId` ASC) VISIBLE,
  INDEX `fk_Training Program_Employee1_idx` (`Employee_EmployeeId` ASC) VISIBLE,
  CONSTRAINT `fk_Training Program_Facility1`
    FOREIGN KEY (`Facility_FacilityId`)
    REFERENCES `Facility` (`FacilityId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Training Program_Employee1`
    FOREIGN KEY (`Employee_EmployeeId`)
    REFERENCES `Employee` (`EmployeeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Notification`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Notification` ;

CREATE TABLE IF NOT EXISTS `Notification` (
  `NotificationId` INT NOT NULL AUTO_INCREMENT,
  `Content` VARCHAR(255) NOT NULL,
  `Frequency` INT NOT NULL,
  `Type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`NotificationId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Billing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Billing` ;

CREATE TABLE IF NOT EXISTS `Billing` (
  `Billingid` INT NOT NULL AUTO_INCREMENT,
  `PaymentMethod` VARCHAR(255) NOT NULL,
  `DueDate` DATE NOT NULL,
  `Amount` DECIMAL(15,2) NOT NULL,
  PRIMARY KEY (`Billingid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Data Collection`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Data Collection` ;

CREATE TABLE IF NOT EXISTS `Data Collection` (
  `CollectionId` INT NOT NULL AUTO_INCREMENT,
  `Timestamp` DATETIME NOT NULL,
  `ConsumptionValue` DECIMAL(15,2) NOT NULL,
  `IntegrationTypes` VARCHAR(255) NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`CollectionId`),
  INDEX `fk_Data Collection_User1_idx` (`User_UserId` ASC) VISIBLE,
  CONSTRAINT `fk_Data Collection_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Aviation Anlytics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aviation Anlytics` ;

CREATE TABLE IF NOT EXISTS `Aviation Anlytics` (
  `AircraftType` INT NOT NULL AUTO_INCREMENT,
  `FuelCost` DECIMAL(15,2) NOT NULL,
  `Time` VARCHAR(45) NOT NULL,
  `Data Collection_CollectionId` INT NOT NULL,
  PRIMARY KEY (`AircraftType`, `Data Collection_CollectionId`),
  INDEX `fk_Aviation Anlytics_Data Collection1_idx` (`Data Collection_CollectionId` ASC) VISIBLE,
  CONSTRAINT `fk_Aviation Anlytics_Data Collection1`
    FOREIGN KEY (`Data Collection_CollectionId`)
    REFERENCES `Data Collection` (`CollectionId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Power Metrics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Power Metrics` ;

CREATE TABLE IF NOT EXISTS `Power Metrics` (
  `InfrastructurePlans` INT NOT NULL AUTO_INCREMENT,
  `TotalPower` DECIMAL(15,2) NOT NULL,
  `AverageCost` DECIMAL(15,2) NOT NULL,
  `Data Collection_CollectionId` INT NOT NULL,
  PRIMARY KEY (`InfrastructurePlans`, `Data Collection_CollectionId`),
  INDEX `fk_Power Metrics_Data Collection1_idx` (`Data Collection_CollectionId` ASC) VISIBLE,
  CONSTRAINT `fk_Power Metrics_Data Collection1`
    FOREIGN KEY (`Data Collection_CollectionId`)
    REFERENCES `Data Collection` (`CollectionId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Campaign_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Campaign_has_User` ;

CREATE TABLE IF NOT EXISTS `Campaign_has_User` (
  `Campaign_CampaignId` INT NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`Campaign_CampaignId`, `User_UserId`),
  INDEX `fk_Campaign_has_User_User1_idx` (`User_UserId` ASC) VISIBLE,
  INDEX `fk_Campaign_has_User_Campaign1_idx` (`Campaign_CampaignId` ASC) VISIBLE,
  CONSTRAINT `fk_Campaign_has_User_Campaign1`
    FOREIGN KEY (`Campaign_CampaignId`)
    REFERENCES `Campaign` (`CampaignId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Campaign_has_User_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Billing_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Billing_has_User` ;

CREATE TABLE IF NOT EXISTS `Billing_has_User` (
  `Billing_Billingid` INT NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`Billing_Billingid`, `User_UserId`),
  INDEX `fk_Billing_has_User_User1_idx` (`User_UserId` ASC) VISIBLE,
  INDEX `fk_Billing_has_User_Billing1_idx` (`Billing_Billingid` ASC) VISIBLE,
  CONSTRAINT `fk_Billing_has_User_Billing1`
    FOREIGN KEY (`Billing_Billingid`)
    REFERENCES `Billing` (`Billingid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Billing_has_User_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Notification_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Notification_has_User` ;

CREATE TABLE IF NOT EXISTS `Notification_has_User` (
  `Notification_NotificationId` INT NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`Notification_NotificationId`, `User_UserId`),
  INDEX `fk_Notification_has_User_User1_idx` (`User_UserId` ASC) VISIBLE,
  INDEX `fk_Notification_has_User_Notification1_idx` (`Notification_NotificationId` ASC) VISIBLE,
  CONSTRAINT `fk_Notification_has_User_Notification1`
    FOREIGN KEY (`Notification_NotificationId`)
    REFERENCES `Notification` (`NotificationId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notification_has_User_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table `Feedback_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Feedback_has_User` ;

CREATE TABLE IF NOT EXISTS `Feedback_has_User` (
  `Feedback_FeedbackId` INT NOT NULL,
  `User_UserId` INT NOT NULL,
  PRIMARY KEY (`Feedback_FeedbackId`, `User_UserId`),
  INDEX `fk_Feedback_has_User_User1_idx` (`User_UserId` ASC) VISIBLE,
  INDEX `fk_Feedback_has_User_Feedback1_idx` (`Feedback_FeedbackId` ASC) VISIBLE,
  CONSTRAINT `fk_Feedback_has_User_Feedback1`
    FOREIGN KEY (`Feedback_FeedbackId`)
    REFERENCES `Feedback` (`FeedbackId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Feedback_has_User_User1`
    FOREIGN KEY (`User_UserId`)
    REFERENCES `User` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Supplier_has_Inventory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Supplier_has_Inventory` ;

CREATE TABLE IF NOT EXISTS `Supplier_has_Inventory` (
  `Supplier_SupplierId` INT NOT NULL,
  `Inventory_InventoryId` INT NOT NULL,
  PRIMARY KEY (`Supplier_SupplierId`, `Inventory_InventoryId`),
  INDEX `fk_Supplier_has_Inventory_Inventory1_idx` (`Inventory_InventoryId` ASC) VISIBLE,
  INDEX `fk_Supplier_has_Inventory_Supplier1_idx` (`Supplier_SupplierId` ASC) VISIBLE,
  CONSTRAINT `fk_Supplier_has_Inventory_Supplier1`
    FOREIGN KEY (`Supplier_SupplierId`)
    REFERENCES `Supplier` (`SupplierId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Supplier_has_Inventory_Inventory1`
    FOREIGN KEY (`Inventory_InventoryId`)
    REFERENCES `Inventory` (`InventoryId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Legal Case_has_Employee`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Legal Case_has_Employee` ;

CREATE TABLE IF NOT EXISTS `Legal Case_has_Employee` (
  `Legal Case_Caseid` INT NOT NULL,
  `Employee_EmployeeId` INT NOT NULL,
  PRIMARY KEY (`Legal Case_Caseid`, `Employee_EmployeeId`),
  INDEX `fk_Legal Case_has_Employee_Employee1_idx` (`Employee_EmployeeId` ASC) VISIBLE,
  INDEX `fk_Legal Case_has_Employee_Legal Case1_idx` (`Legal Case_Caseid` ASC) VISIBLE,
  CONSTRAINT `fk_Legal Case_has_Employee_Legal Case1`
    FOREIGN KEY (`Legal Case_Caseid`)
    REFERENCES `Legal Case` (`Caseid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Legal Case_has_Employee_Employee1`
    FOREIGN KEY (`Employee_EmployeeId`)
    REFERENCES `Employee` (`EmployeeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Participant Feedback_has_Training Program`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Participant Feedback_has_Training Program` ;

CREATE TABLE IF NOT EXISTS `Participant Feedback_has_Training Program` (
  `Participant Feedback_FeedbackSequence` INT NOT NULL,
  `Training Program_TrainingId` INT NOT NULL,
  PRIMARY KEY (`Participant Feedback_FeedbackSequence`, `Training Program_TrainingId`),
  INDEX `fk_Participant Feedback_has_Training Program_Training Progr_idx` (`Training Program_TrainingId` ASC) VISIBLE,
  INDEX `fk_Participant Feedback_has_Training Program_Participant Fe_idx` (`Participant Feedback_FeedbackSequence` ASC) VISIBLE,
  CONSTRAINT `fk_Participant Feedback_has_Training Program_Participant Feed1`
    FOREIGN KEY (`Participant Feedback_FeedbackSequence`)
    REFERENCES `Participant Feedback` (`FeedbackSequence`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participant Feedback_has_Training Program_Training Program1`
    FOREIGN KEY (`Training Program_TrainingId`)
    REFERENCES `Training Program` (`TrainingId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Supervisor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Supervisor` ;

CREATE TABLE IF NOT EXISTS `Supervisor` (
  `Supervisor` VARCHAR(45) NOT NULL,
  `Employee_EmployeeId` INT NOT NULL,
  PRIMARY KEY (`Supervisor`, `Employee_EmployeeId`),
  INDEX `fk_Supervisor_Employee1_idx` (`Employee_EmployeeId` ASC) VISIBLE,
  CONSTRAINT `fk_Supervisor_Employee1`
    FOREIGN KEY (`Employee_EmployeeId`)
    REFERENCES `Employee` (`EmployeeId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
