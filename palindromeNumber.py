def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        stringX = str(x)
        for i in range(int(len(stringX)/2)):
            if stringX[i] != stringX[-i-1]:
                return False
        return True