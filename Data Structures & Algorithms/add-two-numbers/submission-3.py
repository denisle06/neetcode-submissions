# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #super simple solution.
        #traverse linked list and turn it into string
        #then turn it into int

        #better solution.
        #apply basic mathematics: take 1 + 4 -> create new node with this value
        #take 2 + 5 -> create new node with this value
        #In a sum of two number, the remainder can never exceed 1 -> could
        #be represented with a bool.

        dummy = ListNode(0)
        remain = False
        curr1 = l1
        curr2 = l2
        head = dummy

        while True:
            if curr1 == curr2 == None:
                if remain:
                    head.next = ListNode(1)
                return dummy.next
            elif curr1 == None:
                head.next = curr2
                while remain:
                    if curr2.val == 9:
                        if curr2.next is None:
                            curr2.val = 0
                            curr2.next = ListNode(1)
                            curr2 = curr2.next
                            remain = False
                        else:
                            curr2.val = 0
                            curr2 = curr2.next
                            remain = True
                    else:
                        curr2.val = curr2.val + 1
                        remain = False
                return dummy.next
            elif curr2 == None:
                head.next = curr1
                while remain:
                    if curr1.val == 9:
                        if curr1.next is None:
                            curr1.val = 0
                            curr1.next = ListNode(1)
                            curr1 = curr1.next
                            remain = False
                        else:
                            curr1.val = 0
                            curr1 = curr1.next
                            remain = True
                    else:
                        curr1.val = curr1.val + 1
                        remain = False
                return dummy.next
            else:
                if remain:
                    if curr1.val + curr2.val < 9:
                        new_node = ListNode(curr1.val + curr2.val + 1)
                        remain = False
                    else:
                        new_node = ListNode(curr1.val + curr2.val + 1 - 10)
                        remain = True
    
                    head.next = new_node
                    curr1 = curr1.next
                    curr2 = curr2.next
                    head = head.next
                else:
                    if curr1.val + curr2.val > 9:
                        new_node = ListNode(curr1.val + curr2.val - 10)
                        remain = True
                    else:
                        new_node = ListNode(curr1.val + curr2.val)
                    head.next = new_node
                    curr1 = curr1.next
                    curr2 = curr2.next
                    head = head.next
                    



