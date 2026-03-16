
from analysis import load_expenses,category_expense,daily_expense
import matplotlib.pyplot as plt
import seaborn as sns

# Step 4.4 — Category Expense Pie Chart


def category_pie_chart():
    df=load_expenses()
    data=category_expense(df)
    plt.pie(data,labels=data.index,autopct="%1.1f%%")
    plt.figure()
    plt.title("Expense Distribution by Category")
    plt.show()


# Step 4.5 — Category Bar Chart


def category_bar_chart():
    df=load_expenses()
    data=category_expense(df)
    sns.barplot(x=data.index,y=data.values)
    plt.figure()
    plt.title("Category Wise Expense")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

# Step 4.6 — Daily Expense Line Chart

def daily_line_chart():
    df=load_expenses()
    data=daily_expense(df)
    plt.plot(data.index,data.values,marker="o")
    plt.figure()
    plt.title("Daily Expense Trend")
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.show()

