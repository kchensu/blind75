def containsDuplicate(a):
    seen = set()

    for num in a:
        if num not in seen:
            seen.add(num)
        else:
            True
    return False


a = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(a))
