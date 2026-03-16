# pip install mysql-connector-python

import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="expense_tracker3"
    )

    return connection

def add_expenses(date, category, amount, description):
    conn=connect_db()
    cursor=conn.cursor()

    query="""INSERT INTO expenses(date, category, amount, description) VALUES(%s, %s, %s, %s)"""

    values=(date, category, amount, description)

    cursor.execute(query,values)

    conn.commit()
    cursor.close()

    conn.close()


def get_expenses():
    conn=connect_db()
    cursor=conn.cursor()
    query="""SELECT * FROM expenses"""
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def delete_expense(expense_id):
    conn=connect_db()
    cursor=conn.cursor()

    query="DELETE FROM expenses  WHERE id= %s"
    cursor.execute(query,(expense_id,))
    conn.commit()
    cursor.close()
    conn.close()