#include<stdlib.h>
#include <iostream>
#include <vector>
using namespace std;
//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};
void printList(ListNode* l1) {
    while (l1 != NULL) {
        cout << l1->val << endl;
        l1 = l1->next;
    }
}
int count(ListNode* l1) {
    int co = 0;
    while (l1->next != NULL) {
        co++;
        l1 = l1->next;
    }
    return co;
}
void refix(ListNode* l1, int num) {
    ListNode* ptr = l1;
    while (ptr->next != NULL) {
        ptr = ptr->next;
    }
    while (num > 0) {
        ListNode* newnode = new ListNode();
        ptr->next = newnode;
        ptr = ptr->next;
        num--;
    }
}
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (count(l1) > count(l2)) {
            refix(l2, count(l1) - count(l2));
        }
        else if (count(l1) < count(l2)) {
            refix(l1, count(l2) - count(l1));
        }
        vector<bool> lstCheck;
        int val = l1->val + l2->val;
        ListNode* ret;
        if (val >= 10) {
            ret = new ListNode(val - 10);
            lstCheck.push_back(true);
        }
        else {
            ret = new ListNode(val);
            lstCheck.push_back(false);
        }
        l1 = l1->next;
        l2 = l2->next;
        ListNode* ptr = ret;
        while (l1 != NULL) {
            int num = 0;
            if (lstCheck.at(lstCheck.size() - 1)) {
                num = l1->val + l2->val + 1;
                lstCheck.push_back(true);
            }
            else {
                num = l1->val + l2->val;
                lstCheck.push_back(false);
            }
            ListNode* newnode;
            if (num >= 10) {
                newnode = new ListNode(num - 10);
                lstCheck.push_back(true);
            }
            else {
                newnode = new ListNode(num);
                lstCheck.push_back(false);
            }
            while (ptr->next != NULL) {
                ptr = ptr->next;
            }
            ptr->next = newnode;
            l1 = l1->next;
            l2 = l2->next;
        }
        if (lstCheck.at(lstCheck.size() - 1)) {
            ptr = ptr->next;
            ptr->next = new ListNode(1);
        }
        return ret;
    }
};
int lengthOfLongestSubstring(string s) {

}
int main() {
    /*Solution* a = new Solution();
    ListNode* x1 = new ListNode(4);
    ListNode* x2 = new ListNode(4, x1);
    ListNode* x3 = new ListNode(3, x2);
    ListNode* x1_ = new ListNode(9);
    ListNode* x2_ = new ListNode(6, x1_);
    ListNode* x3_ = new ListNode(4, x2_);
    ListNode* x4_ = new ListNode(7, x3_);
    ListNode* aa = a->addTwoNumbers(x3, x4_);
    printList(aa);*/
    return 0;
}