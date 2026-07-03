# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #store value of the linked list into a dict. If exist in a dict, then return
        #true. if there are a null pointer -> false

        #wrong. Two pointer fast and slow approach
        

        if head == None:
            return False
        if head.next == None:
            return False

        fast = head
        slow = head

        while True:
            if head.next == None or head.next.next == None:
                return False
                
            else:
                if fast == None or fast.next == None or fast.next.next == None:
                    return False
                else:
                    fast = fast.next.next
                
                if slow == None or slow.next == None:
                    return False
                else:
                    slow = slow.next

                if fast.next == slow.next:
                    return True
            
            