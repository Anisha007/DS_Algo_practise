def print_fn(n):
    if n == 1:
        print("1")
        return
    print_fn(n - 1)
    print(n)


def print_fn_rev(n):
    if n == 1:
        print("1")
        return
    print(n)
    print_fn_rev(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


