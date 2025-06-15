# Convert Celsius to Fahrenheit or vice versa

choice = input("Convert to (C)elsius or (F)ahrenheit? ")

if choice.lower() == 'c':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", round(c, 2))
elif choice.lower() == 'f':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", round(f, 2))
else:
    print("Invalid choice")
