
def convert(s: str, numRows: int):
    # string = ""

    # for i in range(numRows):
    #     if i == 0:
    #         numb = int(len(s) / numRows)
    #         for j in range(numb):
    #             string += s[j * (numRows - 1) * 2]
    #     elif i == numRows - 1:
    #         for j in range(numb):
    #             if i + 2 * j * (numRows - 1) < len(s):
    #                 string += s[i + 2 * j * (numRows - 1)]
    #     else:
    #         flag = 1
    #         for j in range(numb):
    #             string += s[numRows - i]
    # print(string)
    lstBlock = []
    numberOfString = (numRows - 1) * 2
    numberOfBlock = int(len(s) / numberOfString)
    print(numberOfBlock)
    for i in range(numberOfBlock + 1):
        if numberOfString * (i+1) < len(s):
            lstBlock.append(s[numberOfString * i : numberOfString * (i+1)])
        else:
            lstBlock.append(s[numberOfString * i :])
    string = ""
    for i in range(numRows):
        if i == 0:
            for block in lstBlock:
                if i < len(block):
                    string += block[i]
        elif i == numRows - 1:
            for block in lstBlock:
                if i < len(block):
                    string += block[i]
        else:
            for block in lstBlock:
                if i < len(block):
                    string += block[i]
                if numberOfString - i < len(block):
                    string += block[numberOfString - i]
    return string
print(convert("PAYPALISHIRING", 3))