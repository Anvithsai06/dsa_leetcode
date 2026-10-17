# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        prev=None
        temp=head
        c=0
        while temp:
            temp=temp.next
            c+=1
        mid=c//2
        temp=head
        for i in range(mid):
            prev=temp
            temp=temp.next
        if prev:
            prev.next=temp.next
            return head
