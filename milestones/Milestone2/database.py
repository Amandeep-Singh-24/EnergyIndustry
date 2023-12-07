# In this file you must implement your main query methods
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

# Database configuration
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

# note that your remote host where your database is hosted
# must support user permissions to run stored triggers, procedures and functions.


class Database:

  @staticmethod
  def connect(bot_name):
    """
        Creates a connection with the database.
        """
    try:
      conn = pymysql.connect(host=db_host,
                             user=db_username,
                             password=db_password,
                             db=db_name,
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
      print(f"Bot {bot_name} connected to database {db_name}")
      return conn
    except Exception as err:  # Catching a broader range of exceptions
      print(f"Connection error: {err}")
      return None

  @staticmethod
  def get_response(query, values=None, fetch=False, many_entities=False):
    """
        Executes the given SQL query with provided values.
        """
    response = None
    connection = Database.connect("Bot")
    if connection is None:
      print("Failed to connect to the database.")
      return response

    try:
      with connection.cursor() as cursor:
        cursor.execute(query, values)
        if fetch:
          response = cursor.fetchall() if many_entities else cursor.fetchone()
        else:
          connection.commit()
    except Exception as e:
      print(f"An error occurred: {e}")
    finally:
      if connection:
        connection.close()
    return response

  @staticmethod
  def select(query, values=None):
    """
        Executes a SELECT query.
        """
    return Database.get_response(query, values, fetch=True)

  @staticmethod
  def insert(query, values=None, many_entities=False):
    """
        Executes an INSERT query.
        """
    return Database.get_response(query, values, many_entities=many_entities)

  @staticmethod
  def update(query, values=None):
    """
        Executes an UPDATE query.
        """
    return Database.get_response(query, values)

  @staticmethod
  def delete(query, values=None):
    """
        Executes a DELETE query.
        """
    return Database.get_response(query, values)

  @staticmethod
  def call_procedure(procedure_name, args=()):
    connection = Database.connect("Bot")
    if connection is None:
      return None
    try:
      with connection.cursor() as cursor:
        cursor.callproc(procedure_name, args)
        result = cursor.fetchone()
        return result
    except Exception as e:
      print(f"Procedure execution error: {e}")
    finally:
      if connection:
        connection.close()

  @staticmethod
  def call_function(function_name, args=()):
    connection = Database.connect("Bot")
    if connection is None:
      return None
    try:
      with connection.cursor() as cursor:
        cursor.execute(f"SELECT {function_name}({','.join(['%s']*len(args))})",
                       args)
        result = cursor.fetchone()
        return result
    except Exception as e:
      print(f"Function execution error: {e}")
    finally:
      if connection:
        connection.close()

  @staticmethod
  def create_trigger(trigger_sql):
    return Database.get_response(trigger_sql, fetch=False)


class Query:
  # User Queries
  CREATE_USER = "INSERT INTO User (Email, FullName, DateOfBirth, Mailing_MailingId) VALUES (%s, %s, %s, %s)"
  READ_USER = "SELECT * FROM User WHERE UserID = %s"
  UPDATE_USER = "UPDATE User SET Email = %s, FullName = %s, DateOfBirth = %s WHERE UserID = %s"
  DELETE_USER = "DELETE FROM User WHERE UserID = %s"

  # Employee Queries
  CREATE_EMPLOYEE = "INSERT INTO Employee (FullName, Position, EmployeeID) VALUES (%s, %s, %s)"
  READ_EMPLOYEE = "SELECT * FROM Employee WHERE EmployeeID = %s"
  UPDATE_EMPLOYEE = "UPDATE Employee SET FullName = %s, Position = %s WHERE EmployeeID = %s"
  DELETE_EMPLOYEE = "DELETE FROM Employee WHERE EmployeeID = %s"

  # Energy Source Queries
  CREATE_ENERGY_SOURCE = "INSERT INTO `Energy Source` (Capacity, SourceType, SourceName, User_UserId) VALUES (%s, %s, %s, %s)"
  READ_ENERGY_SOURCE = "SELECT * FROM `Energy Source` WHERE SourceID = %s"
  UPDATE_ENERGY_SOURCE = "UPDATE `Energy Source` SET Capacity = %s, SourceType = %s, SourceName = %s WHERE SourceID = %s"
  DELETE_ENERGY_SOURCE = "DELETE FROM `Energy Source` WHERE SourceID = %s"

  # Campaign Queries
  CREATE_CAMPAIGN = "INSERT INTO Campaign (Date, TargetAudience, CampaignName) VALUES (%s, %s, %s)"
  READ_CAMPAIGN = "SELECT * FROM Campaign WHERE CampaignID = %s"
  UPDATE_CAMPAIGN = "UPDATE Campaign SET Date = %s, TargetAudience = %s, CampaignName = %s WHERE CampaignID = %s"
  DELETE_CAMPAIGN = "DELETE FROM Campaign WHERE CampaignID = %s"

  # Feedback Queries
  CREATE_FEEDBACK = "INSERT INTO Feedback (Rating, Content) VALUES (%s, %s)"
  READ_FEEDBACK = "SELECT * FROM Feedback WHERE FeedbackID = %s"
  UPDATE_FEEDBACK = "UPDATE Feedback SET Rating = %s, Content = %s WHERE FeedbackID = %s"
  DELETE_FEEDBACK = "DELETE FROM Feedback WHERE FeedbackID = %s"

  # Report Queries
  CREATE_REPORT = "INSERT INTO Report (Duration, GeneratedDate, ReportType, User_UserId) VALUES (%s, %s, %s, %s)"
  READ_REPORT = "SELECT * FROM Report WHERE ReportId = %s"
  UPDATE_REPORT = "UPDATE Report SET Duration = %s, GeneratedDate = %s, ReportType = %s WHERE ReportId = %s"
  DELETE_REPORT = "DELETE FROM Report WHERE ReportId = %s"

  # Inventory Queries
  CREATE_INVENTORY = "INSERT INTO Inventory (Quantity, ProductName) VALUES (%s, %s)"
  READ_INVENTORY = "SELECT * FROM Inventory WHERE InventoryId = %s"
  UPDATE_INVENTORY = "UPDATE Inventory SET Quantity = %s, ProductName = %s WHERE InventoryId = %s"
  DELETE_INVENTORY = "DELETE FROM Inventory WHERE InventoryId = %s"

  # Supplier Queries
  CREATE_SUPPLIER = "INSERT INTO Supplier (SupplierName, ProductType) VALUES (%s, %s)"
  READ_SUPPLIER = "SELECT * FROM Supplier WHERE SupplierId = %s"
  UPDATE_SUPPLIER = "UPDATE Supplier SET SupplierName = %s, ProductType = %s WHERE SupplierId = %s"
  DELETE_SUPPLIER = "DELETE FROM Supplier WHERE SupplierId = %s"

  # Research Project Queries
  CREATE_RESEARCH_PROJECT = "INSERT INTO `Research Projects` (ProjectName, FundingSource, Dates, Employee_EmployeeId) VALUES (%s, %s, %s, %s)"
  READ_RESEARCH_PROJECT = "SELECT * FROM `Research Projects` WHERE ProjectId = %s"
  UPDATE_RESEARCH_PROJECT = "UPDATE `Research Projects` SET ProjectName = %s, FundingSource = %s, Dates = %s WHERE ProjectId = %s"
  DELETE_RESEARCH_PROJECT = "DELETE FROM `Research Projects` WHERE ProjectId = %s"

  # Legal Case Queries
  CREATE_LEGAL_CASE = "INSERT INTO `Legal Case` (Status, LawyerAssigned) VALUES (%s, %s)"
  READ_LEGAL_CASE = "SELECT * FROM `Legal Case` WHERE Caseid = %s"
  UPDATE_LEGAL_CASE = "UPDATE `Legal Case` SET Status = %s, LawyerAssigned = %s WHERE Caseid = %s"
  DELETE_LEGAL_CASE = "DELETE FROM `Legal Case` WHERE Caseid = %s"

  # Participant Feedback Queries
  CREATE_PARTICIPANT_FEEDBACK = "INSERT INTO `Participant Feedback` (Comments, FullName) VALUES (%s, %s)"
  READ_PARTICIPANT_FEEDBACK = "SELECT * FROM `Participant Feedback` WHERE FeedbackSequence = %s"
  UPDATE_PARTICIPANT_FEEDBACK = "UPDATE `Participant Feedback` SET Comments = %s, FullName = %s WHERE   FeedbackSequence = %s"
  DELETE_PARTICIPANT_FEEDBACK = "DELETE FROM `Participant Feedback` WHERE FeedbackSequence = %s"

  # Asset Queries
  CREATE_ASSET = "INSERT INTO Asset (AssetType, Value, DatePurchased, User_UserId) VALUES (%s, %s, %s, %s)"
  READ_ASSET = "SELECT * FROM Asset WHERE AssetId = %s"
  UPDATE_ASSET = "UPDATE Asset SET AssetType = %s, Value = %s, DatePurchased = %s WHERE AssetId = %s"
  DELETE_ASSET = "DELETE FROM Asset WHERE AssetId = %s"

  # Facility Queries
  CREATE_FACILITY = "INSERT INTO Facility (Size, Location, UsageType, Asset_AssetId) VALUES (%s, %s, %s, %s)"
  READ_FACILITY = "SELECT * FROM Facility WHERE FacilityId = %s"
  UPDATE_FACILITY = "UPDATE Facility SET Size = %s, Location = %s, UsageType = %s WHERE FacilityId = %s"
  DELETE_FACILITY = "DELETE FROM Facility WHERE FacilityId = %s"

  # Training Program Queries
  CREATE_TRAINING_PROGRAM = "INSERT INTO `Training Program` (TrainingName, Duration, Facility_FacilityId, Employee_EmployeeId) VALUES (%s, %s, %s, %s)"
  READ_TRAINING_PROGRAM = "SELECT * FROM `Training Program` WHERE TrainingId = %s"
  UPDATE_TRAINING_PROGRAM = "UPDATE `Training Program` SET TrainingName = %s, Duration = %s WHERE TrainingId = %s"
  DELETE_TRAINING_PROGRAM = "DELETE FROM `Training Program` WHERE Employee_EmployeeId = %s"

  # Notification Queries
  CREATE_NOTIFICATION = "INSERT INTO Notification (Content, Frequency, Type) VALUES (%s, %s, %s)"
  READ_NOTIFICATION = "SELECT * FROM Notification WHERE NotificationId = %s"
  UPDATE_NOTIFICATION = "UPDATE Notification SET Content = %s, Frequency = %s, Type = %s WHERE NotificationId = %s"
  DELETE_NOTIFICATION = "DELETE FROM Notification WHERE NotificationId = %s"

  # Billing Queries
  CREATE_BILLING = "INSERT INTO Billing (PaymentMethod, DueDate, Amount) VALUES (%s, %s, %s)"
  READ_BILLING = "SELECT * FROM Billing WHERE Billingid = %s"
  UPDATE_BILLING = "UPDATE Billing SET PaymentMethod = %s, DueDate = %s, Amount = %s WHERE Billingid = %s"
  DELETE_BILLING = "DELETE FROM Billing WHERE Billingid = %s"

  # Data Collection Queries
  CREATE_DATA_COLLECTION = "INSERT INTO `Data Collection` (Timestamp, ConsumptionValue, IntegrationTypes, User_UserId) VALUES (%s, %s, %s, %s)"
  READ_DATA_COLLECTION = "SELECT * FROM `Data Collection` WHERE CollectionId = %s"
  UPDATE_DATA_COLLECTION = "UPDATE `Data Collection` SET Timestamp = %s, ConsumptionValue = %s, IntegrationTypes = %s WHERE CollectionId = %s"
  DELETE_DATA_COLLECTION = "DELETE FROM `Data Collection` WHERE CollectionId = %s"

  # Aviation Analytics Queries
  CREATE_AVIATION_ANALYTICS = "INSERT INTO `Aviation Analytics` (AircraftType, FuelCost, Time, `Data Collection_CollectionId`) VALUES (%s, %s, %s, %s)"
  READ_AVIATION_ANALYTICS = "SELECT * FROM `Aviation Analytics` WHERE AircraftType = %s"
  UPDATE_AVIATION_ANALYTICS = "UPDATE `Aviation Analytics` SET FuelCost = %s, Time = %s WHERE AircraftType = %s"
  DELETE_AVIATION_ANALYTICS = "DELETE FROM `Aviation Analytics` WHERE AircraftType = %s"

  # Power Metrics Queries
  CREATE_POWER_METRICS = "INSERT INTO `Power Metrics` (InfrastructurePlans, TotalPower, AverageCost, `Data Collection_CollectionId`) VALUES (%s, %s, %s, %s)"
  READ_POWER_METRICS = "SELECT * FROM `Power Metrics` WHERE InfrastructurePlans = %s"
  UPDATE_POWER_METRICS = "UPDATE `Power Metrics` SET TotalPower = %s, AverageCost = %s WHERE InfrastructurePlans = %s"
  DELETE_POWER_METRICS = "DELETE FROM `Power Metrics` WHERE InfrastructurePlans = %s"

  # Media Outreach Queries
  CREATE_MEDIA_OUTREACH = "INSERT INTO `Media Outreach` (Platform, ContentType, CampaignName, Campaign_CampaignId) VALUES (%s, %s, %s, %s)"
  READ_MEDIA_OUTREACH = "SELECT * FROM `Media Outreach` WHERE Platform = %s"
  UPDATE_MEDIA_OUTREACH = "UPDATE `Media Outreach` SET ContentType = %s, CampaignName = %s WHERE Platform = %s"
  DELETE_MEDIA_OUTREACH = "DELETE FROM `Media Outreach` WHERE Platform = %s"

  # Mailing Queries
  CREATE_MAILING = "INSERT INTO Mailing (Address, DeliveryDate) VALUES (%s, %s)"
  READ_MAILING = "SELECT * FROM Mailing WHERE MailingId = %s"
  UPDATE_MAILING = "UPDATE Mailing SET Address = %s, DeliveryDate = %s WHERE MailingId = %s"
  DELETE_MAILING = "DELETE FROM Mailing WHERE MailingId = %s"

  # Partnership Queries
  CREATE_PARTNERSHIP = "INSERT INTO Partnership (Duration, StartDate, PartnerName, Employee_EmployeeId) VALUES (%s, %s, %s, %s)"
  READ_PARTNERSHIP = "SELECT * FROM Partnership WHERE PartnershipId = %s"
  UPDATE_PARTNERSHIP = "UPDATE Partnership SET Duration = %s, StartDate = %s, PartnerName = %s WHERE PartnershipId = %s"
  DELETE_PARTNERSHIP = "DELETE FROM Partnership WHERE PartnershipId = %s"

  # Data Retrieval Queries
  SUMMARY_REPORT_ENERGY_PRODUCTION = """
    SELECT SourceType, SUM(Capacity) as TotalCapacity, AVG(Capacity) as AverageCapacity
    FROM `Energy Source`
    WHERE Capacity > %s
    GROUP BY SourceType
"""
  USERS_FEEDBACK_RATINGS = """
    SELECT U.UserID, U.FullName, F.Rating
    FROM User U
    JOIN `Energy Source` E ON U.UserID = E.User_UserId
    JOIN Feedback_has_User FU ON U.UserID = FU.User_UserId
    JOIN Feedback F ON FU.Feedback_FeedbackId = F.FeedbackId
    WHERE E.SourceType = %s
"""
  DETAILED_REPORT_PARTNERSHIPS = """
    SELECT P.PartnerName, E.FullName, E.Position
    FROM Partnership P
    JOIN Employee E ON P.Employee_EmployeeId = E.EmployeeID
    WHERE P.Duration > %s
"""
  LEGAL_CASES_STATUS = """
    SELECT LC.Caseid, LC.LawyerAssigned, E.FullName
    FROM `Legal Case` LC
    JOIN `Legal Case_has_Employee` LCE ON LC.Caseid = LCE.`Legal Case_Caseid`
    JOIN Employee E ON LCE.Employee_EmployeeId = E.EmployeeID
    WHERE LC.Status = %s
"""

  # Data Insertion Queries
  INSERT_EMPLOYEE_AND_TRAINING = """
    INSERT INTO Employee (FullName, Position) VALUES (%s, %s);
    INSERT INTO `Training Program` (TrainingName, Duration, Facility_FacilityId, Employee_EmployeeId)
    VALUES (%s, %s, %s, LAST_INSERT_ID());
"""
  INSERT_ASSET_AND_FACILITY = """
    INSERT INTO Asset (AssetType, Value, DatePurchased, User_UserId) VALUES (%s, %s, %s, %s);
    INSERT INTO Facility (Size, Location, UsageType, Asset_AssetId) VALUES (%s, %s, %s, LAST_INSERT_ID());
  """


  # Data Update Queries
  UPDATE_USER_CONTACT_AND_MAILING = """
    UPDATE User SET ContactInfo = %s WHERE UserID = %s;
    UPDATE Mailing SET Address = %s WHERE MailingId = (SELECT Mailing_MailingId FROM User WHERE UserID = %s);
"""
  UPDATE_CAMPAIGN_AND_MEDIA_OUTREACH = """
    UPDATE Campaign SET CampaignName = %s, TargetAudience = %s WHERE CampaignId = %s;
    UPDATE `Media Outreach` SET CampaignName = %s WHERE Campaign_CampaignId = %s;
"""
  # New queries
  UPDATE_USER_EMAIL_AND_MAILING = """
      UPDATE User SET Email = %s WHERE UserID = %s;
      UPDATE Mailing SET MailingId = %s WHERE MailingId = (SELECT Mailing_MailingId FROM User WHERE UserID = %s);
  """

  INSERT_ASSET_AND_FACILITY = """
      INSERT INTO Asset (AssetType, Value, DatePurchased, User_UserId) VALUES (%s, %s, %s, %s);
      INSERT INTO Facility (Size, Location, UsageType, Asset_AssetId) VALUES (%s, %s, %s, LAST_INSERT_ID());
  """

  # Data Deletion Queries
  DELETE_SUPPLIER_AND_INVENTORY = """
    DELETE FROM Inventory WHERE InventoryId IN (SELECT Inventory_InventoryId FROM Supplier_has_Inventory WHERE Supplier_SupplierId = %s);
    DELETE FROM Supplier WHERE SupplierId = %s;
"""
  DELETE_EMPLOYEE_AND_TRAINING = """
    DELETE FROM `Training Program` WHERE Employee_EmployeeId = %s;
    DELETE FROM Employee WHERE EmployeeID = %s;
"""

  # Stored SQL Components
  TRIGGER_ENERGY_SOURCE_AUDIT = """
    CREATE TRIGGER IF NOT EXISTS energy_source_audit
    AFTER INSERT ON `Energy Source`
    FOR EACH ROW
    BEGIN
        INSERT INTO energy_source_audit_table (source_id, new_capacity, action_type, action_timestamp)
        VALUES (NEW.SourceId, NEW.Capacity, 'INSERT', NOW());
    END;
"""
  TRIGGER_BACKUP_USER_DATA = """
    CREATE TRIGGER IF NOT EXISTS backup_user_data
    BEFORE DELETE ON User
    FOR EACH ROW
    BEGIN
        INSERT INTO user_backup_table (user_id, email, full_name, date_of_birth)
        VALUES (OLD.UserId, OLD.Email, OLD.FullName, OLD.DateOfBirth);
    END;
"""
  PROCEDURE_AVERAGE_ENERGY_CONSUMPTION = """
    CREATE PROCEDURE calculate_average_energy_consumption(IN energy_type VARCHAR(255))
    BEGIN
        SELECT AVG(Capacity) AS average_capacity
        FROM `Energy Source`
        WHERE SourceType = energy_type;
    END;
"""
  FUNCTION_NEXT_ENERGY_SOURCE_ID = """
    CREATE FUNCTION get_next_energy_source_id()
    RETURNS INT DETERMINISTIC
    BEGIN
        DECLARE next_id INT;
        SELECT MAX(SourceId) + 1 INTO next_id FROM `Energy Source`;
        RETURN next_id;
    END;
"""
  FUNCTION_TOTAL_PROJECT_COST = """
    CREATE FUNCTION calculate_total_project_cost(employee_id INT)
    RETURNS DECIMAL(10,2)
    BEGIN
        DECLARE total_cost DECIMAL(10,2);
        SELECT SUM(Cost) INTO total_cost 
        FROM projects 
        WHERE employee_id = employee_id;
        RETURN total_cost;
    END;
"""
