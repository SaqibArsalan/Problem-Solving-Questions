
def factorial_using_for_loop(num):
    fact = 1

    for i in range(1, num+1):
        fact *= i

    return fact

print(factorial_using_for_loop(3))