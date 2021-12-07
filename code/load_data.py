import psycopg2
import preprocessing
import load
# creating schema
def load_everything():
    # loadign scheme
    #connection_string = "dbname=%s user=%s password=%s host=%s port=%s" % ('project',user,pas,'127.0.0.1','5433')
    connection_string = " user = 'admin' password = 'admin'  host = '127.0.0.1'  port = '5433' dbname = 'project' "
    #connection_string = " user = 'agtuxdlalnzqgd' password = '1da65b17677151a3d0ef958a156021d37672cb8668ca7f5eab3aca5096afd669'  host = 'ec2-54-158-232-223.compute-1.amazonaws.com'  port = '5432' dbname = 'dc26hii2bqkpr5' "
    conn = psycopg2.connect(connection_string)
    # with conn.cursor() as cursor:
    #     setup_queries = open('database.sql', 'r').read()
    #     cursor.execution_options(isolation_level="AUTOCOMMIT").execute(setup_queries)
    #     conn.commit()


    with conn.cursor() as cursor:
        setup_queries = open('code/schema.sql', 'r').read()
        cursor.execute(setup_queries)
        conn.commit()
    # preprocess the data
    preprocessing.preprocess()
    # loading csv into database
    load.load_into_database()
    

if __name__ == "__main__":
    load_everything()