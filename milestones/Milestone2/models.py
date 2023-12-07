"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""

from database import Database
from database import Query


class TestModel:
  """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

  def __init__(self, ctx):
    self.ctx = ctx
    self.author = ctx.message.author.name

  def response(self):
    return f'Hi, {self.author}. I am alive'


class UserModel:

  def __init__(self, user_id=None):
    self.user_id = user_id

  def create_user(self, email, full_name, date_of_birth, mailing_id):
    return Database.insert(Query.CREATE_USER,
                           (email, full_name, date_of_birth, mailing_id))

  def read_user(self):
    return Database.select(Query.READ_USER, (self.user_id, ))

  def update_user(self, email, full_name, date_of_birth):
    return Database.update(Query.UPDATE_USER,
                           (email, full_name, date_of_birth, self.user_id))

  def delete_user(self):
    return Database.delete(Query.DELETE_USER, (self.user_id, ))

  @staticmethod
  def users_feedback(energy_source):
      query = Query.USERS_FEEDBACK_RATINGS
      data = Database.select(query, (energy_source,))

      if not data or not isinstance(data, list):
          return "No feedback found for the specified energy source."

      formatted_response = ""
      for record in data:
          if isinstance(record, dict) and 'FullName' in record and 'Rating' in record:
              formatted_response += f"User: {record['FullName']}, Rating: {record['Rating']}\n"
          else:
              return "Unexpected data format received from the database."

      return formatted_response.strip()

  @staticmethod
  def update_contact_and_mailing(user_id, new_email, new_mailing_id):
      Database.update(Query.UPDATE_USER_EMAIL_AND_MAILING, (new_email, user_id, new_mailing_id, user_id))
      return "User contact and mailing information updated successfully."

class EmployeeModel:

  def __init__(self, employee_id=None):
    self.employee_id = employee_id

  def create_employee(self, name, position):
    return Database.insert(Query.CREATE_EMPLOYEE, (name, position))

  def read_employee(self):
    return Database.select(Query.READ_EMPLOYEE, (self.employee_id, ))

  def update_employee(self, name, position):
    return Database.update(Query.UPDATE_EMPLOYEE,
                           (name, position, self.employee_id))

  def delete_employee(self):
    return Database.delete(Query.DELETE_EMPLOYEE, (self.employee_id, ))

  @staticmethod
  def insert_employee_and_training(name, position, training_name, duration, facility_id):
      query = Query.INSERT_EMPLOYEE_AND_TRAINING
      result = Database.insert(query, (name, position, training_name, duration, facility_id))

      if result:
          return f"Employee '{name}' with position '{position}' and training '{training_name}' successfully added."
      else:
          return "Failed to insert employee and training data."

  @staticmethod
  def delete_employee_and_training(employee_id):
    # Delete training programs associated with the employee
    Database.delete(Query.DELETE_TRAINING_PROGRAM, (employee_id,))

    # Delete the employee record
    return Database.delete(Query.DELETE_EMPLOYEE, (employee_id,))

  


class EnergySourceModel:

  def __init__(self, source_id=None):
    self.source_id = source_id

  def create_energy_source(self, capacity, source_type, source_name, user_id):
    return Database.insert(Query.CREATE_ENERGY_SOURCE,
                           (capacity, source_type, source_name, user_id))

  def read_energy_source(self):
    return Database.select(Query.READ_ENERGY_SOURCE, (self.source_id, ))

  def update_energy_source(self, capacity, source_type, source_name):
    return Database.update(
        Query.UPDATE_ENERGY_SOURCE,
        (capacity, source_type, source_name, self.source_id))

  def delete_energy_source(self):
    return Database.delete(Query.DELETE_ENERGY_SOURCE, (self.source_id, ))

  @staticmethod
  def summary_report(threshold):
    query = Query.SUMMARY_REPORT_ENERGY_PRODUCTION
    data = Database.select(query, (threshold, ))

    # Check if data is not empty and is a list
    if not data or not isinstance(data, list):
      return "No data found for the specified threshold."

    # Formatting the response
    formatted_response = ""
    for record in data:
      # Ensure each record is a dictionary and has the expected keys
      if isinstance(
          record, dict
      ) and 'SourceType' in record and 'TotalCapacity' in record and 'AverageCapacity' in record:
        formatted_response += f"SourceType: {record['SourceType']}, Total Capacity: {record['TotalCapacity']}, Average Capacity: {record['AverageCapacity']}\n"
      else:
        return "Unexpected data format received from the database."

    return formatted_response.strip(
    ) if formatted_response else "No data available for the specified threshold."


class CampaignModel:

  def __init__(self, campaign_id=None):
    self.campaign_id = campaign_id

  def create_campaign(self, date, target_audience, campaign_name):
    return Database.insert(Query.CREATE_CAMPAIGN,
                           (date, target_audience, campaign_name))

  def read_campaign(self):
    return Database.select(Query.READ_CAMPAIGN, (self.campaign_id, ))

  def update_campaign(self, date, target_audience, campaign_name):
    return Database.update(
        Query.UPDATE_CAMPAIGN,
        (date, target_audience, campaign_name, self.campaign_id))

  def delete_campaign(self):
    return Database.delete(Query.DELETE_CAMPAIGN, (self.campaign_id, ))

  @staticmethod
  def update_campaign_and_media_outreach(campaign_id, campaign_name, target_audience):
      query = Query.UPDATE_CAMPAIGN_AND_MEDIA_OUTREACH
      result = Database.update(query, (campaign_name, target_audience, campaign_id, campaign_name, campaign_id))

      if result:
          return f"Campaign ID {campaign_id} updated with name '{campaign_name}' and target audience '{target_audience}'. Media outreach also updated."
      else:
          return "Failed to update campaign and media outreach."


class FeedbackModel:

  def __init__(self, feedback_id=None):
    self.feedback_id = feedback_id

  def create_feedback(self, rating, content):
    return Database.insert(Query.CREATE_FEEDBACK, (rating, content))

  def read_feedback(self):
    return Database.select(Query.READ_FEEDBACK, (self.feedback_id, ))

  def update_feedback(self, rating, content):
    return Database.update(Query.UPDATE_FEEDBACK,
                           (rating, content, self.feedback_id))

  def delete_feedback(self):
    return Database.delete(Query.DELETE_FEEDBACK, (self.feedback_id, ))


class ReportModel:

  def __init__(self, report_id=None):
    self.report_id = report_id

  def create_report(self, duration, generated_date, report_type, user_id):
    return Database.insert(Query.CREATE_REPORT,
                           (duration, generated_date, report_type, user_id))

  def read_report(self):
    return Database.select(Query.READ_REPORT, (self.report_id, ))

  def update_report(self, duration, generated_date, report_type):
    return Database.update(
        Query.UPDATE_REPORT,
        (duration, generated_date, report_type, self.report_id))

  def delete_report(self):
    return Database.delete(Query.DELETE_REPORT, (self.report_id, ))


class InventoryModel:

  def __init__(self, inventory_id=None):
    self.inventory_id = inventory_id

  def create_inventory(self, quantity, product_name):
    return Database.insert(Query.CREATE_INVENTORY, (quantity, product_name))

  def read_inventory(self):
    return Database.select(Query.READ_INVENTORY, (self.inventory_id, ))

  def update_inventory(self, quantity, product_name):
    return Database.update(Query.UPDATE_INVENTORY,
                           (quantity, product_name, self.inventory_id))

  def delete_inventory(self):
    return Database.delete(Query.DELETE_INVENTORY, (self.inventory_id, ))


class SupplierModel:

  def __init__(self, supplier_id=None):
    self.supplier_id = supplier_id

  def create_supplier(self, supplier_name, product_type):
    return Database.insert(Query.CREATE_SUPPLIER,
                           (supplier_name, product_type))

  def read_supplier(self):
    return Database.select(Query.READ_SUPPLIER, (self.supplier_id, ))

  def update_supplier(self, supplier_name, product_type):
    return Database.update(Query.UPDATE_SUPPLIER,
                           (supplier_name, product_type, self.supplier_id))

  def delete_supplier(self):
    return Database.delete(Query.DELETE_SUPPLIER, (self.supplier_id, ))

  @staticmethod
  def delete_supplier_and_inventory(supplier_id):
      query = Query.DELETE_SUPPLIER_AND_INVENTORY
      result = Database.delete(query, (supplier_id, supplier_id))

      if result:
          return f"Supplier with ID {supplier_id} and associated inventory deleted successfully."
      else:
          return "Failed to delete supplier and inventory."


class ResearchProjectModel:

  def __init__(self, project_id=None):
    self.project_id = project_id

  def create_research_project(self, project_name, funding_source, dates,
                              employee_id):
    return Database.insert(Query.CREATE_RESEARCH_PROJECT,
                           (project_name, funding_source, dates, employee_id))

  def read_research_project(self):
    return Database.select(Query.READ_RESEARCH_PROJECT, (self.project_id, ))

  def update_research_project(self, project_name, funding_source, dates):
    return Database.update(
        Query.UPDATE_RESEARCH_PROJECT,
        (project_name, funding_source, dates, self.project_id))

  def delete_research_project(self):
    return Database.delete(Query.DELETE_RESEARCH_PROJECT, (self.project_id, ))


class LegalCaseModel:

  def __init__(self, case_id=None):
    self.case_id = case_id

  def create_legal_case(self, status, lawyer_assigned):
    return Database.insert(Query.CREATE_LEGAL_CASE, (status, lawyer_assigned))

  def read_legal_case(self):
    return Database.select(Query.READ_LEGAL_CASE, (self.case_id, ))

  def update_legal_case(self, status, lawyer_assigned):
    return Database.update(Query.UPDATE_LEGAL_CASE,
                           (status, lawyer_assigned, self.case_id))

  def delete_legal_case(self):
    return Database.delete(Query.DELETE_LEGAL_CASE, (self.case_id, ))

  @staticmethod
  def cases_by_status(status):
      query = Query.LEGAL_CASES_STATUS
      data = Database.select(query, (status,))

      if not data or not isinstance(data, list):
          return "No legal cases found for the specified status."

      formatted_response = ""
      for record in data:
          if isinstance(record, dict) and 'Caseid' in record and 'LawyerAssigned' in record and 'FullName' in record:
              formatted_response += f"Case ID: {record['Caseid']}, Lawyer: {record['LawyerAssigned']}, Employee: {record['FullName']}\n"
          else:
              return "Unexpected data format received from the database."

      return formatted_response.strip()


class ParticipantFeedbackModel:

  def __init__(self, feedback_sequence=None):
    self.feedback_sequence = feedback_sequence

  def create_participant_feedback(self, comments, fullname):
    return Database.insert(Query.CREATE_PARTICIPANT_FEEDBACK,
                           (comments, fullname))

  def read_participant_feedback(self):
    return Database.select(Query.READ_PARTICIPANT_FEEDBACK,
                           (self.feedback_sequence, ))

  def update_participant_feedback(self, comments, fullname):
    return Database.update(Query.UPDATE_PARTICIPANT_FEEDBACK,
                           (comments, fullname, self.feedback_sequence))

  def delete_participant_feedback(self):
    return Database.delete(Query.DELETE_PARTICIPANT_FEEDBACK,
                           (self.feedback_sequence, ))


class AssetModel:

  def __init__(self, asset_id=None):
    self.asset_id = asset_id

  def create_asset(self, asset_type, value, date_purchased, user_id):
    return Database.insert(Query.CREATE_ASSET,
                           (asset_type, value, date_purchased, user_id))

  def read_asset(self):
    return Database.select(Query.READ_ASSET, (self.asset_id, ))

  def update_asset(self, asset_type, value, date_purchased):
    return Database.update(Query.UPDATE_ASSET,
                           (asset_type, value, date_purchased, self.asset_id))

  def delete_asset(self):
    return Database.delete(Query.DELETE_ASSET, (self.asset_id, ))

  @staticmethod
  def insert_asset_and_facility(asset_type, value, date_purchased, user_id, size, location, usage_type):
      Database.insert(Query.INSERT_ASSET_AND_FACILITY, (asset_type, value, date_purchased, user_id, float(size), location, usage_type))
      return "Asset and facility data inserted successfully."


class FacilityModel:

  def __init__(self, facility_id=None):
    self.facility_id = facility_id

  def create_facility(self, size, location, usage_type, asset_id):
    return Database.insert(Query.CREATE_FACILITY,
                           (size, location, usage_type, asset_id))

  def read_facility(self):
    return Database.select(Query.READ_FACILITY, (self.facility_id, ))

  def update_facility(self, size, location, usage_type):
    return Database.update(Query.UPDATE_FACILITY,
                           (size, location, usage_type, self.facility_id))

  def delete_facility(self):
    return Database.delete(Query.DELETE_FACILITY, (self.facility_id, ))


class TrainingProgramModel:

  def __init__(self, training_id=None):
    self.training_id = training_id

  def create_training_program(self, training_name, duration, facility_id,
                              employee_id):
    return Database.insert(Query.CREATE_TRAINING_PROGRAM,
                           (training_name, duration, facility_id, employee_id))

  def read_training_program(self):
    return Database.select(Query.READ_TRAINING_PROGRAM, (self.training_id, ))

  def update_training_program(self, training_name, duration):
    return Database.update(Query.UPDATE_TRAINING_PROGRAM,
                           (training_name, duration, self.training_id))

  def delete_training_program(self):
    return Database.delete(Query.DELETE_TRAINING_PROGRAM, (self.training_id, ))


class NotificationModel:

  def __init__(self, notification_id=None):
    self.notification_id = notification_id

  def create_notification(self, content, frequency, notification_type):
    return Database.insert(Query.CREATE_NOTIFICATION,
                           (content, frequency, notification_type))

  def read_notification(self):
    return Database.select(Query.READ_NOTIFICATION, (self.notification_id, ))

  def update_notification(self, content, frequency, notification_type):
    return Database.update(
        Query.UPDATE_NOTIFICATION,
        (content, frequency, notification_type, self.notification_id))

  def delete_notification(self):
    return Database.delete(Query.DELETE_NOTIFICATION, (self.notification_id, ))


class BillingModel:

  def __init__(self, billing_id=None):
    self.billing_id = billing_id

  def create_billing(self, payment_method, due_date, amount):
    return Database.insert(Query.CREATE_BILLING,
                           (payment_method, due_date, amount))

  def read_billing(self):
    return Database.select(Query.READ_BILLING, (self.billing_id, ))

  def update_billing(self, payment_method, due_date, amount):
    return Database.update(Query.UPDATE_BILLING,
                           (payment_method, due_date, amount, self.billing_id))

  def delete_billing(self):
    return Database.delete(Query.DELETE_BILLING, (self.billing_id, ))


class DataCollectionModel:

  def __init__(self, collection_id=None):
    self.collection_id = collection_id

  def create_data_collection(self, timestamp, consumption_value,
                             integration_types, user_id):
    return Database.insert(
        Query.CREATE_DATA_COLLECTION,
        (timestamp, consumption_value, integration_types, user_id))

  def read_data_collection(self):
    return Database.select(Query.READ_DATA_COLLECTION, (self.collection_id, ))

  def update_data_collection(self, timestamp, consumption_value,
                             integration_types):
    return Database.update(
        Query.UPDATE_DATA_COLLECTION,
        (timestamp, consumption_value, integration_types, self.collection_id))

  def delete_data_collection(self):
    return Database.delete(Query.DELETE_DATA_COLLECTION,
                           (self.collection_id, ))


class AviationAnalyticsModel:

  def __init__(self, aircraft_type=None):
    self.aircraft_type = aircraft_type

  def create_aviation_analytics(self, fuel_cost, time, collection_id):
    return Database.insert(
        Query.CREATE_AVIATION_ANALYTICS,
        (self.aircraft_type, fuel_cost, time, collection_id))

  def read_aviation_analytics(self):
    return Database.select(Query.READ_AVIATION_ANALYTICS,
                           (self.aircraft_type, ))

  def update_aviation_analytics(self, fuel_cost, time):
    return Database.update(Query.UPDATE_AVIATION_ANALYTICS,
                           (fuel_cost, time, self.aircraft_type))

  def delete_aviation_analytics(self):
    return Database.delete(Query.DELETE_AVIATION_ANALYTICS,
                           (self.aircraft_type, ))


class PowerMetricsModel:

  def __init__(self, infrastructure_plans=None):
    self.infrastructure_plans = infrastructure_plans

  def create_power_metrics(self, total_power, average_cost, collection_id):
    return Database.insert(
        Query.CREATE_POWER_METRICS,
        (self.infrastructure_plans, total_power, average_cost, collection_id))

  def read_power_metrics(self):
    return Database.select(Query.READ_POWER_METRICS,
                           (self.infrastructure_plans, ))

  def update_power_metrics(self, total_power, average_cost):
    return Database.update(
        Query.UPDATE_POWER_METRICS,
        (total_power, average_cost, self.infrastructure_plans))

  def delete_power_metrics(self):
    return Database.delete(Query.DELETE_POWER_METRICS,
                           (self.infrastructure_plans, ))


class MediaOutreachModel:

  def __init__(self, platform=None):
    self.platform = platform

  def create_media_outreach(self, content_type, campaign_name, campaign_id):
    return Database.insert(
        Query.CREATE_MEDIA_OUTREACH,
        (self.platform, content_type, campaign_name, campaign_id))

  def read_media_outreach(self):
    return Database.select(Query.READ_MEDIA_OUTREACH, (self.platform, ))

  def update_media_outreach(self, content_type, campaign_name):
    return Database.update(Query.UPDATE_MEDIA_OUTREACH,
                           (content_type, campaign_name, self.platform))

  def delete_media_outreach(self):
    return Database.delete(Query.DELETE_MEDIA_OUTREACH, (self.platform, ))


class MailingModel:

  def __init__(self, mailing_id=None):
    self.mailing_id = mailing_id

  def create_mailing(self, address, delivery_date):
    return Database.insert(Query.CREATE_MAILING, (address, delivery_date))

  def read_mailing(self):
    return Database.select(Query.READ_MAILING, (self.mailing_id, ))

  def update_mailing(self, address, delivery_date):
    return Database.update(Query.UPDATE_MAILING,
                           (address, delivery_date, self.mailing_id))

  def delete_mailing(self):
    return Database.delete(Query.DELETE_MAILING, (self.mailing_id, ))


class PartnershipModel:

  def __init__(self, partnership_id=None):
    self.partnership_id = partnership_id

  def create_partnership(self, duration, start_date, partner_name,
                         employee_id):
    return Database.insert(Query.CREATE_PARTNERSHIP,
                           (duration, start_date, partner_name, employee_id))

  def read_partnership(self):
    return Database.select(Query.READ_PARTNERSHIP, (self.partnership_id, ))

  def update_partnership(self, duration, start_date, partner_name):
    return Database.update(
        Query.UPDATE_PARTNERSHIP,
        (duration, start_date, partner_name, self.partnership_id))

  def delete_partnership(self):
    return Database.delete(Query.DELETE_PARTNERSHIP, (self.partnership_id, ))

  @staticmethod
  def detailed_report(min_duration):
      query = Query.DETAILED_REPORT_PARTNERSHIPS
      data = Database.select(query, (min_duration,))

      if not data or not isinstance(data, list):
          return "No partnership details found for the specified duration."

      formatted_response = ""
      for record in data:
          if isinstance(record, dict) and 'PartnerName' in record and 'FullName' in record and 'Position' in record:
              formatted_response += f"Partner: {record['PartnerName']}, Employee: {record['FullName']}, Position: {record['Position']}\n"
          else:
              return "Unexpected data format received from the database."

      return formatted_response.strip()

