
def factorial_using_for_loop(num):
    fact = 1

    if num < 0:
        print("Not possible")
        return -1

    elif num == 0:
        return 1

    else:
        for i in range(1, num+1):
            fact *= i

    return fact


print(factorial_using_for_loop(0))