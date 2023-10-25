   -- Script name: inserts.sql
   -- Author:      Amandeep Singh
   -- Purpose:     insert sample data to test the integrity of this database system
   
   -- the database used to insert the data into.
   USE EnergyIndustryDB; 
   
INSERT INTO mailing (MailingId, DeliveryDate, Address) VALUES
(1, '1990-01-01', '123 Alice St'),
(2, '1992-02-15', '456 Bob Rd'),
(3, '2000-05-25', '789 Charlie Ln');

-- Inserts for User table
INSERT INTO User (UserID, Email, FullName, DateOfBirth, Mailing_MailingId) VALUES  
(1, 'alice@email.com', 'Alice Smith', '1990-01-01', 1),
(2, 'bob@email.com', 'Bob Jones', '1992-02-15', 2),
(3, 'charlie@email.com', 'Charlie Brown', '2000-05-25', 3);


-- Inserts for Energy Source table
INSERT INTO `Energy Source` (Capacity, SourceType, SourceName, SourceID, User_UserId) 
VALUES  
(1000, 'Solar', 'Solar Panel A', 1, 1), 
(2000, 'Wind', 'Wind Turbine B', 2, 2), 
(3000, 'Hydro', 'Hydro Dam C', 3, 3);


-- Inserts for Campaign table
INSERT INTO Campaign (Date, TargetAudience, CampaignName, CampaignID) VALUES 
('2023-10-25', 'Adults', 'Save Energy', 1),
('2023-11-05', 'Teens', 'Energy Future', 2),
('2023-12-01', 'Businesses', 'Sustainable Biz', 3);

-- Inserts for Media Outreach table
INSERT INTO `Media Outreach` (ContentType, Platform, CampaignName, Campaign_CampaignId) 
VALUES  
('Video', 1, 'SomeCampaignName1', 1),
('Image', 2, 'SomeCampaignName2', 2),
('Text', 3, 'SomeCampaignName3', 3);


-- Inserts for Feedback table
INSERT INTO Feedback (Rating, FeedbackID, Content) VALUES 
('Excellent', 1, 'Great service!'),
('Good', 2, 'Satisfactory experience.'),
('Poor', 3, 'Could be better.');

-- Inserts for Report table
INSERT INTO Report (Duration, GeneratedDate, ReportType, ReportID, User_UserId) 
VALUES  
(10, '2023-10-24', 'Annual', 1, 1),
(5, '2023-09-24', 'Biannual', 2, 2),
(1, '2023-10-01', 'Monthly', 3, 3);

 -- Inserts for Employee table
INSERT INTO Employee (FullName, Position, EmployeeID) VALUES 
('John Smith', 'Technician', 1),
('Jane Doe', 'Engineer', 2),
('Robert White', 'Manager', 3);

-- Inserts for Partnership table
INSERT INTO Partnership (Duration, StartDate, PartnershipID, PartnerName, Employee_EmployeeId) 
VALUES  
(12, '2023-01-01', 1, 'PartnerCo A', 1),
(6, '2023-06-01', 2, 'PartnerCo B', 2),
(3, '2023-08-01', 3, 'PartnerCo C', 3);

-- Inserts for Inventory table
INSERT INTO Inventory (Quantity, InventoryID, ProductName) 
VALUES  
(100, 1, 'Solar Panel Model X'),
(50, 2, 'Wind Turbine Model Y'),
(75, 3, 'Hydro Dam Model Z');

-- Inserts for Supplier table
INSERT INTO Supplier (SupplierName, SupplierID, ProductType) VALUES 
('Supplier A', 1, 'Solar Panels'),
('Supplier B', 2, 'Wind Turbines'),
('Supplier C', 3, 'Hydro Dams');

-- Inserts for Legal Case table
INSERT INTO `Legal Case` (Status, CaseID, LawyerAssigned) VALUES 
('Open', 1, 'John Doe'),
('Closed', 2, 'Jane Smith'),
('Pending', 3, 'Robert White');

