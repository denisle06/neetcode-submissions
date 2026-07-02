# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            #strategy for linked list: have a dummy head and call dummy.next
        dummy = ListNode(0)
        dummy.next = head
        i = 1

        #for the linked list of length n, the mapping is as follow:
        #0 -> n-1. 1 -> n-2. 2->n-3. 3-> n-4.
        #we could maintain two list of nodes, and alternating through it.
        #But that would not be o(n) time 

        #instead we can maintain two variable for it.
        #The first variable should be the current node. The second variable should
        #be adjacent

        #i = 0
        #0, 1, 2, 3, 4. -> 0, 2, 1, 3, 4 -> 0, 3, 2, 1, 4 -> 0, 4, 3, 2, 1 -> 
        #0, 4, 1, 3, 2 

        

        #end condition: We store 3 node. If the last node = none => stop the loop

        #The shuffle above. i = 0, i++.Always store 3 node: i, i+ 1, i + 2. 
        #let i+1 point to i+2.next. Let i+2 point to i + 1. Let i point to i+2
        
        #Logic failing

        # attach node i + 1 to node 0 and node 1. Skip 1 node step then keep inserting
        # 0, 1, 2, 3, 4, 5 -> 3 node saved: 0, 1, 2. i = 0
        # 0, 2, 1, 3, 4, 5 -> 3 node saved: 1, 3, 4. i = 2
        # 0, 2, 1, 4, 3, 5 -> 3 node saved: 3, 5, None -> stop. i = 4

        #wrong logic
        #A simpler aprpoach: Keep track of i and i+1. traverse to end of chain, attach
        #last element and increment i
        #0, 1, 2, 3, 4, 5. i = 0. Saved 0, 1, insert 5 into 0, 1
        #0, 5, 1, 2, 3, 4. i = 2. Saved 1, 2, insert 4 into 1, 2
        #0, 5, 1, 4, 2, 3. i = 4. Saved 2, 3. Check and see that 3.next is None.

        #0, 1, 2, 3, 4, 5, 6. i = 0. Saved 0, 1, insert 6 into 0, 1
        #0, 6, 1, 2, 3, 4, 5. i = 2. Saved 1, 2, insert 5 into 1, 2 
        #0, 6, 1, 5, 2, 3, 4. i = 4. Saved 2, 3. Insert 4 into 2, 3
        #0, 6, 1, 5, 2, 4, 2. i = 6. Save 2, None. Check and see that one is None

        #0, 1, 2, 3, 4, 5, 6, 7. i = 0. Saved 0, 1, insert 7 into 0, 1
        #0, 7, 1, 2, 3, 4, 5, 6. i = 2. Saved 1, 2, insert 6 into 1, 2 
        #0, 7, 1, 6, 2, 3, 4, 5. i = 4. Saved 2, 3. Insert 5 into 2, 3
        #0, 7, 1, 6, 2, 5, 3, 4. i = 6. Saved 3, 4. Check and see that 4.next is None


        if dummy.next == None:
            return
        elif dummy.next.next == None:
            return
        elif dummy.next.next.next == None:
            return
        else:
            first_node = None
            second_node = None
            near_end_node = None
            current_head = dummy.next

            while True:      
                first_node = current_head
                second_node = first_node.next
                

                if second_node == None or second_node.next == None:
                    break
                
                near_end_node = second_node

                while True:
                    if near_end_node.next.next == None:
                        break
                    near_end_node = near_end_node.next

                
                #swap logic:
                first_node.next = near_end_node.next
                near_end_node.next.next = second_node
                near_end_node.next = None
                
                
                current_head = second_node
            
            