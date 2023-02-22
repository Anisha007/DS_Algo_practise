"""
The stock span problem is a financial problem where we have a series of N daily price quotes
for a stock and we need to calculate the span of the stock’s price for all N days. The span Si of the stock’s price
on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price
of the stock on the current day is less than its price on the given day.
Input: N = 7, price[] = [100 80 60 70 60 75 85]
Output: 1 1 1 2 1 4 6
So we need to find the consecutive smaller or equal before it
"""


def NGL_index_computaion(arr):
    res_index_arr = [-1 for i in range(len(arr))]
    stack = list()
    for i in range(0, len(arr)):
        while len(stack) > 0 and arr[stack[0]] < arr[i]:
            stack.pop(0)
        res_index_arr[i] = -1 if len(stack) == 0 else stack[0]
        stack.insert(0, i)

    return res_index_arr


def stock_span(arr):
    NGL_index = NGL_index_computaion(arr)
    res_arr = []
    for i in range(0, len(arr)):
        res_arr.insert(i, (i - NGL_index[i]))
    return res_arr


if __name__ == '__main__':
    input_ = input("Enter the array elements\n")
    input_arr = [int(ele) for ele in input_.split(',')]
    result = stock_span(input_arr)
    print(result)
