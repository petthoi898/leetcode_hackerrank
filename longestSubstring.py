def find(subStr : str, s : str):
    pass
def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 0:
            return 0
        lstCheck = []
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                a = set(s[i:j])
                ret = ""
                for x in a:
                    ret += str(x)
                if s.find(ret) != i:
                    lstCheck.append(len(ret))
                    
        return max(lstCheck)

lengthOfLongestSubstring(" ")