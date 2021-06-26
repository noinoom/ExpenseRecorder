# basicsqlite3.py

import sqlite3

# สร้าง database
conn = sqlite3.connect('expense.sqlite3')
# สร้างตัวดำเนินการ (อยากได้อะไรใช้ตัวนี้ได้เลย)
c = conn.cursor()

# สร้าง table ด้วยภาษา SQL
'''
'รหัสรายการ (transactionid) TEXT',
'วัน-เวลา (datetime)' TEXT,
'รายการ'(title) TEXT,
'ค่าใช้จ่าย (expense) REAL (float)',
'จำนวน (quantity)' INTEGER,
'รวม (total) REAL'
'''
c.execute("""CREATE TABLE IF NOT EXISTS expenselist (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				transactionid TEXT,
				datetime TEXT,
				title TEXT,
				expense REAL,
				quantity INTEGER,
				total REAL
			)""")

def insert_expense(transactionid,datetime,title,expense,quantity,total):
	ID = None
	with conn:
		c.execute("""INSERT INTO expenselist VALUES (?,?,?,?,?,?,?)""",
			(ID,transactionid,datetime,title,expense,quantity,total))
	conn.commit() # การบันทึกข้อมูลลงในฐานข้อมูล ถ้าไม่รันตัวนี้จะไม่บันทึก
	print('Insert Success!')

def show_expense():
	with conn:
		c.execute("SELECT * FROM expenselist")
		expense = c.fetchall() #คำสั่งให้ดึงข้อมูลเข้ามา
		print(expense)
	
	return expense

def update_expense(transactinid,title,expense,quantity,total):
	with conn:
		c.execute("""UPDATE expenselist SET title =?,expense=?,quantity=?,total=? WHERE transactionid=?""",
		([title,expense,quantity,total,transactinid]))
	conn.commit()
	print('Data updated')

def delecte_expense(transactionid):
	with conn:
		c.execute("DELETE FROM expenselist WHERE transactinid=?",([transactionid,]))
	conn.commit()
	print('Data deleted')
#insert_expense('')
#update_expense('')
#delete_expense('')
#show_expense() # - R - READ


print('success')