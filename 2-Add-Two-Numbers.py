from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode(0)
        tail_node = head_node
        remain_value = 0

        while l1 != None or l2 != None or remain_value != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + remain_value
            remain_value = sum // 10
            digit = sum % 10

            new_node = ListNode(digit)
            tail_node.next = new_node
            tail_node = tail_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = head_node.next
        head_node.next = None
        return result