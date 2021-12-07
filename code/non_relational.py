from csv import DictReader
import csv
import pandas as pd
import math
import psycopg2
from sqlalchemy import create_engine
from pymongo import MongoClient
import json




with open('data/cr93-x2xf.json') as f:
        # print("loop me ")
    json_data = json.load(f)

client = MongoClient("mongodb://localhost:27017/")
projectDB = client["project"]
project_collection = projectDB["project"]
project_collection.drop()
project_collection.insert_many(json_data)

db = client.project
collection = db["project"]
# query = {"bbl":"4037990015"}
# result = list(collection.find(query))
# print(result)
print("Done <#")