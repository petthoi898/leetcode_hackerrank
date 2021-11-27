# Definition for singly-linked list.
import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def count(lNum):
    ret = 0
    while lNum > 0:
        lNum = int(lNum/10)
        ret += 1
    return ret
def refix(l1: ListNode, number):
        while number > 0:
            while l1.next is not None:
                l1 = l1.next
            l1.next = ListNode(0)
            number -= 1
def pri(l1: ListNode):
    while l1 is not None:
        print(l1.val)
        l1 = l1.next
def check(num):
    return num > 10
def addNumber(L3: ListNode, num, flag):
    if not flag:
        while L3 is not None:
            L3 = L3.next
        L3.val =  num
    else:
        while L3 is not None:
            L3 = L3.next
        L3.val = num + 1
class SLL:
    def __init__(self, head = None, tail= None):
        self.head = head
        self.tail = tail
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = List
        a.insert()
        l1Str = ""
        l2Str = ""
        l1_ = l1
        l2_ = l2
        while l1 is not None:
            l1Str += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2Str += str(l2.val)
            l2 = l2.next
        l1Num = count(int(l1Str))
        l2Num = count(int(l2Str))
        if l1Num - l2Num > 0:
            refix(l2_, l1Num - l2Num)
        else:
            refix(l1_, l2Num - l1Num)
        num = l1_.val + l2_.val
        lstCheck = []
        if num >= 10:
            L3 = ListNode(num - 10)
            lstCheck.append(True)
        else:
            L3 = ListNode(num)
            lstCheck.append(False)
        l1_ = l1_.next
        l2_ = l2_.next
        while l1_ is not None:
            if lstCheck.pop():
                num = l1_.val + l2_.val + 1
            else:
                num = l1_.val + l2_.val
            while L3.next is not None:
                L3 = L3.next
            if num >= 10:
                L3.next = ListNode(num - 10)
                lstCheck.append(True)
            else:
                L3.next = ListNode(num)
                lstCheck.append(False)
            l1_ = l1_.next
            l2_ = l2_.next
        if lstCheck.pop():
            L3.next = ListNode(1)
        return L3


a = Solution()

pri(a.addTwoNumbers(ListNode(2,ListNode(4, ListNode(9))), ListNode(5, ListNode(6, ListNode(4, ListNode(9))))))
pri(a.addTwoNumbers(ListNode(2,ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))