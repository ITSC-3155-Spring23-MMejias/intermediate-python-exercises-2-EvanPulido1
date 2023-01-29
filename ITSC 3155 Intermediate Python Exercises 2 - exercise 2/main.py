# Evan Pulido
# ITSC 3155

# Fibonacci sequence is a series of numbers where the next number is
# found by adding the two numbers before it

# I learned how to get the time it took for implementation to complete with
# https://www.tutorialspoint.com/time-process-time-function-in-python
import time

# A function that gives a a number from the fibonacci sequence
# The number provided by the user will determine which fibonacci number will be returned
def fibonacci(n):
    # If the number is 0 then return 0
    # This is the first number in the fibonacci series
    if n == 0:
        return 0
    # If the number is 1 or 2 then return 1
    # These two values are the second and third number in the fibonacci series
    elif n == 1 or n == 2:
        return 1
    
    # This is a recursion that gives a number by adding the two previous two numbers before it
    return fibonacci(n-1) + fibonacci(n-2)

# Ask the user to enter an n value, it must be from 15 and 35 inclusive
# Link that helped me with the while true loop:
# https://www.geeksforgeeks.org/how-to-use-while-true-in-python/
while True:
    # Ask the user to enter integer and if it is not 15-35 then print error message and ask the user again
    # Link that helped me learn assert: https://www.w3schools.com/python/ref_keyword_assert.asp
    try:
        number = int(input('Enter a number between 15 and 35: '))
        assert 15 <= number <= 35
        break
    except AssertionError:
        print('Integer must be between 15 and 35.')

# Print the fibonacci number
# Print the time it took for the implementation to occur
print('fib(' + str(number) + ')= ' + str(fibonacci(number)))
print('fib(' + str(number) + ') took ' + str(time.process_time()) + ' seconds')