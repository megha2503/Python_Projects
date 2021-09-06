import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY, title text,author text,year integer, isbn integer)")
        self.conn.commit()
        # conn.close()

    def insert(self,title,author,year,isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        self.conn.close()


    def view(self):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        # conn.commit()
        # self.conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
       # conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = cur.fetchall()
        #conn.commit()
        #self.conn.close()
        return rows

    def delete(self, year):
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        self.cur.execute("DELETE FROM books WHERE year=?",(year))
        self.conn.commit()
        #self.conn.close()

    def update(self, id,title,author,year,isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(id, title, author, year, isbn))
        self.conn.commit()
        self.conn.close()

    def __del__(self):
        self.conn.close()


#connect()
#insert("Angles and Demons","Dan Brown",1999,198987456)
#delete(1999)
#print(view())
#
#print(search(author="Michelle Obama"))