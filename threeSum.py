def check(res, next):
    return next in res
def threeSum(nums):
    lengthNums = len(nums)
    if lengthNums < 3:
        return []
    neg, pos, zero = [], [], []
    for number in nums:
        if number > 0:
            neg.append(number)
        elif number < 0:
            pos.append(number)
        else:
            zero.append(number)
    # neg = list(set(neg))
    N, P = set(neg), set(pos)
    # pos = list(set(pos))
    res = []
    if len(zero) >= 3:
        res.append([0,0,0])
    # zero = list(set(zero))
    if len(zero) > 0:
        for number in neg:
            if -number in pos:
                next = [-number, 0, number]
                if not check(res, next):
                    res.append(next)
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            tar = pos[i] + pos[j]
            if -tar in neg:
                next = [pos[i], pos[j], -tar]
                if not check(res, next):
                    res.append(next)
    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            tar = neg[i] + neg[j]
            if -tar in pos:
                next = [-tar, neg[i], neg[j]]
                if not check(res, next):
                    res.append(next)
    return res
print(threeSum([-1,0,1,2,-1,-4]))