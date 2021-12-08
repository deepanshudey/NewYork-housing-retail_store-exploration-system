import psycopg2
import psycopg2.extras
import json
import pandas as pd
from pymongo import MongoClient
from psycopg2 import sql
import geopy.distance
from prettytable import PrettyTable
from uszipcode import SearchEngine
from datetime import datetime, timezone

dt = datetime.now(timezone.utc)
class DatabaseProjectStores():
    
    def __init__(self,conn):
        self.conn=conn

        
        return           


    def search_projects_zipcode(self):
        zip = input("Enter zip code (Example: 10030) \t")
        if(len(zip)!=5):
            raise Exception("Pincode must be 5 digits")

        try:
            query = sql.SQL("""select project_id ,
    project_name,
    project_start_date,
    project_completion_date,
    postcode,bbl  from project  where postcode= {zip}""").format(zip=sql.Literal(zip))
           

            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # print(cursor.mogrify(query, params))
            # print(cursor.mogrify(query, params))
            cursor.execute(query)
            result = cursor.fetchall()
            print(" Projects in the entered pincode are: \n")
            if result==[]:
                print("No Projects found at this pincode")
            else:
                table= PrettyTable()
                table.field_names = ["Project ID","Project name", "Project Start Date","Project Completion Date","Postcode","BBL"]
                for row in result:
                    table.add_row(row)
                print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]

            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            #print(x)
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "project",y,dt,"Select"))
            self.conn.commit()
            return

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return



    def search_projects_project_id(self):
        x = input("Enter project id (Example: 44223) \t")
        try:
            query = sql.SQL("""select project_id ,
    project_name,
    project_start_date,
    project_completion_date,
    postcode,bbl from project where project_id= {x}""").format(x=sql.Literal(x))
           

            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # print(cursor.mogrify(query, params))
            # print(cursor.mogrify(query, params))
            cursor.execute(query)
            result = cursor.fetchall()
            print(" Project details: \n")
            if result==[]:
                print("No Projects found with this ID. Enter valid/correct project id")
            else:
                table= PrettyTable()
                table.field_names = ["Project ID","Project name", "Project Start Date","Project Completion Date","Postcode","BBL"]
                for row in result:
                    table.add_row(row)
                print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "project",y,dt ,"Select"))
            self.conn.commit()
            return

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return




    def search_projects_name(self):
        x = input("Enter project name or part of it (Example: Rochest) \t")
        try:
            query = sql.SQL("""select project_id ,
    project_name,
    project_start_date,
    project_completion_date,
    postcode,bbl from project where project_name ilike {x}""").format(x=sql.Literal("%"+x+"%"))
           

            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # print(cursor.mogrify(query, params))
            # print(cursor.mogrify(query, params))
            cursor.execute(query)
            result = cursor.fetchall()
            if result==[]:
                print("No Projects found with this Project Name")
            else:
                table= PrettyTable()
                table.field_names = ["Project ID","Project name", "Project Start Date","Project Completion Date","Postcode","BBL"]
                for row in result:
                    table.add_row(row)
                print(table)
            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "project",y,dt,"Select" ))
            self.conn.commit()
            return

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return




    def search_projects_date(self):
        x = input("Enter Date after which you want to view the projects (Enter Date in YYYY-MM-DD format only) \t")
        try:
            query = sql.SQL("""select project_id ,
    project_name,
    project_start_date,
    project_completion_date,
    postcode,bbl from project where project_start_date>= {x}""").format(x=sql.Literal(x))

            import datetime
            try:
                datetime.datetime.strptime(x, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
           

            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # print(cursor.mogrify(query, params))
            # print(cursor.mogrify(query, params))
            cursor.execute(query)
            result = cursor.fetchall()
            if result==[]:
                print("No Projects found which started after this date")
            else:
                print(" Projects Details: \n")
            
                # for r in result:
                #     print(" Project Id : ",
                #       r[0], " Project Name: ", r[1].rstrip(), " Project Start Date: ", r[2], " Project End Date: ", r[3], " Zip : ", r[4])
                table= PrettyTable()
                table.field_names = ["Project ID","Project name", "Project Start Date","Project Completion Date","Postcode","BBL"]
                for row in result:
                    table.add_row(row)
                print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "project",y,dt,"Select" ))
            self.conn.commit()
            return

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return





