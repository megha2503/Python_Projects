import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY, title text,author text,year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    #conn.commit()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows = cur.fetchall()
    #conn.commit()
    conn.close()
    return rows

# def delete():
#     conn = sqlite3.connect("books.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM books WHERE year=?",(year))
#     conn.commit()
#     conn.close()

def update():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(id, title, author, year, isbn))
    conn.commit()
    conn.close()

connect()
#insert("Angles and Demons","Dan Brown",1999,198987456)
#delete(1999)
#print(view())

print(search(author="Michelle Obama"))