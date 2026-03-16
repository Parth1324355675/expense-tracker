from database import get_expenses

records=get_expenses()

for row in records:
    print(row)