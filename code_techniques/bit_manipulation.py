# left shift operation: multiply by 2
rn = 5
for k in range(rn):
    print(k)
    print((1 << k))

# right shift operation divide by 2
rn = 4
ele = 95
for k in range(rn):
    print(k, ele >> k)

# number representation
print(15, 0b1111, 0xF)
print(0b101 * 0b1010)

"""
Bit manipulation concepts:
check: check(n, 0) or check(n, 1) :  check if the nth bit is set or unset
set(n): set the nth bit to 1
unset(n)/reset(n): set the nth bit to 0
toggle(n): change form 0 to 1 and vice versa
"""

print(bin(15))
num = 0b1100011
k = 3


# "setting k position in the number"
def set(num, k):
    if k == -1:
        return num
    num = num | (1 << k)
    a = set(num, k - 1)
    return a


print(bin(set(num, k)))


# unset or reset

def reset(num, k):
    a = num & ~(1 << k)
    return a


num = 0b1111101
print(bin(reset(num, k)))


def check_set(num, k):
    a = num & (1 << k)
    # num = 1111 k=2  a = 0b01000
    # num = 1011 k=2  a = 0b0000
    # if kth bit is 0, the operation evaluates tgo 0
    # else operation evaluates to non zero i.e 2^k
    return True if a != 0 else False


print(check_set(num, 3))


def toggle(num, k):
    a = num ^ (1 << k)
    print(bin(num), bin(a), k)
    return a


print(bin(toggle(num, 3)))
