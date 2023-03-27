"""
print n digit binary number where no. of 1s>= no. of zeros for all prefix
"""


def gen_prefix_numbers_backtrack2(ip, n):
    if ip[0] + ip[1] == n:
        return [""]
    ip[1] += 1
    op_list = gen_prefix_numbers_backtrack2(ip, n)
    for i in range(len(op_list)):
        op_list[i] = "1" + op_list[i]
    ip[1] -= 1
    op_list2 = []
    if ip[1] > ip[0]:
        ip[0] = ip[0] + 1
        op_list2 = gen_prefix_numbers_backtrack2(ip, n)
        for i in range(len(op_list2)):
            op_list2[i] = "0" + op_list2[i]
        ip[0] = ip[0] - 1
    op_list.extend(op_list2)
    return op_list


def gen_prefix_numbers_backtrack1(ip, op, n):
    if ip[0] + ip[1] == n:
        return [op]
    ip[1] += 1
    op_list = gen_prefix_numbers_backtrack1(ip, op + "1", n)
    ip[1] -= 1
    op_list2 = []
    if ip[1] > ip[0]:
        ip[0] = ip[0] + 1
        op_list2 = gen_prefix_numbers_backtrack1(ip, op + "0", n)
        ip[0] = ip[0] - 1
    op_list.extend(op_list2)
    return op_list


def gen_prefix_numbers(ip, op, n):
    if ip[0] + ip[1] == n:
        print(op)
        return
    if ip[0] == ip[1]:
        ip[1] += 1
        op = op + "1"
        gen_prefix_numbers(ip, op, n)
    else:
        ip1 = ip.copy()
        ip2 = ip.copy()
        ip1[0] = ip1[0] + 1
        gen_prefix_numbers(ip1, op + "0", n)
        ip2[1] = ip2[1] + 1
        gen_prefix_numbers(ip2, op + "1", n)


n = 4
ip = [0, 0]
op = ""
print(gen_prefix_numbers_backtrack2(ip, n))
# print([].append("op"))
