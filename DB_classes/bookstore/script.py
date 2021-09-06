# #connect to database
# #create a cursor object
# #Write an SQL query
# #Commit changes
# #close the connection
import sqlite3

def create_table():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(BASE_DIR, "lite.db")
    cur = conn.cursor()
    cur.execute("CREATE table if NOT EXISTS 'store'(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

insert("cofee bar", 10, 5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

# import mysql.connector
# word = input("Enter a word in English and press Enter: ")
# con = mysql.connector.connect(
#     user="ardit700_student", 
#     password = "ardit700_student", 
#     host="108.167.140.122", 
#     database = "ardit700_pm1database"
# )
# cursor = con.cursor()
# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
# results = cursor.fetchall()
# if results:
#     for result in results:
#         print(result[1])
# else:
#     print("We couldn't find any results about that.")
