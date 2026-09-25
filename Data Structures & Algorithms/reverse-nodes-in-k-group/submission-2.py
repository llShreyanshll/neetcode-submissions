# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gp = dummy

        while True:
            kth = self.getkth(gp, k)
            if not kth:
                break

            gn = kth.next
            prev, curr = kth.next, gp.next

            while curr != gn:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = gp.next
            gp.next = kth
            gp = temp

        return dummy.next



    def getkth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
