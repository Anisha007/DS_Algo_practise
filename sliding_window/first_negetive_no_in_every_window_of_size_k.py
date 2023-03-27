def solve(arr, k):
    lookup = []
    i, j = 0, 0
    ans = []
    while j < len(arr):
        print(j)
        if arr[j] < 0:
            lookup.append(arr[j])
        if j - i < k:
            j += 1
        elif j - i == k:
            # calculate ans
            if len(lookup) == 0:
                ans.append(0)
                print("ans = ", ans)
            if arr[i] < 0 and arr[i] == lookup[0]:
                ans.append(arr[i])
                print("ans = ", ans)
                lookup.pop(0)
                i += 1
                j += 1
            elif arr[i] >= 0:
                i += 1
        if arr[j] >= 0:
            j += 1
    return ans


print(solve([12, -1, -7, 3, 5, -1, 4, 5, 6], 2))
