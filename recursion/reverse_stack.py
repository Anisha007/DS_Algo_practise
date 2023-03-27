def insert_fun(stack_arr, ele):
    if len(stack_arr)==0:
        stack_arr.insert(0, ele)
        return stack_arr
    else:
        e = stack_arr.pop(0)
        stack_arr = insert_fun(stack_arr, ele)
        stack_arr.insert(0, e)
        return stack_arr


def reverse_stack(stack_arr):
    if len(stack_arr)==1:
        return stack_arr
    ele = stack_arr.pop(0)
    stack_arr = reverse_stack(stack_arr)
    stack_arr = insert_fun(stack_arr, ele)
    return stack_arr


print(reverse_stack([1,2,3,4,5,6]))