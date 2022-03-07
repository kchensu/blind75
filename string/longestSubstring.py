def longestSubstring(s):
    seen = set()
    l, r = 0, 0
    res = 0
    while r < len(s):
        if s[r] not in seen:
            seen.add(s[r])
            r += 1
            res = max(res, len(seen))
        else:
            seen.remove(s[l])
            l += 1
    return res


s = "abcabcbb"
print(longestSubstring(s))
