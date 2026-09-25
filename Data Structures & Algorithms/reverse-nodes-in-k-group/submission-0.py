# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        k_tail = None
        curr = head

        while curr:
            count = 0
            curr = head

            while curr and count < k:
                curr = curr.next
                count += 1

            if count == k:
                rev_head = self.reverse(head, k)
            
                if not new_head:
                    new_head = rev_head

                if k_tail:
                    k_tail.next = rev_head
                
                k_tail = head
                head = curr

        if k_tail:
            k_tail.next = head

        return new_head if new_head else head
                



    def reverse(self, head, k):
        prev = None
        curr = head

        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        return prev
        