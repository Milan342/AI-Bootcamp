def factorial(number):
    result = 1
    for value in range(1, number + 1):
        result = result * value
    return result


number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", number, "is", factorial(number))
