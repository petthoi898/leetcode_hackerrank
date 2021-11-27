def check(a: int):
    return abs(a) >= 2**31
def reverse(x : int):
    res = ""
    pos = False
    if x < 0:
        pos = True
        x = abs(x)
    while x > 0:
        a = x % 10
        res += str(a)
        x = int(x / 10)
    ret = int(res)
    if check(ret):
        return 0
    else:
        if pos:
            return -ret
        else: return ret
print(reverse(123))