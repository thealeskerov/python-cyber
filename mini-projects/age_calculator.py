# Calculates age and days until next birthday

from datetime import datetime

# Ask user for birthdate
birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.today()

# Calculate age
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# Calculate days until next birthday
next_birthday = birth.replace(year=today.year)
if next_birthday < today:
    next_birthday = birth.replace(year=today.year + 1)
days_until_birthday = (next_birthday - today).days

# Display results
print(f"You are {age} years old.")
print(f"Days until your next birthday: {days_until_birthday}")
