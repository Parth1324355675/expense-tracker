# Expense Tracker Dashboard

This project is a web-based expense tracker built using Python and Streamlit. 
It helps users record daily expenses, analyze spending patterns, and track their monthly budget.

## Features

- Add new expenses with date, category, amount, and description
- View all expenses in a table
- Delete expenses
- Filter expenses by category and amount
- Download expense report as CSV
- Track monthly budget
- View expense analytics using charts

## Technologies Used

- Python
- Streamlit
- MySQL
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

app.py → Main Streamlit application that creates the dashboard and user interface.

database.py → Handles database connection and operations like adding, deleting, and retrieving expenses.

analysis.py → Processes the expense data and performs calculations such as total expenses, category-wise expenses, and monthly analysis.

charts.py → Generates charts and visualizations such as pie charts, bar charts, and line charts to show spending patterns.



## app.py

This file is the main application of the project. It uses Streamlit to create the web interface.

Functions of this file:
- Creates the dashboard layout
- Allows users to add new expenses
- Displays expense tables
- Shows analytics and charts
- Allows filtering and deleting expenses
- Tracks the user’s monthly budget


## database.py

This file manages the connection between the application and the MySQL database.

Main functions:
- connect_db() → Connects to the MySQL database
- add_expenses() → Inserts new expense records
- get_expenses() → Retrieves all expense data
- delete_expense() → Deletes an expense by ID


## analysis.py

This file is responsible for analyzing expense data using Pandas.

Main functions:
- load_expenses() → Loads data from the database into a Pandas DataFrame
- total_expense() → Calculates total expenses
- category_expense() → Calculates expenses grouped by category
- daily_expense() → Calculates expenses for each day
- monthly_expense() → Calculates expenses for each month


## charts.py

This file creates visualizations of expense data using Matplotlib and Seaborn.

Charts included:
- Pie Chart → Shows expense distribution by category
- Bar Chart → Displays category-wise expenses
- Line Chart → Shows daily expense trends


## Database Schema

Table: expenses

Columns:
- id (INT) → Unique expense ID
- date (DATE) → Date of the expense
- category (VARCHAR) → Expense category
- amount (FLOAT) → Expense amount
- description (TEXT) → Additional details


## How to Run the Project

1 Install required libraries

pip install streamlit pandas matplotlib seaborn mysql-connector-python

2 Run the application

streamlit run app.py