def test(*params):
    print(params)

test(1, 2, 3, True, 'string')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))