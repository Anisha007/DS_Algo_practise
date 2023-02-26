def insert_(arr, ele):
    print(arr)
    if len(arr) == 0 or ele <= arr[0]:
        arr.insert(0, ele)
        return arr
    temp = arr[0]
    arr.pop(0)
    arr = insert_(arr, ele)
    arr.insert(0, temp)
    return arr


def sort_(arr):
    if len(arr) == 1:
        return arr
    else:
        ele = arr[0]
        arr.pop(0)
        sorted_arr = sort_(arr)
        arr = insert_(sorted_arr, ele)
        return arr


array_ = [8, 5, 3, 2, 7, 6, 1]
arr_2 = [1, 3, 5, 7, 9]
print(sort_(array_))
# print(insert_(arr_2, 2))