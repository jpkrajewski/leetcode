# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  # Dummy node to simplify result list creation
        current = dummy  # Pointer to build the resulting linked list

        while l1 or l2 or carry:
            current_sum = carry
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            
            # Calculate new digit and carry
            carry, digit = divmod(current_sum, 10)

            # Add the digit to the resulting list
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next  # Return the head of the actual result list
