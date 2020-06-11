import sqlite3

def connect():
    conn=sqlite3.connect("store.db")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store ( id INTEGER PRIMARY KEY, title TEXT ,author TEXT, year integer, price integer)')
    conn.commit()
    conn.close()

def insert(title,author,year,price):
    conn=sqlite3.connect("store.db")
    cur=conn.cursor()
    cur.execute('INSERT INTO store VALUES (NULL,?,?,?,?)',(title,author,year,price))
    conn.commit()
    conn.close()

def viewall():
    conn=sqlite3.connect("store.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author='',year='',price=''):
    conn=sqlite3.connect("store.db")
    cur=conn. cursor()
    cur.execute("SELECT * FROM store WHERE title=? OR author=? OR year=? Or price=?",(title,author,year,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("store.db")
    cur=conn. cursor()
    cur.execute("DELETE FROM store WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,price):
    conn=sqlite3.connect("store.db")
    cur=conn. cursor()
    cur.execute("UPDATE store SET title=? ,author=?, year=?,price=? WHERE id=?",(title,author,year,price,id))
    conn.commit()
    conn.close()

connect()
