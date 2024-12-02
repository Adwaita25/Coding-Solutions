# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        to_delete = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.val in to_delete:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next
