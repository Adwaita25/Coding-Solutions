# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = None, head
        while fast:
            nxt = fast.next
            fast.next = slow
            slow = fast
            fast = nxt
        return slow
        
