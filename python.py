#write a function to find Average of numbers
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Test the calculate_average function
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average:", average)
