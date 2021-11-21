from operator import itemgetter

def isPalidrome(s: str):
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True
def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    lstCheck = []
    i = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalidrome(s[i:j]):
                lstCheck.append((s[i:j], len(s[i:j])))
    return max(lstCheck,key=lambda item:item[1])[0]


print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
print("bb"[0:2])