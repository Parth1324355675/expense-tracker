# # pip install mysql-connector-python

# import mysql.connector

# def connect_db():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="expense_tracker3"
#     )

#     return connection

# def add_expenses(date, category, amount, description):
#     conn=connect_db()
#     cursor=conn.cursor()

#     query="""INSERT INTO expenses(date, category, amount, description) VALUES(%s, %s, %s, %s)"""

#     values=(date, category, amount, description)

#     cursor.execute(query,values)

#     conn.commit()
#     cursor.close()

#     conn.close()


# def get_expenses():
#     conn=connect_db()
#     cursor=conn.cursor()
#     query="""SELECT * FROM expenses"""
#     cursor.execute(query)
#     result=cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return result

# def delete_expense(expense_id):
#     conn=connect_db()
#     cursor=conn.cursor()

#     query="DELETE FROM expenses  WHERE id= %s"
#     cursor.execute(query,(expense_id,))
#     conn.commit()
#     cursor.close()
#     conn.close()


# SQLite 
import sqlite3

# create connection
def get_connection():
    conn = sqlite3.connect("expenses.db")
    return conn


# create table if not exists
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()


# add expense
def add_expenses(date, category, amount, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )

    conn.commit()
    conn.close()


# fetch all expenses
def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    conn.close()
    return records


# delete expense
def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()


# create table automatically when file runs
create_table()