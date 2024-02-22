from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_digit = 0
        head_of_list = None
        current_node = None
        while l1 is not None or l2 is not None:
            value = carry_digit
            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next
            node_value = ListNode(value % 10)
            carry_digit = value // 10

            if head_of_list == None:
                head_of_list = node_value
                current_node = node_value

            else:
                current_node.next = node_value
                current_node = current_node.next

        if carry_digit is not 0:
            current_node.next = ListNode(carry_digit)
    
        return head_of_list
            

        