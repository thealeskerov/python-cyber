# Password Strength Checker using regex

import re

def check_password_strength(password):
    strength = 0

    # Check different password features
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Evaluate the strength
    if strength <= 2:
        return "Weak"
    elif strength in [3, 4]:
        return "Moderate"
    else:
        return "Strong"

# User input
pwd = input("Enter a password to check: ")
print("Password strength:", check_password_strength(pwd))
