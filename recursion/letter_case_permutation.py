def permutation_with_letter_case(ip, op):
    if len(ip) == 0:
        print(op)
        return
    if ip[0].isalpha():
        op_toggle_case = op + (ip[0].lower() if ip[0].isupper() else ip[0].upper())
        op_without_toggle = op + ip[0]
        ip_next = ip[1:]
        permutation_with_letter_case(ip_next, op_toggle_case)
        permutation_with_letter_case(ip_next, op_without_toggle)

    else:
        op = op + ip[0]
        ip_next = ip[1:]
        permutation_with_letter_case(ip_next, op)


permutation_with_letter_case("A1b34c", "")
