"""
This script is to find the following:
1. nearest greatest element to left
2. nearest greatest element to right
3. nearest smallest element to left
4. nearest smallest element to right
"""


def nearest_greatest_element_to_left(arr, implementation_type="OPT"):
    """
    :param arr: input array 
    :param implementation_type: indicates the type of implementation which we want to run 
    :return: result array
    """
    res_array = [-1 for i in range(len(arr))]
    # brute force implementation
    if implementation_type == "BF":
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[i]:
                    res_array[i] = arr[j]
                    break
    else:
        stack = list()
        for i in range(len(arr)):
            while len(stack) > 0 and arr[i] >= stack[0]:
                stack.pop(0)
            res_array[i] = -1 if len(stack) == 0 else stack[0]
            stack.insert(0, arr[i])
    return res_array


def nearest_greatest_element_to_right(arr, implementation_type="OPT"):
    """
    :param implementation_type: indicates the type of implementation which we want to run
    :param arr: input array
    :return: result array
    """
    res_arr = [-1 for i in range(len(arr))]
    # Brute force(BF) implementation
    if implementation_type == "BF":
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    res_arr[i] = arr[j]
                    break
    else:
        stack = list()
        # since it is a stack implementation and we are finding the greatest element,
        # we will focus on stack right to left
        for i in range(len(arr) - 1, -1, -1):
            # if len(stack) == 0:
            #     stack.insert(0, arr[i])
            # elif stack[0] > arr[i]:
            #     res_arr[i] = stack[0]
            # else:
            # the above few lines are redundant lines
            while len(stack) > 0 and stack[0] <= arr[i]:
                stack.pop(0)
            res_arr[i] = -1 if len(stack) == 0 else stack[0]
            stack.insert(0, arr[i])

    return res_arr


def nearest_smallest_element_to_left(arr, implementation_type="OPT"):
    """
    :param arr: input array
    :param implementation_type: BF or OPT
    :return: result array
    """
    result_array = [-1 for i in range(len(arr))]
    if implementation_type == "BF":
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i]:
                    result_array[i] = arr[j]
                    break
    else:
        stack = list()
        for i in range(len(arr)):
            while len(stack) > 0 and arr[i] < stack[0]:
                stack.pop(0)
            result_array[i] = -1 if len(stack) == 0 else stack[0]
            stack.insert(0, arr[i])
    return result_array


def nearest_smallest_element_to_right(arr, implementation_type="OPT"):
    """
    :param arr: input array
    :param implementation_type:BT or OPT
    :return: result array
    """
    res_arr = [-1 for i in range(len(arr))]
    if implementation_type == "BF":
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    res_arr[i] = arr[j]
                    break
    else:
        stack = list()
        for i in range(len(arr) - 1, -1, -1):
            while len(stack) > 0 and arr[i] < stack[0]:
                stack.pop()
            res_arr[i] = -1 if len(stack) == 0 else stack[0]
            stack.insert(0, arr[i])
    return res_arr


if __name__ == '__main__':
    input_num = int(input(" Enter 1 for nearest greatest element to left\n "
                          "Enter 2 for nearest greatest element to right \n "
                          "Enter 3 for nearest smallest element to left \n "
                          "Enter 4 for  nearest smallest element to right\n"))
    input_opt = input("Enter BF for Brute Force Implementation and OPT or anything else for optimal implementation\n")
    input_ = input("Enter the array elements separated by comma\n")
    array_input = [elm for elm in input_.split(',')]
    result = []
    if input_num == 1:
        result = nearest_greatest_element_to_left(array_input, input_opt)
    elif input_num == 2:
        result = nearest_greatest_element_to_right(array_input, input_opt)
    elif input_num == 3:
        result = nearest_smallest_element_to_left(array_input, input_opt)
    elif input_num == 4:
        result = nearest_smallest_element_to_right(array_input, input_opt)
    else:
        print("Invalid Input")
    print(result)