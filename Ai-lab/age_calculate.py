from datetime import date

# Input date of birth
year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

dob = date(year, month, day)
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is:", age)