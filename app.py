# pip install streamlit

# Step 5.3 — Create Basic Streamlit App

import streamlit as st
from database import add_expenses
from analysis import load_expenses,category_expense,daily_expense
from analysis import monthly_expense
from database import delete_expense



st.title("Expense Tracker Dashboard")
st.write("Welcome to your expense tracker!")


side_bar=st.sidebar.selectbox("Navigation",["Dashboard","Add expense","View expenses","Analytics"])


df=load_expenses()


# Step 5.4 — Add Expense Form

# st.header("Add New expense")

# date=st.date_input("Date")

# category=st.selectbox("Category",["Food", "Travel", "Shopping", "Bills", "Other"])

# amount=st.number_input("amount")

# description=st.text_input("Description")

# if st.button("Add Expense"):
#     add_expenses(date,category,amount,description)
#     st.success("Expense added successfully")




# Step 5.5 — Show Expenses Table

# from analysis import load_expenses
# st.header("All Expenses")
# df=load_expenses()
# st.dataframe(df)



# Step 5.6 — Show Analytics

# from analysis import category_expense,daily_expense

# st.header("Expense Analytics")

# st.subheader("Categorical Spending")
# cat_dat=category_expense(df)
# st.bar_chart(cat_dat)


# st.subheader("daily Spending")
# daily_data=daily_expense(df)
# st.line_chart(daily_data)



if side_bar=="Dashboard":
    st.header("Overview")

    total = df["amount"].sum()

    st.metric("Total Expense", total)


        # if menu == "Dashboard":
# KPI cards
    st.header("Expense Overview")

    total_expense = df["amount"].sum()
    total_transactions = len(df)
    avg_expense = df["amount"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Expenses", f"₹{total_expense}")
    col2.metric("Transactions", total_transactions)
    col3.metric("Average Expense", f"₹{round(avg_expense,2)}")

    st.write("Recent Expenses")




    # Budget tracker
    #    
    st.subheader("Budget Tracker")



    budget = st.number_input("Enter Monthly Budget", value=10000)

    remaining = budget - total_expense



    st.write(f"Remaining Budget: ₹{remaining}")

    progress = total_expense / budget

    st.progress(min(progress,1.0))



#  For last 5 records
    st.dataframe(df.tail())

    # Category spending %

    st.subheader("Category Distribution")

    category_data = df.groupby("category")["amount"].sum()

    st.bar_chart(category_data)


    # RECENT TRANSACTION:


    st.subheader("Recent Transactions")

    st.dataframe(df.sort_values("date", ascending=False).head(5))








elif side_bar=="Add expense":
    st.header("Add New Expense:")
    date = st.date_input("Date")

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    amount = st.number_input("Amount")

    description = st.text_input("Description")

    if st.button("Add Expense"):
        add_expenses(date, category, amount, description)
        st.success("Expense Added Successfully!")


elif side_bar=="View expenses":
    st.header("View Expenses:")
    st.dataframe(df)

    categories=df["category"].unique()
    select_category=st.selectbox("Filter by category",["All"]+list(categories))

    start_date=st.date_input("Start date:")
    end_date=st.date_input("End Date:")
    min_amount=st.number_input("Minimum Amount:",value=0)
    filter_df=df.copy()



    
    if select_category!="All":
        filter_df=filter_df[filter_df["category"]==select_category]
        filter_df["date"]=filter_df["date"].astype(str)
        filter_df = filter_df[filter_df["amount"] >= min_amount]

    st.subheader("Filtered Results")
    st.dataframe(filter_df)






    # Export extense report to csv

    st.subheader("Download Report")
    csv=df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Extense Report",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )





    # from database import delete_expense

    st.subheader("Delete Expenses:")
    expense_ids=df['id'].tolist()
    selected_id=st.selectbox("Select expense id to delete",expense_ids)
    if st.button("Delete Expense"):
        delete_expense(selected_id)
        st.success("Expense deleted successfully")
        


    



elif side_bar=="Analytics":
    st.header("Expense Analytics:")

    # category chart
    st.subheader("Category Spending")
    cat_data=category_expense(df)
    st.bar_chart(cat_data)

    # daily chart
    st.subheader("Daily Expense Trend")
    daily_data=daily_expense(df)
    st.line_chart(daily_data)

    # monthly report

    # from analysis import monthly_expense
    st.subheader("Monthly Expense Report")
    monthly_data=monthly_expense(df)
    st.bar_chart(monthly_data)




    st.subheader("Total Month Spending")

    for month,value in monthly_data.items():
        st.write(f"{month}: Rs.{value}")


    # Top spending category

    st.subheader("Top spending Category")
    top_category=df.groupby("category")["amount"].sum().idxmax()
    st.write(top_category)





