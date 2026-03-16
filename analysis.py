import pandas as pd
import numpy as np

from database import get_expenses

def load_expenses():
    data=get_expenses()

    columns=['id','date', 'category', 'amount', 'description']
    df=pd.DataFrame(data,columns=columns)
    return df

def total_expense(df):
    return df["amount"].sum()

def category_expense(df):
    return df.groupby('category')['amount'].sum()

def daily_expense(df):
    return df.groupby("date")["amount"].sum()



def monthly_expense(df):
    df["date"]=pd.to_datetime(df["date"])
    df["month"]=df["date"].dt.to_period("M")
    monthly=df.groupby('month')["amount"].sum()
    return monthly