-- Inserts for Research Project table
INSERT INTO `Research Projects` (ProjectID, ProjectName, FundingSource, Dates, Employee_EmployeeId) 
VALUES  
(1, 'Solar Efficiency', 'Govt Grant', '2023-01-01 10:00:00', 1),
(2, 'Wind Dynamics', 'Private Fund', '2023-05-01 11:00:00', 2),
(3, 'Hydro Innovations', 'Research Grant', '2023-09-01 12:00:00', 3);

-- Inserts for Participant Feedback table
INSERT INTO `Participant Feedback` (Comments, Fullname, FeedbackSequence) 
VALUES  
('Great research!', 'Participant A', 1),
('Interesting findings.', 'Participant B', 2),
('More data needed.', 'Participant C', 3);

-- Inserts for Asset table
INSERT INTO Asset (DatePurchased, Value, AssetType, AssetId, User_UserId) VALUES  
('2022-01-01', '10000', 'Solar Panel', 1, 1),
('2021-05-15', '25000', 'Wind Turbine', 2, 2),
('2020-09-20', '50000', 'Hydro Dam', 3, 3);



 -- Inserts for Facility table 
INSERT INTO Facility (UsageType, Size, Location, FacilityID, Asset_AssetId) VALUES  
('Research', 1000, 'Location A', 1, 1),
('Manufacturing', 5000, 'Location B', 2, 2),
('Storage', 3000, 'Location C', 3, 3);


-- Inserts for Training Program table
INSERT INTO `Training Program` (Duration, TrainingID, TrainingName, Facility_FacilityId, Employee_EmployeeId) VALUES  
(5, 1, 'Solar Panel Installation', 1, 1),
(3, 2, 'Wind Turbine Maintenance', 2, 2),
(7, 3, 'Hydro Dam Safety', 3, 3);

-- Inserts for Notification table
INSERT INTO Notification (Content, Frequency, Type, NotificationID) VALUES 
('Maintenance due', 1, 'Alert', 1),
('Training scheduled', 7, 'Reminder', 2),
('New research published', 30, 'Info', 3);

-- Inserts for Billing table
INSERT INTO Billing (PaymentMethod, DueDate, Amount, BillingID) VALUES 
('Credit Card', '2023-11-01', 100.50, 1),
('Bank Transfer', '2023-11-15', 200.25, 2),
('Cash', '2023-12-05', 50.75, 3);

-- Inserts for Data Collection table
INSERT INTO `Data Collection` (IntegrationTypes, ConsumptionValue, Timestamp, CollectionId, User_UserId) 
VALUES  
('API', 500, '2023-10-25 10:30:00', 1, 1),
('Manual', 250, '2023-10-25 11:00:00', 2, 2),
('Batch', 750, '2023-10-25 12:00:00', 3, 3);

-- Inserts for Aviation Analytics table
INSERT INTO `Aviation Anlytics` (AircraftType, FuelCost, Time, `Data Collection_CollectionId`) 
VALUES  
    (747, 5000, '10:00:00', 1), 
    (320, 3000, '08:00:00', 2), 
    (172, 100, '01:00:00', 3);


-- Inserts for Power Metrics table
INSERT INTO `Power Metrics` (InfrastructurePlans, TotalPower, AverageCost, `Data Collection_CollectionId`) 
VALUES (1, 50000, 0.05, 1), 
       (2, 60000, 0.04, 2), 
       (3, 70000, 0.03, 3);

-- Inserts for Billing_has_User       
INSERT INTO Billing_has_User (Billing_BillingId, User_UserId) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserts for Campaign_has_user
INSERT INTO Campaign_has_User (Campaign_CampaignId, User_UserId) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserts for Feedback_has_User
INSERT INTO Feedback_has_User (Feedback_FeedbackId, User_UserId) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserts for Legalcase_has_Employee
INSERT INTO `Legal Case_has_Employee` (`Legal Case_Caseid`, Employee_EmployeeId) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserts for Notification_has_User
INSERT INTO Notification_has_User (Notification_NotificationId, User_UserId) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Inserts for Supplier_has_Inventory
INSERT INTO Supplier_has_Inventory (Supplier_SupplierId, Inventory_InventoryId) VALUES
(1, 1),
(2, 2),
(3, 3);




   