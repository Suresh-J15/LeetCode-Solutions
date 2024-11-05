# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, carry = ListNode(), 0
        temp = result

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            add = digit1 + digit2 + carry
            carry = add // 10
            add = add % 10
            temp.next = ListNode(add)
            temp = temp.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return result.next