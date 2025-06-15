# Print the multiplication table for a number

# Get the number from user
num = int(input("Enter a number: "))

# Loop from 1 to 10 and multiply
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
