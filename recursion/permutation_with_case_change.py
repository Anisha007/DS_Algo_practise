def permutation_case_change(ip, op):
    if len(ip)==0:
        print(op)
        return
    op_case_change = op+ip[0].upper()
    op_no_change = op+ip[0]
    ip = ip[1:]
    permutation_case_change(ip, op_no_change)
    permutation_case_change(ip, op_case_change)


permutation_case_change("abc", "")