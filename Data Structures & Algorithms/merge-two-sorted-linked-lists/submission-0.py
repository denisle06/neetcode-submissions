class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #logic: keep track of the two list node. If one of the two is none, always
        #append the other. If both is None, return the List

        dummy = ListNode(0)
        curr = dummy

        while True:
            if list1 == None:
                if list2 == None:
                    return dummy.next
                else:
                    curr.next = list2
                    return dummy.next
            elif list2 == None:
                if list1 == None:
                    return dummy.next
                else:
                    curr.next = list1
                    return dummy.next
            else:    
                if list1.val >= list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next