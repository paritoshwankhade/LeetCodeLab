#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#idea 1: brute force
# convert the linked list to integer, add them, and convert back to linked list
#idea 2:
# traverse the linked list, add the values, and create a new linked list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        i = 0
        while l1:
            num1 += l1.val * 10 ** i
            l1 = l1.next
            i += 1
        i = 0
        while l2:
            num2 += l2.val * 10 ** i
            l2 = l2.next
            i += 1
        num3 = num1 + num2
        if num3 == 0:
            return ListNode(0)
        head = ListNode(num3 % 10)
        temp = head
        num3 //= 10
        while num3:
            head.next = ListNode(num3 % 10)
            head = head.next
            num3 //= 10
        return temp
# @lc code=end

