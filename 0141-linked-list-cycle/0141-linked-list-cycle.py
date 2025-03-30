# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # nodes_seen = set()
        # # print(nodes_seen)
        # current = head
        # # print(current)
        # while current is not None:
        #     if current in nodes_seen:
        #         return True
        #     nodes_seen.add(current)
        #     # print(nodes_seen)
        #     current = current.next
        #     # print(current)
        # return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False