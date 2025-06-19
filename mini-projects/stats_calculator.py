# Calculates basic statistics from a list of numbers

import statistics

def get_numbers():
    raw = input("Enter numbers separated by commas: ")
    return [float(num.strip()) for num in raw.split(",")]

# Get user input
nums = get_numbers()

# Display statistics
print(f"Count: {len(nums)}")
print(f"Mean: {statistics.mean(nums)}")
print(f"Median: {statistics.median(nums)}")
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
print(f"Standard Deviation: {statistics.stdev(nums)}")
