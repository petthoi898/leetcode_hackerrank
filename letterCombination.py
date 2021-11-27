
def letterCombinations(digits: str):
        dictNumber = { 
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        for i in range(len(digits)):
            if res:
                respone1 = []
                for a in res:
                    respone1 += [a + x for x in dictNumber[digits[i]]]
                res = respone1
            else:
                res = dictNumber[digits[i]]
        return res
print(letterCombinations(digits="23"))
