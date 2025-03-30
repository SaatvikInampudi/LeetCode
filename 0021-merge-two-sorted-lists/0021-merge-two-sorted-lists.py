# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 != None:
        #     print(list1)
        #     print(list1.next)
        #     print(list1.val)


        # maintain an unchanging reference to node ahead of the return node.

        # if l1 is None and l2 is not None:
        #     return l2
        # elif l2 is None and l1 is not None:
        #     return l1
        # elif l1 is None and l2 is None:
        #     return None
        # else:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next