# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        f=s=head
        while f and f.next:
            s=s.next
            f=f.next.next
        sec=s.next
        s.next=None
        prev=None
        curr=sec
        while curr:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        sec=prev
        first=head
        while sec:
            temp1=first.next
            temp2=sec.next
            first.next=sec
            sec.next=temp1
            first=temp1
            sec=temp2
