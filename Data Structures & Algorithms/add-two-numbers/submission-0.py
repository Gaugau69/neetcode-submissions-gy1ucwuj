# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry != 0:
            somme = 0

            if l1:
                somme += l1.val 
                l1 = l1.next
            if l2:
                somme += l2.val
                l2 = l2.next
            if carry:
                somme += carry

            carry = somme // 10
            somme = somme % 10
            cur.next = ListNode(somme)
            cur = cur.next

        return dummy.next
