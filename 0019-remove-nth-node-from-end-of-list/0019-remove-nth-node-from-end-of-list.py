# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # dummy = ListNode(0)
        # # print(dummy.val)
        # dummy.next = head
        # length = 0
        # first = head
        # while first is not None:
        #     length += 1
        #     first = first.next
        # length -= n
        # first = dummy
        # while length > 0:
        #     length -= 1
        #     first = first.next
        # first.next = first.next.next
        # return dummy.next

        curr = head
        count=0
        while curr:
            count+=1
            curr = curr.next
        
        if count == n:
            return head.next

        curr = head        
        for i in range(count-n-1):
            curr = curr.next        
        curr.next = curr.next.next
        
        return head