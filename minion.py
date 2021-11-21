def minion_game(string):
    # your code goes here
    
    vowels = ["U","E",'O',"A",'I']
    listVowels = [(".", -1)]
    listConsonants = [(".", -1)]
    for a in range(len(string)):
        #print(string[a])
        if string[a] not in vowels:
            listVowels.append((string[a], a))
        else:
            listConsonants.append((string[a], a))
#    return max(calculate(string, listConsonants), calculate(string, listVowels))
    listVowels.remove((".", -1))
    listConsonants.remove((".", -1))
    st = calculate(string, listVowels)
    kv = calculate(string, listConsonants)
    #print(str(st) + " " + str(kv))
    if st > kv :
        return "Stuart "+ str(st)
    elif kv < st:
        return "Kevin "+ str(kv)
    else:
        print("Draw")
def calculate(string, listOfIndex):
    point = 0
    for a in listOfIndex:
        for i in range(len(string)):
            if a[-1] <= i:
                point = point + 1 
    return point      


if __name__ == '__main__':
    f =open('input.txt', 'r')
    content = f.readlines()
    print(minion_game("BANANANAAAS".upper()))