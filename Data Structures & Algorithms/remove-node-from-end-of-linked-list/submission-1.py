# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #super simple solution.
        #keep track of 3 pointer at the same time
        #3 pointer keep advancing up until one of them until the last pointer is null
        #keep track of the middle pointer and consider it as the index
        #when the middle pointer = index -> remove it and attach the first pointer
        #to the last.

        #wrong. Remove count from end to top
        #super simple patch: Just traverse the list once and keep track of the 
        #length. Then subtract it with n to find the needed index

        
        dummy = ListNode(0)
        dummy.next = head

        count = 0
        curr_pointer = dummy
        while True:
            if curr_pointer == None: 
                break
            else:
                curr_pointer = curr_pointer.next
                count += 1

        target = count - n

        if head.next == None:
            return None

        i = 1
        curr = dummy.next
        prev = dummy
        nex = dummy.next.next

        while True:
            if i == target:
                prev.next = nex
                curr.next = None
                return dummy.next
            else:
                prev = curr
                curr = nex
                nex = nex.next
                i += 1
                
        

        

