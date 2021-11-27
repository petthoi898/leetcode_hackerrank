def maxArea(height: list[int]) -> int:
    maxWater = 0
    i = 0
    j = len(height) - 1
    while i < j:
        maxWater = max(maxWater, (j - i) * min(height[i], height[j]))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxWater
print(maxArea([1,4,5,6,8,4]))