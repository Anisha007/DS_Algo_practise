# given a sting or array of integer, get subst


def subset(ip, op):
    if len(ip) == 0:
        print(op)
        return
    else:
        op_skip_ele = op
        op_take_ele = (*op, ip[0])
        ip = ip[1:]
        subset(ip, op_skip_ele)
        subset(ip, op_take_ele)


def subset_global(ip, op):
    if len(ip) == 0:
        res.append(op)
        return
    else:
        op_skip_ele = op
        op_take_ele = (*op, ip[0])
        ip = ip[1:]
        subset_global(ip, op_skip_ele)
        subset_global(ip, op_take_ele)


def subset_return(ip, i=0):
    if len(ip) == 0:
        return [()]
    else:
        ip_new = ip[1:]
        op = subset_return(ip_new)
        op2 = ((ip[0], *i) for i in subset_return(ip_new))
        return (*op, *op2)


def subset_return_process_from_last(ip):
    if len(ip) == 0:
        return [()]
    else:
        ip_new = ip[:-1]
        op = subset_return_process_from_last(ip_new)
        op2 = ((*i, ip[-1]) for i in subset_return_process_from_last(ip_new))
        return (*op, *op2)


res = []
ip1 = ('a', 'a', 'c')
op1 = ()
print((subset_return(ip1)))
# print(res)
# ('b', 'c')

"""
3 ways the function can be implemented
1. print at base location
2. use a global variable and store the output during base condition
3. return the entire output as tuple of tuple
"""

# def get_subset(input_, output):
#     if len(input_) == 0:
#         print(output)
#         return
#     output1 = output
#     output2 = (*output, input_[0])
#     n = 0
#     input_ = input_[1:]
#     get_subset(input_, output1)
#     get_subset(input_, output2)
#
#
# get_subset(('a','b','c'), ())
