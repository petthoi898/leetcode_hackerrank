def romanToInt(s : str):
    num = 0
    flag = False
    for i in range(len(s)):
        if flag:
            flag = False
            continue
        if s[i] == "M":
            num += 1000
        elif s[i] == "D":
            num += 500
        elif s[i] == "C":
            if s[i+1] == "D":
                num += 400
                flag = True
            elif s[i+1] == "M":
                num += 900
                flag = True
            else:
                num += 100
        elif s[i] == "L":
            num += 50
        elif s[i] == "X":
            if i == len(s) - 1:
                num += 10
                return num
            if s[i+1] == "L":
                num += 40
                flag = True
            elif s[i+1] == "C":
                num += 90
                flag = True
            else:
                num += 10
        elif s[i] == "V":
            num += 5
        else:
            if i == len(s) - 1:
                num += 1
                return num
            if s[i+1] == "V":
                num += 4
                flag = True
            elif s[i+1] == "X":
                num += 9
                flag = True
            else:
                num += 1
    return num
print(romanToInt("MDLXX"))