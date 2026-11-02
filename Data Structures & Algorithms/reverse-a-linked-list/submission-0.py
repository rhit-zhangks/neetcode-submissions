# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        curr_node = head.next
        head.next = None
        prev_node = head

        while curr_node is not None:
            temp_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_next
        
        return prev_node
