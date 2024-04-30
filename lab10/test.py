import psycopg2
import csv
from config import host,user,password,db_name,port

try:
    connection=psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit=True
##creating
#    with connection.cursor() as cursor:
#        cursor.execute(
#            """CREATE TABLE phonebook(
#            id SERIAL PRIMARY KEY,
#            first_name varchar(32) NOT NULL,
#            last_name varchar(32) NOT NULL,
#            phone_num varchar(11)
#        );"""
#        )

#insert terminal
    # with connection.cursor() as cursor:
    #     data=(input("First Name:"),input("Last Name:"),input("Phone Number:"))
    #     cursor.execute(
    #          """INSERT INTO phonebook(first_name,last_name,phone_num) VALUES (%s,%s,%s);""",data
    # )
    # print("Data from terminal inserted")

# #insert from csv
#     with open('tablephone.csv','r') as file:
#         a=csv.reader(file)
#         for data in a:
#             with connection.cursor() as cursor:
#                 cursor.execute(
#              """INSERT INTO phonebook(first_name,last_name,phone_num) VALUES (%s,%s,%s);""",data
#     )
#     print("Data from csv inserted")

#delete data
    name=input("Name to delete")
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM phonebook WHERE first_name=%s""",(name,)
        )
        print("Data has been deleted")

except Exception as _ex:
    print("error ",_ex)
finally:
    if connection:
        connection.close()
        print("Closed")