######################################################### b   #########################################################



    def search_zipcode(self):
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)

            query = sql.SQL("""select distinct r.store_name,r.street_address,p.project_name,h.facility_name,
            r.zip_code  from  retail_store r inner join project p on p.postcode=r.zip_code inner join hospital h 
            on h.postcode=p.postcode limit 20""")

            
            cursor.execute(query)
            result = cursor.fetchall()
            #print(result)

            
            
            table= PrettyTable()
            table.field_names = ["store_name","street name", "project_name","facility_name","Zipcode"]
            for row in result:
                table.add_row(row)
            print(table)


            
            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "retail_store",y,dt ,"Select"))
            cursor.execute(query1, (x, "project",y,dt ,"Select"))
            cursor.execute(query1, (x, "hospital",y,dt,"Select" ))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return

    
    #################################  c  ######################################
    
    def search_retail_store_closest(self):
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            query = """select store_name,
    street_address ,
borough,latitude,longitude,zip_code  from retail_store"""
            p = input("Enter your pincode: (Example: 10010) \t")
            #lon = input("Enter your Longitude: (Example: -73.95) \t")
            km = float(input("Enter Desired KM range (Example: 50)\t"))

            if(len(p)!=5):
                raise Exception("Incorrect Pincode")

            if(km<0):
                raise Exception("Invalid Distance")
            cursor.execute(query)
            result = cursor.fetchall()
            search = SearchEngine(simple_zipcode=True)
            zip1 = search.by_zipcode(p)
            lat1 =zip1.lat
            long1 =zip1.lng
            all_closest =[]
            coords = (lat1, long1)
            for r in result:
                coord_2 = (r[3], r[4])
                
                dis = geopy.distance.geodesic(coords, coord_2).km
                #print(dis)
                if(dis < km):
                    
                    all_closest.append([r,dis ])
            #print(all_closest)
            all_closest.sort(key=lambda x: x[1])
            if(len(all_closest) >=10):
                ten = all_closest[:10]
            else:
                ten = all_closest
            #print(all_closest)
            table= PrettyTable()
            table.field_names = ["Store Name", "Street Address","Borough","Latitude","Longitude","Zipcode","Distance"]
            for el in ten:
                table.add_row([el[0][0],el[0][1],el[0][2],el[0][3],el[0][4],el[0][5],el[1]])
            print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "retail_store",y,dt,"Select" ))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return




    def search_hospitals_closest(self):
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            query = """select facility_type,
    facility_name ,
location_1,latitude,longitude,postcode  from hospital"""
            p = input("Enter your pincode: (Example: 10010) \t")
            #lon = input("Enter your Longitude: (Example: -73.95) \t")
            km = float(input("Enter Desired KM range (Example: 50)\t"))

            if(len(p)!=5):
                raise Exception("Incorrect Pincode")

            if(km<0):
                raise Exception("Invalid Distance")
            cursor.execute(query)
            result = cursor.fetchall()
            search = SearchEngine(simple_zipcode=True)
            zip1 = search.by_zipcode(p)
            lat1 =zip1.lat
            long1 =zip1.lng
            all_closest =[]
            coords = (lat1, long1)
            for r in result:
                coord_2 = (r[3], r[4])
                
                dis = geopy.distance.geodesic(coords, coord_2).km
                #print(dis)
                if(dis < km):
                    
                    all_closest.append([r,dis ])
            #print(all_closest)
            all_closest.sort(key=lambda x: x[1])
            if(len(all_closest) >=10):
                ten = all_closest[:10]
            else:
                ten = all_closest
            #print(all_closest)
            table= PrettyTable()
            table.field_names = ["Facility Type", "Facility Name","Location","Latitude","Longitude","Zipcode","Distance"]
            for el in ten:
                table.add_row([el[0][0],el[0][1],el[0][2],el[0][3],el[0][4],el[0][5],el[1]])
            print(table)
            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "hospital",y,dt,"Select" ))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return

   
    def search_projects_closest(self):
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            query = """select p.project_id,
    p.project_name ,
p.project_start_date,p.project_completion_date,b.latitude,b.longitude,p.postcode  from project p inner join building_address b on p.project_id=b.project_id"""
            p = input("Enter your pincode: (Example: 10010) \t")
            #lon = input("Enter your Longitude: (Example: -73.95) \t")
            km = float(input("Enter Desired KM range (Example: 50)\t"))

            if(len(p)!=5):
                raise Exception("Incorrect Pincode")

            if(km<0):
                raise Exception("Invalid Distance")

            cursor.execute(query)
            result = cursor.fetchall()
            search = SearchEngine(simple_zipcode=True)
            zip1 = search.by_zipcode(p)
            lat1 =zip1.lat
            long1 =zip1.lng
            all_closest =[]
            coords = (lat1, long1)
            for r in result:
                coord_2 = (r[4], r[5])
                
                dis = geopy.distance.geodesic(coords, coord_2).km
                #print(dis)
                if(dis < km):
                    
                    all_closest.append([r,dis ])
            #print(all_closest)
            all_closest.sort(key=lambda x: x[1])
            if(len(all_closest) >=10):
                ten = all_closest[:10]
            else:
                ten = all_closest
            #print(all_closest)
            table= PrettyTable()
            table.field_names = ["Project ID", "Project Name","Project Start Date","Project End Date","Latitude","Longitude","Zipcode","Distance"]
            for el in ten:
                table.add_row([el[0][0],el[0][1],el[0][2],el[0][3],el[0][4],el[0][5],el[0][6],el[1]])
            print(table)
            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)

            cursor.execute(query1, (x, "project",y,dt ,"Select"))

            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return







    def search_school(self):
        try:    

            pin = input("Enter the pincode (Example: 10011)\t")
            
            client = MongoClient("mongodb://localhost:27017/")
            projectDB = client["project"]
            project_collection = projectDB["project"]
            
            # client.server_info()
            results = project_collection.find({"postcode": pin})
            if results==[]:
                print("No schools found at this pincode")
            for x in results:
                print("\n")
                print(" School Name : ",
                      x["school"], " School Address: ", x["address"])



        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return

        cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor)
        us = sql.SQL("""select current_user """)
        cursor.execute(us)
        result = cursor.fetchall()
        for r in result:
            x=r[0]
        #print(x)
        # db = sql.SQL("""SELECT current_database() """)
        # cursor.execute(db)
        # result = cursor.fetchall()
        # for r in result:
        #     y=r[0]
        query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
        cursor.execute(query1, (x, "NA(Non-Relational)","school",dt ,"Select"))



    def search_school_closest(self):
        try:    
            from decimal import Decimal
            pin = input("Enter your pincode \t")
            
            client = MongoClient("mongodb://localhost:27017/")
            projectDB = client["project"]
            project_collection = projectDB["project"]
            
            # client.server_info()
            results = project_collection.find()
            if results==[]:
                print("No schools found at this pincode")
            else:
                #print(results["school"])
                km = float(input("Enter Desired KM range \t"))

                search = SearchEngine(simple_zipcode=True)
                zip1 = search.by_zipcode(pin)
                lat1 =zip1.lat
                long1 =zip1.lng
                all_closest =[]
                coords = (lat1, long1)
                
                for r in results:
                    #print(r["school"])
                    coord_2 = (Decimal(r["latitude"]), Decimal(r["longitude"]))
                    print(coord_2)
                    #dis = geopy.distance.geodesic(coords, coord_2).km
                    #print(dis)
                #     if(dis < km):
                        
                #         all_closest.append([r,dis ])
                # print(all_closest)
                # all_closest.sort(key=lambda x: x[1])
                # if(len(all_closest) >=10):
                #     ten = all_closest[:10]
                # else:
                #     ten = all_closest
                #print(all_closest)
                table= PrettyTable()
                #print(ten[2])
                # table.field_names = ["Store Name", "Street Address","Distance"]
                # for el in ten:
                #     table.add_row([el["school"],el["address"],el[1]])
                # print(table)

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return



    def display_table(self):
        try:    

            table_name = input("Enter the table name you want to view \t")
            print("\n")
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            query = sql.SQL("""select * from {table_name} limit 10""").format(table_name=sql.Identifier(table_name))

            
            cursor.execute(query)
            result = cursor.fetchall()
            x= [i[0] for i in cursor.description]
            #print(x)
            table= PrettyTable()
            table.field_names = x
            for row in result:
                table.add_row(row)
            print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, table_name,y,dt ,"Select"))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return



    def display_user_logs(self):
        try:    

            print("\n")
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            query = sql.SQL("""select * from user_logs order by stamp desc limit 10""")

            
            cursor.execute(query)
            result = cursor.fetchall()

            x= [i[0] for i in cursor.description]
            #print(x)
            table= PrettyTable()
            table.field_names = x
            for row in result:
                table.add_row(row)
            print(table)

            # us = sql.SQL("""select current_user """)
            # cursor.execute(us)
            # result = cursor.fetchall()
            # for r in result:
            #     x=r[0]
            # #print(x)
            # db = sql.SQL("""SELECT current_database() """)
            # cursor.execute(db)
            # result = cursor.fetchall()
            # for r in result:
            #     y=r[0]
            # query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            # cursor.execute(query1, (x, table_name,y,dt,"Select" ))
            # self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return   

    def display_audit(self):
        try:    

            table_name = input("Enter the table name you want to view \t")
            print("\n")
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            query = sql.SQL("""select * from {table_name} order by stamp desc limit 10""").format(table_name=sql.Identifier(table_name))

            
            cursor.execute(query)
            result = cursor.fetchall()
            x= [i[0] for i in cursor.description]
            #print(x)
            table= PrettyTable()
            table.field_names = x
            for row in result:
                table.add_row(row)
            print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, table_name,y,dt,"Select" ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return


            

    def insert_retail_store(self):
        try:    

            store_name = input("Enter  Store Name ( String ) \t")
            street_address = input("Enter  Street Address \t")
            borough = input("Enter  borough \t")
            zip_code = input("Enter  zip_code (5 digits) \t")
            bbl= input("Enter  bbl (10 digits) \t")
            latitude = input("Enter  latitude \t")
            longitude = input("Enter longitude \t \n")

            if(len(bbl)!=10):
                raise Exception("bbl should 10 digits")


            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            n=0

            query = """INSERT INTO retail_store (store_name, street_address,
                            borough, zip_code, bbl, latitude, longitude) VALUES (%s, %s, %s,%s,%s,%s,%s)"""

            

            cursor.execute(query, (store_name, street_address,
                            borough, zip_code, bbl, latitude, longitude))

            # self.conn.commit()
            n = n+cursor.rowcount
            if(n ==1):
                self.conn.commit()
                print("Inserted Succesfully")

                us = sql.SQL("""select current_user """)
                cursor.execute(us)
                result = cursor.fetchall()
                for r in result:
                    x=r[0]
                #print(x)
                db = sql.SQL("""SELECT current_database() """)
                cursor.execute(db)
                result = cursor.fetchall()
                for r in result:
                    y=r[0]
                query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
                cursor.execute(query1, (x, "retail_store",y,dt,"Insert" ))
                self.conn.commit()
            else:
                print("There is some problem with the entered values")
                return 




        except Exception as e:
            self.conn.rollback()
            print("This is the Error")

            print(str(e))
            print("Contact Admin for resolution")
            return


    def search_all(self):
        
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            
            query = sql.SQL(""" select postcode,count(*) from hospital  group by postcode having count(*) >1 and postcode in 
            (select zip_code from retail_store where zip_code in
            (
            select postcode from project group by postcode having count(*) > 1
            )) order by count(*) descz""")

            
            cursor.execute(query)
            result = cursor.fetchall()
            #print(result)

            
            
            table= PrettyTable()
            table.field_names = ["ZipCode","Number of Hospital,Projects,Retail Store"]
            for row in result:
                table.add_row(row)
            print(table)
            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "retail_store",y,dt ,"Select"))
            cursor.execute(query1, (x, "project",y,dt ,"Select"))
            cursor.execute(query1, (x, "hospital",y,dt,"Select" ))
            self.conn.commit()


        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return

    

    def search_borough(self):
        
        try:
            cursor = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            
            query = sql.SQL("""         select borough,count(*) from building_address  group by borough having borough in 
            (select borough from hospital)
            """)


            
            cursor.execute(query)
            result = cursor.fetchall()
            #print(result)

            
            
            table= PrettyTable()
            table.field_names = ["ZipCode","Number of Hospital,Projects,Retail Store"]
            for row in result:
                table.add_row(row)
            print(table)

            us = sql.SQL("""select current_user """)
            cursor.execute(us)
            result = cursor.fetchall()
            for r in result:
                x=r[0]
            #print(x)
            db = sql.SQL("""SELECT current_database() """)
            cursor.execute(db)
            result = cursor.fetchall()
            for r in result:
                y=r[0]
            query1 = sql.SQL("""INSERT INTO user_logs (userid, table_name,db,stamp,operation) VALUES (%s, %s, %s,%s,%s) """)
            cursor.execute(query1, (x, "building_address",y,dt ,"Select"))
            cursor.execute(query1, (x, "hospital",y,dt,"Select" ))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print("This is the Error")
            print(str(e))
            print("Contact Admin for resolution")
            return
