# basicsqlite3.py

import sqlite3

# สร้าง database
conn = sqlite3.connect('expense.sqlite3')
#สร้างตัวดำเนินการ (อยากได้อะไรใช้ตัวนี้ได้เลย)
c = conn.cursor()

# สร้าง table ด้วยภาษา SQL


c.execute("""CREATE TABLE IF NOT EXISTS expenselist (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                transactionid TEXT,
                datatime TEXT,
                title TEXT,
                expense REAL,
                quantity INTEGER,
                total REAL
            )""")


def insert_expense(transactionid, datetime, title, expense, quantity, total):
    ID = None
    With conn:
        c.excute("""INSERT INTO expenslist VALUES (?,?,?,?,?,?,?)""",
                 (ID, transactionid, datetime, title, expense, quantity, total))
    conn.commit()  # การบันทึุกข้อมูลลงในฐานข้อมูล

print('success')
