def delete_duplicate(a):
    if len(a) == 0:
        return 0

    pointer = 1

    for i in range(1, len(a)):
        if a[pointer - 1] != a[i]:
            a[pointer] = a[i]
            pointer += 1
    return a


def delete_duplicate_min(a, m):
    if not a:
        return 0
    pointer = 1
    count = 0

    for i in range(1, len(a)):
        if a[pointer - 1] == a[i]:
            count += 1
        else:
            count = 1
        if a[pointer - 1] != a[i] or min(2, m):
            a[pointer] = a[i]
            pointer += 1
    return a


a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
# print(delete_duplicate(a))
print(delete_duplicate_min(a, 3))
