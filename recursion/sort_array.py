def insert_(arr, ele):
    if len(arr) == 0 or ele >= arr[-1]:
        arr.insert(len(arr), ele)
        return arr
    temp = arr[-1]
    arr.pop()
    arr = insert_(arr, ele)
    arr.insert(len(arr), temp)
    return arr


def sort_(arr):
    if len(arr) == 1:
        return arr
    else:
        ele = arr[-1]
        arr.pop()
        sorted_arr = sort_(arr)
        arr = insert_(sorted_arr, ele)
        return arr


array_ = [8, 5, 3, 2, 7, 6, 1]
arr_2 = [1, 3, 5, 7, 9]
print(sort_(array_))