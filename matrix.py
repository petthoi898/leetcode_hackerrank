#!/bin/python3

import math
import os
import random
import re
import sys


def refix(lst: list, x, a):
    for a in range(x, a):
        lst[a] = " "

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
ret = ""
symbols = ("!","@","#","$","%","&"," ")
for i in range(0, m):
    for a in matrix:
        ret += str(a[i])
lstRet = list(ret)
for a in range(len(lstRet)):
    if lstRet[a] in symbols:
        flag = -1
        for x in range(a, len(lstRet)):
            if lstRet[x] not in symbols:
                flag = x
                break
        if flag != -1:      
            for i in range(a, flag):
                lstRet[i] = " "
flagIdx = -1
a = "".join(lstRet)
for x in range(len(a) - 1,0,-1):
    if a[x] in symbols:
        continue
    else:
        flagIdx = x
        break
if flagIdx != -1:
    b = a[:flagIdx]
    c = a[flagIdx:]
idx = b.find("  ")
while idx != -1:
    b = b.replace("  "," ")
    idx = b.find("  ")
print(b + c)
