def check(res : int):
    return abs(res) >= 2**31
def myAtoi(s: str) -> int:

    number = []
    for i in range(10):
        number.append(str(i))
    symbols = [' ', '+', '-']
    if s[0] not in symbols and s[0] not in number: return 0
    res = ""
    for i in s:
        if i in number:
            res += i
        if i == ' ':
            continue
        if i == '-':
            res += "-"
    a = int(res)
    while check(a):
        res = res[1:]
        a =int(res)    
    return int(res)
print(myAtoi("42"))