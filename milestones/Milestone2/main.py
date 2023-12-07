"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
import os
from discord.ext import commands
from models import *
from database import Database

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
  print(f"Bot {bot.user} has joined the room")  # the bot is online
  Database.connect(bot.user)  # bot connected to database


# set the inbounds for ipv4 addresses in your AWS RDS instance to https:/0.0.0.0/


@bot.command(
    name="test",
    description="write your database business requirement for this command here"
)
async def _test(ctx, arg1):
  testModel = TestModel(ctx, arg1)
  response = testModel.response()
  await ctx.send(response)


# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.


@bot.command(
    name="getEnergyProductionReport",
    description="Retrieve energy production report for sources above a threshold"
)
async def get_energy_production_report(ctx, threshold: float):
  response = EnergySourceModel.summary_report(threshold)
  await ctx.send(response)


@bot.command(name="getUserFeedbackByEnergySource",
             description="Get user feedback for a specific energy source")
async def get_user_feedback_by_energy_source(ctx, energy_source: str):
  response = UserModel.users_feedback(energy_source)
  await ctx.send(response)


@bot.command(
    name="getPartnershipDetails",
    description="Get details of partnerships longer than a specified duration")
async def get_partnership_details(ctx, duration: int):
  response = PartnershipModel.detailed_report(duration)
  await ctx.send(response)


@bot.command(name="getLegalCasesByStatus",
             description="Get legal cases by their status")
async def get_legal_cases_by_status(ctx, status: str):
  response = LegalCaseModel.cases_by_status(status)
  await ctx.send(response)


@bot.command(name="insertEmployeeAndTraining",
             description="Insert a new employee and their training program")
async def insert_employee_and_training(ctx, name: str, position: str,
                                       training_name: str, duration: int,
                                       facility_id: int):
  response = EmployeeModel.insert_employee_and_training(
      name, position, training_name, duration, facility_id)
  await ctx.send(response)


@bot.command(name="addAssetWithFacility",
   description="Add a new asset and its corresponding facility")
async def add_asset_with_facility(ctx, asset_details: str, facility_details: str):
# Extracting individual details from the input strings
  asset_type, value, date_purchased, user_id = asset_details.split(',')
  size, location, usage_type = facility_details.split(',')

# Convert value, user_id, and size to appropriate types
  value = float(value)
  user_id = int(user_id)
  size = float(size)  # Updated to float as per schema

# Call the method with processed values
  response = AssetModel.insert_asset_and_facility(asset_type.strip(), value,
                                          date_purchased.strip(),
                                          user_id, size,
                                          location.strip(),
                                          usage_type.strip())
  await ctx.send(response)


@bot.command(name="updateUserContactAndMailing",
             description="Update user contact information and mailing address")
async def update_user_contact_and_mailing(ctx, user_id: int,
                                          new_contact_info: str,
                                          new_mailing_info: str):
  response = UserModel.update_contact_and_mailing(user_id, new_contact_info,
                                                  new_mailing_info)
  await ctx.send(response)


@bot.command(
    name="modifyCampaignAndMediaOutreach",
    description="Modify campaign details and update media outreach records")
async def modify_campaign_and_media_outreach(ctx, campaign_id: int,
                                             new_campaign_details: str):
  # Extracting individual details from the input string
  campaign_name, target_audience = new_campaign_details.split(',')
  response = CampaignModel.update_campaign_and_media_outreach(
      campaign_id, campaign_name.strip(), target_audience.strip())
  await ctx.send(response)


@bot.command(
    name="deleteSupplierAndInventory",
    description="Delete a supplier and all associated inventory records")
async def delete_supplier_and_inventory(ctx, supplier_id: int):
  response = SupplierModel.delete_supplier_and_inventory(supplier_id)
  await ctx.send(response)


@bot.command(
    name="removeEmployeeAndTraining",
    description="Remove an employee and all related training program records")
async def remove_employee_and_training(ctx, employee_id: int):
  response = EmployeeModel.delete_employee_and_training(employee_id)
  await ctx.send(response)


@bot.command(name="enableEnergySourceChangeLog",
   description="Enable logging changes to the Energy Source table")
async def enable_energy_source_change_log(ctx):
  try:
    Database.create_trigger(Query.TRIGGER_ENERGY_SOURCE_AUDIT)
    await ctx.send("Energy Source change log trigger enabled.")
  except Exception as e:
    await ctx.send(f"Failed to enable trigger: {e}")



@bot.command(name="enableUserDeletionBackup",
   description="Enable backup of user data upon deletion")
async def enable_user_deletion_backup(ctx):
  try:
    Database.create_trigger(Query.TRIGGER_BACKUP_USER_DATA)
    await ctx.send("User deletion backup trigger enabled.")
  except Exception as e:
    await ctx.send(f"Failed to enable trigger: {e}")
  


@bot.command(
  name="calculateAvgEnergyConsumption",
  description="Calculate the average energy consumption for a specific energy type")
async def calculate_avg_energy_consumption(ctx, energy_type: str):
  result = Database.call_procedure("calculate_average_energy_consumption", (energy_type,))
  if result:
      await ctx.send(f"Average energy consumption for {energy_type}: {result['average_capacity']}")
  else:
      await ctx.send("Error calculating average energy consumption.")

@bot.command(
  name="getNextEnergySourceID",
  description="Get the next available unique ID for a new energy source")
async def get_next_energy_source_id(ctx):
  next_id = Database.call_function("get_next_energy_source_id")
  if next_id:
      await ctx.send(f"Next energy source ID: {next_id['get_next_energy_source_id()']}")
  else:
      await ctx.send("Error retrieving the next energy source ID.")

@bot.command(
  name="calculateTotalProjectCost",
  description="Calculate the total cost of all projects for a given employee")
async def calculate_total_project_cost(ctx, employee_id: int):
  total_cost = Database.call_function("calculate_total_project_cost", (employee_id,))
  if total_cost:
      await ctx.send(f"Total project cost for employee {employee_id}: {total_cost['calculate_total_project_cost(employee_id)']}")
  else:
      await ctx.send("Error calculating total project cost.")



bot.run(TOKEN)
