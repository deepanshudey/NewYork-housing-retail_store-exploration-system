
from csv import DictReader
import csv
import pandas as pd
import math
import psycopg2
from sqlalchemy import create_engine
from pymongo import MongoClient
import json

def convertToInt(d):
    return int(float(d))


def load_into_database():
   
    engine = create_engine('postgresql+psycopg2://admin:admin@127.0.0.1:5433/project')

    #engine = create_engine('postgresql+psycopg2://agtuxdlalnzqgd:1da65b17677151a3d0ef958a156021d37672cb8668ca7f5eab3aca5096afd669@ec2-54-158-232-223.compute-1.amazonaws.com/dc26hii2bqkpr5')
    #print(engine)


    project = pd.read_csv('data/project.csv')
    project = project.iloc[:, 1:]
    #project = project.set_index('project_id', drop=True)


    project.columns = ['project_id','project_name', 'project_start_date','project_completion_date','postcode','bbl']



    project = project.dropna(subset=['project_id'], how='any')
    project = project.drop_duplicates(subset='project_id', keep="first")


    project['postcode'] = project['postcode'].astype(str).astype(float).astype('Int64')
    project['bbl'] = project['bbl'].astype(float).astype('Int64')

    #print(project.columns)
    project.to_sql('project', engine, if_exists='append',index=False )


########################### Housing Dataset ###############################

    hdesc = pd.read_csv('data/house_description.csv')
    hdesc = hdesc.iloc[:, 1:]
    #project = project.set_index('project_id', drop=True)


    hdesc.columns = ['total_units',
    'counted_rental_units',
    'counted_home_ownership_units' ,
    '_1_br_units' ,
    '_2_br_units' ,
    '_3_br_units' ,
    '_4_br_units' ,
    '_5_br_units' ,
    '_6_br_units' ,
    'project_id'  ]



    # project = project.dropna(subset=['project_id'], how='any')
    # project = project.drop_duplicates(subset='project_id', keep="first")


    #print(project.columns)
    hdesc.to_sql('house_description', engine, if_exists='append',index=False )





    ########################### House Affordability Dataset ###############################

    haff = pd.read_csv('data/house_affordability.csv')
    haff= haff.iloc[:, 1:]
    #project = project.set_index('project_id', drop=True)


    haff.columns = [   'prevailing_wage_status',
    'low_income_units',
    'middle_income_units',
    'moderate_income_units',
    'extremely_low_income_units',
    'very_low_income_units',
    'project_id'  ]



    # project = project.dropna(subset=['project_id'], how='any')
    # project = project.drop_duplicates(subset='project_id', keep="first")


    #print(project.columns)
    haff.to_sql('house_affordability', engine, if_exists='append',index=False )





    ########################### Building Address Dataset ###############################

    build = pd.read_csv('data/building_address.csv')
    build= build.iloc[:, 1:]
        #project = project.set_index('project_id', drop=True)


    build.columns = [  'building_id',
    'borough' ,
    'street_name',
    'house_number',
    'project_id'  ,
    'latitude',
    'longitude' ]



    build = build.dropna(subset=['building_id'], how='any')
    build = build.drop_duplicates(subset='building_id', keep="first")

    build['building_id'] = build['building_id'].astype(float).astype('Int64')
    # build['latitude'] = build['latitude'].astype(str)
    # build['longitude'] = build['longitude'].astype(str)
    #print(project.columns)
    build.to_sql('building_address', engine, if_exists='append',index=False )




    ########################### Retail store Dataset ###############################

    retail = pd.read_csv('data/retail_stores.csv')
    retail= retail.iloc[:, 1:]
        #project = project.set_index('project_id', drop=True)


    # build.columns = [  'building_id',
    # 'borough' ,
    # 'street_name',
    # 'house_number',
    # 'project_id'  ,
    # 'latitude',
    # 'longitude' ]



    # build = build.dropna(subset=['building_id'], how='any')
    # build = build.drop_duplicates(subset='building_id', keep="first")

    retail['bbl'] = retail['bbl'].astype(float).astype('Int64')

    #print(project.columns)
    retail.to_sql('retail_store', engine, if_exists='append',index=False )


   ########################### Hospital Dataset ###############################

    hos = pd.read_csv('data/hospital_list.csv')
    hos= hos.iloc[:, 1:]
        #project = project.set_index('project_id', drop=True)


    # build.columns = [  'building_id',
    # 'borough' ,
    # 'street_name',
    # 'house_number',
    # 'project_id'  ,
    # 'latitude',
    # 'longitude' ]



    # build = build.dropna(subset=['building_id'], how='any')
    # build = build.drop_duplicates(subset='building_id', keep="first")

    #retail['bbl'] = retail['bbl'].astype(float).astype('Int64')

    #print(project.columns)
    hos.to_sql('hospital', engine, if_exists='append',index=False )


    print("Load Successful")