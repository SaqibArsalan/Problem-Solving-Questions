def factorial_with_recursion(n):
    if n == 1:
        return n
    else:
        return n * factorial_with_recursion(n -1)


print(factorial_with_recursion(6))