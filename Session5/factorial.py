n = 5 # Number whose factorial we want to calculate
fact = 1 # Initialize factorial to 1

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    fact *= i # Multiply fact by the current number

# Display the calculated factorial
print(f"Factorial of {n} = {fact}")