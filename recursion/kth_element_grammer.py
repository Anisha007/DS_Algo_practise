def get_seq(arr, k):
    if k == 0:
        if arr[k] == 0:
            return [0, 1]
        else:
            return [1, 0]  # not required as starting is 0.

    else:
        seq_arr = get_seq(arr, k - 1)
        if arr[k] == 0:
            seq_arr.append(0)
            seq_arr.append(1)
            return seq_arr

        elif arr[k] == 1:
            seq_arr.extend([1, 0])
            return seq_arr


def gen_grammar(n):
    if n == 1:
        return [0]
    else:
        output = gen_grammar(n - 1)
        arr_res = get_seq(output, len(output) - 1)
        return arr_res


def kth_element_grammer(n, k):
    if k > n * n:
        print("Invalid")
        return
    res = gen_grammar(n)
    print(res, "\n", res[k])


def kth_element_grammar_2(n, k):
    if n == 1 and k == 1:
        return 0
    else:
        mid = int(pow(2, n - 1) / 2)
        if k <= mid:
            return kth_element_grammar_2(n - 1, k)
        else:
            return kth_element_grammar_2(n - 1, k - mid)


print(kth_element_grammar_2(6, 3))
