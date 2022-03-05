def reach(a):
    furthest_reach, last_index = 0, len(a)-1
    i = 0
    while i <= furthest_reach and furthest_reach < last_index:
        furthest_reach = max(furthest_reach, i + a[i])
        i += 1
    return furthest_reach >= last_index


a = [2, 4, 1, 1, 0, 2, 3]
b = [3, 2, 0, 0, 2, 0, 1]

print(reach(b))
