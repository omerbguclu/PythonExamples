import sqlite3
import random
import time
import datetime

con=sqlite3.connect('Dersler.db')
cursor=con.cursor()

def tablooo():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

def rastgelee():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime='python sqlite'
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger)VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

def degeral():
    cursor.execute ('SELECT * FROM Tablo1 WHERE deger=0')
    data=cursor.fetchall()
    for i in data:
        print(i)

def update():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Old Datas------------")
    for i in data:
        print(i)
    cursor.execute("UPDATE Tablo1 SET deger=99 WHERE deger=0")
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("New Datas------------")
    for i in data:
        print(i)

def delete():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Old Datas------------")
    for i in data:
        print(i)
    cursor.execute("DELETE FROM Tablo1 WHERE deger=0")
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("New Datas------------")
    for i in data:
        print(i)


delete()
#con.commit()//this command will make permanent the datas which is processed
con.close()