def check(lst , k):
    lstRet = ""
    for a in lst:
        if a not in lstRet:
            lstRet += str(a)
    return lstRet
def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    for i in range(0,length, k):
        lst = string[i:i + k]
        print(check(lst, k))
    
if __name__ == '__main__':
    #string, k = input(), int(input())
    merge_the_tools("AABCAAADA", 3)