def generate_parenthesis(open, close, op, res):
    if open == 0 and close == 0:
        res.append(op)
        return
    if open != 0:
        op1 = op + "("
        generate_parenthesis(open - 1, close, op1, res)

    if open < close:
        generate_parenthesis(open, close - 1, op + ")", res)


def generate_parenthesis_backtracking(open, close, op):
    if open == 0 and close == 0:
        return [op]
    op_list, op_list2 = [], []
    if open != 0:
        op1 = op + "("
        op_list = generate_parenthesis_backtracking(open - 1, close, op1)

    if open < close:
        op_list2 = generate_parenthesis_backtracking(open, close - 1, op + ")")

    op_list.extend(op_list2)
    return op_list


def generate_parenthesis_backtracking_2(open, close):
    if open == 0 and close == 0:
        return [""]
    op_list, op_list2 = [], []
    if open != 0:
        op_list = generate_parenthesis_backtracking_2(open - 1, close)
        for i in range(len(op_list)):
            op_list[i] = '(' + op_list[i]

    if open < close:
        op_list2 = generate_parenthesis_backtracking_2(open, close - 1)
        for i in range(len(op_list2)):
            op_list2[i] = ')' + op_list2[i]

    op_list.extend(op_list2)
    return op_list


res = []
print(generate_parenthesis_backtracking_2(3, 3))
# print(res)
