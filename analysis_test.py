from analysis import load_expenses,total_expense,category_expense,daily_expense

df=load_expenses()
print("Data")
print(df)

print("\nTotal expenses:")
print(total_expense(df))

print("\nCategory Expense:")
print(category_expense(df))


print("\nDaily Expense")
print(daily_expense(df))