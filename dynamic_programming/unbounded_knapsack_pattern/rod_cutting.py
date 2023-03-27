"""
given length and price and max length of rod, find the max value which can be obtained by cutting the rod
and selling them

"""


def solve(length, price, n, rod):
    if rod == 0:
        return 0
    if n == 0:
        return 0
    if rod < length[n - 1]:
        return solve(length, price, n - 1, rod)
    else:
        return max(solve(length, price, n - 1, rod), price[n - 1] + solve(length, price, n, rod - length[n - 1]))


length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
rod = 8
print(solve(length, price, n, rod))
