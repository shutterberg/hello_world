#Novin Misquith ,St Joseph Engineering College Mangalore
import sqlite3 as db
from sqlite3 import Error

#defining a fuinction to create a connection with sqlite and error handling
def create_conn(table_name):    
    conn=None
    try:
        conn = db.connect(table_name)
        print("Successfully Connected.")
    except Error as e:
        print(e)
    return conn


# function to execute query with error handling
def execute_query(conn,sql):    
    cur=None
    try:
        cur=conn.execute(sql)
        print("Query Successfully Executed.")
    except Error as e:
        print(e)
    return cur


# function to display the result of an query by passing cursor object
def display(cur):              
    print("")
    for row in cur:
        print(row)


#create table query
create_table_query='''CREATE TABLE MOVIES ( 
    ID INTEGER PRIMARY KEY,
    MOV_NAME VARCHAR(20),
    MOV_ACTOR VARCHAR(25),
    MOV_ACTRESS VARCHAR(25),
    MOV_YEAR INTEGER,
    MOV_DIRECTOR VARCHAR(25))
    '''

#insert data queries
insert_data1_query='''INSERT INTO 
MOVIES(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) 
VALUES ('Tennet','John Washington','Elizabeth Debicki',2020,'Christopher Nolan')'''
insert_data2_query='''INSERT INTO 
MOVIES(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) 
VALUES ('Inception','Leonardo DiCaprio','Marion Cotillard',2010 ,'Christopher Nolan')'''
insert_data3_query='''INSERT INTO 
MOVIES(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) 
VALUES ('Interstellar','Matthew McConaughey','Anne Hathaway',2014 ,'Christopher Nolan')'''
insert_data4_query='''INSERT INTO 
MOVIES(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) 
VALUES ('Mugen Train','Tanjirō Kamado','Nezuko Kamado',2020 ,'Haruo Sotozaki')'''
insert_data5_query='''INSERT INTO 
MOVIES(MOV_NAME,MOV_ACTOR,MOV_ACTRESS,MOV_YEAR,MOV_DIRECTOR) 
VALUES ('Blame!','Killy','Cibo',2017 ,'Hiroyuki Seshita')'''


#display queries
display_all_query='''SELECT * FROM MOVIES'''
display_actor_query='''SELECT * FROM MOVIES 
WHERE MOV_ACTOR='Killy' '''
display_director_query='''SELECT * FROM MOVIES 
WHERE MOV_DIRECTOR='Christopher Nolan' '''


#creating connection with data base
conn=create_conn("fav_movie")


#executing create table and insertion queries
execute_query(conn,create_table_query)
execute_query(conn,insert_data1_query)
execute_query(conn,insert_data2_query)
execute_query(conn,insert_data3_query)
execute_query(conn,insert_data4_query)
execute_query(conn,insert_data5_query)

#SELECT queries and display results
print("\nDisplay All")
cur=execute_query(conn,display_all_query)
display(cur)

print("\nDisplay by Actor Killy")
cur=execute_query(conn,display_actor_query)
display(cur)

print("\nDisplay by Director Christoper Nolan")
cur=execute_query(conn,display_director_query)
display(cur)

#closing Connection
conn.close()
