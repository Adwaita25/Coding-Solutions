# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        #finding middle
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while(right):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
