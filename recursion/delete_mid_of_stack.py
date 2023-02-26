def del_mid_stack(stack_list, pos):
    if len(stack_list) == pos:
        stack_list.pop(0)
        return stack_list
    elif len(stack_list) > pos:
        ele = stack_list.pop(0)
        stack_list = del_mid_stack(stack_list, pos)
        stack_list.insert(0, ele)
        return stack_list


# another way to do the same:
# better way
def del_mid_stack_2(stack_list, pos):
    if pos==1:
        stack_list.pop(0)
        return stack_list
    else:
        ele = stack_list.pop(0)
        stack_list = del_mid_stack_2(stack_list, pos-1)
        stack_list.insert(0, ele)
        return stack_list


stack_list = [1,2,3,4,5]
mid_ele = int(len(stack_list) / 2) + 1
print(del_mid_stack_2(stack_list, mid_ele))
