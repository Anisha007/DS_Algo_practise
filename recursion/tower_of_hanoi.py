def TOH(n, source, destination, helper):
    global count_step
    if n == 1:
        print("Move disc {} from {} to {}".format(n, source, destination))
        count_step += 1
    else:
        TOH(n - 1, source, helper, destination)
        print("Move disc {} from {} to {}".format(n, source, destination))
        count_step += 1
        TOH(n - 1, helper, destination, source)


count_step = 0
TOH(4, "A", "C", "B")
print(count_step)
