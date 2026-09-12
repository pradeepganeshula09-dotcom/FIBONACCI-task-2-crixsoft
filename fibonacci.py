# Fibonacci Series Generator
# Crixsoft Solution - Python Development Internship

def fibonacci(n):
    """Generate the first n numbers of the Fibonacci series."""

    first = 0
    second = 1

    series = []

    for i in range(n):
        series.append(first)

        # Calculate the next Fibonacci number
        next_number = first + second
        first = second
        second = next_number

    return series


# Main program
print("=" * 40)
print("       FIBONACCI SERIES GENERATOR")
print("=" * 40)

try:
    n = int(input("Enter the number of terms: "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        result = fibonacci(n)

        print("\nFibonacci Series:")
        print(" → ".join(map(str, result)))

except ValueError:
    print("Invalid input! Please enter a whole number.")
