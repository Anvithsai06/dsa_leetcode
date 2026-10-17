# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        c=0
        if head.next == None:
            return head
        while temp and temp.next:
            temp=temp.next.next
            c+=2
        c+=1
        print(c)
        mid=(c//2)+1 if c%2!=0 else c//2
        print(mid)
        temp=head
        for i in range(mid-1):
            temp=temp.next
        return temp
