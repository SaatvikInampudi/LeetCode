# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        curr_node = head
        while curr_node != None:
            Next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = Next
        return prev
