# Remove Nth Node from End of List
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def removeNthFromEnd(self, head, n):
        leftPointer = head
        rightPointer = head

        while n > 0 and rightPointer:  # there is n gap between two pointers
            rightPointer = rightPointer.next
            n -= 1

        # stop when rightPointer.next is None.
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        if leftPointer == head and not rightPointer:  # if we omit this, it won't work on the edge case of one node
            return head.next

        # skip the leftPointer.next so it would be out of LinkedList
        leftPointer.next = leftPointer.next.next
        return head
    
    solution = removeNthFromEnd(None, [1, 2, 3, 4, 5], 2)
    print(solution) # [1, 2, 3, 5]

