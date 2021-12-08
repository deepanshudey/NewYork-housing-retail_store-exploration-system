from database import DatabaseProjectStores
import load_data
import psycopg2
from psycopg2 import sql

if __name__ == "__main__":
    #load_data.load_everything()
    break_flag=False

    login = 'y'
    while(login != 'z' and break_flag!=True ):

        #obj = DatabaseProjectStores(conn)
        print("\n \n")
        print("Enter")


        print("1: To Login ")
        print("2: To Register ")
        print("z: To Exit ")
        login = input()
        if(login == 'z'):
            print("Thank you.  Exited!!!!")
            break

        elif(login == "2"):
            print("\n ")
            user = input("Enter your username \t")
            pas= input("Enter your password \t")
            mail = input("Enter your email \t")
            query = """INSERT INTO users (userid, passw,mail) VALUES (%s, %s, %s)"""
            connection_string = "dbname=%s user=%s password=%s host=%s port=%s" % ('project','admin','admin','127.0.0.1','5433')

            conn = psycopg2.connect(connection_string)
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(query, (user, pas,mail
                            ))

     
            

            create = sql.SQL("CREATE USER {username} WITH PASSWORD {password}").format(
             username=sql.Identifier(user),
            password=sql.Placeholder())
           
            cursor.execute(create, (pas,))

            priv = sql.SQL("GRANT Insert ON table user_login_details TO {username};").format(username=sql.Identifier(user))
        
            cursor.execute(priv)

            priv1 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE project TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv1)
            priv2 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE retail_store TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv2)
            priv3 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE building_address TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv3)
            priv4 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE house_description TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv4)
            priv5 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE hospital TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv5)
            priv6 = sql.SQL("GRANT ALL PRIVILEGES ON TABLE house_affordability TO {username};").format(username=sql.Identifier(user))
            cursor.execute(priv6)
            print("Registration Successful!!!!")
            conn.commit()



        elif(login == "1"):
            print("\n ")
            

            ex=0
            user = input("Enter your username \t")
            pas= input("Enter your password \t")
            try:
                connection_string = "dbname=%s user=%s password=%s host=%s port=%s" % ('project',user,pas,'127.0.0.1','5433')
                conn = psycopg2.connect(connection_string)


                try:   

                    from datetime import datetime, timezone

                    dt = datetime.now(timezone.utc)

                    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                    n=0

                    query = """INSERT INTO user_login_details (userid, passw,stamp) VALUES (%s, %s, %s)"""

                    cursor.execute(query, (user, pas,dt
                                    ))

                    # self.conn.commit()
                    n = n+cursor.rowcount
                    if(n ==1):
                        conn.commit()
                        #print("Inserted Succesfully")
                    else:
                        pass
                    # print("There is some problem with the entered values")
                    


                except Exception as e:
                    conn.rollback()
                    print("This is the Error")

                    print(str(e))
                    print("Contact Admin for resolution")

            except Exception as e:
                print("\n Authentication Failed")
                print(str(e))
                print("\n Contact Admin for resolution")
                ex=1


                




            #obj.__init__()
            ans = 'y'
            while(ans != 'z' and ex==0):

                obj = DatabaseProjectStores(conn)
                print("\n \n")

                print("Menu : ")
                print("Enter")


                print("a: Search Housing projects ")
                print("b: To Display buildings, retail store & hospitals by pincode ")
                print("c: Find retail store or Hospitals or Projects Near you")
                print("d: Search schools by pincode (Non-relational Database)")
                print("e: Display Table ")
                print("f: Insert Data in Retail Store ")
                print("g: View Number of Hospitals, Retail Store and Projects at a Pincode")
                print("h: Group Hospital & Housing Projects by Borough ")
                print("i: View Audit tables (Admin only) ")
                print("j: View User Logs (Admin only) ")

                print("\n ")
                print("Enter z to Exit")
                ans = input()
                if(ans == 'z'):
                    print("Thank you.  Exited!!!!")
                    break_flag=True


                elif(ans == "a"):
                    print("\n ")
                    flag = 'y'

                    while(flag != 'z'):
                        print("\n \n")

                        print("Menu : ")
                        print("Enter")


                        print("1: Search projects by project id ")
                        print("2: Search projects by project pincode ")
                        print("3: Search projects by project name")
                        print("4: Search projects by project start date after a particular date ")
                        print("Enter z to move to Main Menu")


                        flag = input()
                        if(flag == 'z'):
                            break
                        elif(flag == "2"):
                            print("\n ")
                            obj.search_projects_zipcode()
                        elif(flag == "1"):
                            print("\n ")
                            obj.search_projects_project_id()
                        elif(flag == "3"):
                            print("\n ")
                            obj.search_projects_name()
                        elif(flag == "4"):
                            print("\n ")
                            obj.search_projects_date()                
                            
                        else:
                            print("Nothing Matches, Enter Again")



                elif(ans == "b"):
                    obj.search_zipcode()

                elif(ans == "c"):
                    
                    print("\n ")
                    flag = 'y'

                    while(flag != 'z'):
                        print("\n \n")

                        print("Menu : ")
                        print("Enter")


                        print("1: View Nearby Retail Stores ")
                        print("2: View Nearby Hospitals ")
                        print("3: View Nearby Projects")
                        print("Enter z to move to Main Menu")


                        flag = input()
                        if(flag == 'z'):
                            break
                        elif(flag == "2"):
                            print("\n ")
                            obj.search_hospitals_closest()
                        elif(flag == "1"):
                            print("\n ")
                            obj.search_retail_store_closest()
                        elif(flag == "4"):
                            print("\n ")
                            obj.search_school_closest()
                        elif(flag == "3"):
                            print("\n ")
                            obj.search_projects_closest()               
                            

                            
                        else:
                            print("Nothing Matches, Enter Again")





                elif(ans == "d"):
                    obj.search_school()

                elif(ans == "e"):
                    print("Table Names -:  project, house_description, retail_store, hospital, building_address, house_affordability")
                    obj.display_table()

                elif(ans == "f"):
                    obj.insert_retail_store()
                    
                elif(ans == "g"):
                    obj.search_all()
                elif(ans == "h"):
                    obj.search_borough()
                elif(ans == "i"):
                    

                    print("Table Names -:  project_audit, house_description_audit, retail_store_audit, hospital_audit, building_address_audit, house_affordability_audit")
                    obj.display_audit()

                elif(ans == "j"):
                    obj.display_user_logs()
                else:
                    print("Nothing Matches, Enter Again")

            


