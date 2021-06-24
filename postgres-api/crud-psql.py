import psycopg2
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://github.com/Supriya-Konijeti,',
                        auth=HTTPBasicAuth('Supriya-Konijeti', 'Priyak@33'))
print(response)


def Insert():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    cur = conn.cursor()
    ID = int(input("Enter id.. "))
    name = input("Enter Name... ")
    location = input("Enter Location... ")

    cur.execute(
        "insert into Employee(id,name,location) values( %s,%s, %s)", (ID, name, location))
    conn.commit()
    conn.close()
    return "Record inserted into table"


def Retrive():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    cur = conn.cursor()

    retrive_by_id_query = '''
    select * from Employee
    '''

    cur.execute(retrive_by_id_query)
    rows = cur.fetchall()

    row_num = int(input("Enter required row number.. "))
    print(rows[row_num-1])
    """for r in rows:
        print (f"id = {r[0]}, name = {r[1]}, location = {r[2]}")"""

    conn.close()
    return "Record fetched successfully from table"


def Update():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    cur = conn.cursor()

    #row_num=int(input("Enter required row number.. "))
    update_query = '''
    update Employee set "name" = 'priya',location='hyderabad' where id=2
    '''

    """
    ID=int(input("Enter id to update.. "))
    name= input("Enter Name... ")
    location = input("Enter Location... ")
    """
    cur.execute(update_query)
    conn.commit()
    conn.close()
    return "Record updated into table"


def Delete():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    cur = conn.cursor()
    row_num = int(input("Enter required row number.. "))
    delete_query = '''
    delete from Employee where id=1
    '''

    cur.execute(delete_query)
    conn.commit()
    conn.close()
    return "Record is sucessfully deleted from table"


def errorHandling():
    return "Invalid Choice"


print('''
    1.Insert
    2.Retrive
    3.Update
    4.Delete
    0.Exit
    ''')

choice = int(input("Enter your choice..  "))
# while choice != 0:
operations = {
    1: Insert,
    2: Retrive,
    3: Update,
    4: Delete
}
output = operations.get(choice, errorHandling)()
print(output)
