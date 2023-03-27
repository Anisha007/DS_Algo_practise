"""
Given a string "abc" or an array, include space in between the character
OUTPUT
"a b c"
"a bc"
"ab c"
"abc"
"""


# def permutation_with_space_using_list(ip):

def permutation_with_space_using_string(ip, op):
    if len(ip) == 0:
        print(op)
        return
    else:
        op_take_space = op + '_' + ip[0]
        op_skip_space = op + ip[0]
        ip_new = ip[1:]
        permutation_with_space_using_string(ip_new, op_take_space)
        permutation_with_space_using_string(ip_new, op_skip_space)


if __name__ == '__main__':
    ip = input("Enter string\n")
    op = ""
    # we will insert the 1st character
    if len(ip) <= 1:
        op = ip
        print(op)
    # for first element processing
    op = op.join(ip[0])
    ip_new = ip[1:]
    permutation_with_space_using_string(ip_new, op)
    # op_tuple =
