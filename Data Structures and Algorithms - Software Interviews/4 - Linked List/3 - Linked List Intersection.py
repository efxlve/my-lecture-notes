#Intersection of two Linked Lists
#Write a program to find the node at which the intersection of two singly linked lists begins.
#
#For example, the following two linked lists:
#
#A:          a1 → a2
#                   ↘
#                     c1 → c2 → c3
#                   ↗
#B:     b1 → b2 → b3
#begin to intersect at node c1.
#
#Notes:
#
#If the two linked lists have no intersection at all, return null.
#The linked lists must retain their original structure after the function returns.
#You may assume there are no cycles anywhere in the entire linked structure.
#Your code should preferably run in O(n) time and use only O(1) memory.
#
#https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        aPointer = headA
        bPointer = headB

        while aPointer != bPointer:
            if aPointer:
                aPointer = aPointer.next
            else:
                aPointer = headB

            if bPointer:
                bPointer = bPointer.next
            else:
                bPointer = headA

        return aPointer
    
    solution = getIntersectionNode(None, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    print(solution) # [1, 2, 3, 5]