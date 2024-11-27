# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)

        left_head, right_head = left, right

        while head:
            if head.val < x:
                left_head.next = head
                left_head = head
            else:
                right_head.next = head
                right_head = head
            head = head.next
        right_head.next = None
        left_head.next = right.next

        return left.next
