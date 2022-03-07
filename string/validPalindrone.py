def validPalindrone(s):
    s = s.lower()
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


s = "A man, a plan, a canal: Panama"
p = "race a car"


def test1():
    assert validPalindrone(s) == True


def test2():
    assert validPalindrone(p) == False
