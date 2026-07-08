"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #In python specifically, we can hash a custom class. Thus, we
        #could create a hash map that contains key-value pairs that
        #are original: copy.

        #In the first pass, we create new instances, save them in an array, 
        #keep track of the length of array, and hash them. For the second pass
        #we just traverse the saved array, point each node to the next node
        #and point last node to null as well as replacing all random pointer
        #with its hashed value

        #i just misunderstood the assignment. The random is the random index, 
        #not the node. Super simple solution. Since we have already store
        #the node in an array format that allow indexed value, we can just
        #replace random with the index of the node

        if head == None:
            return None

        dummy = Node(0)
        dummy.next = head
        curr = head

        dummy_copy = Node(0)
        copy_curr = dummy_copy
        node_array = []
        node_dict = {}
        

        while True:
            if curr == None:
                break
            else:
                new_node = Node(curr.val)
                new_node.next = curr.next
                new_node.random = curr.random
                node_array.append(new_node)
                node_dict[curr] = new_node
                curr = curr.next
        
        for i in range(0, len(node_array)):
            if i == len(node_array) - 1:
                node_array[i].next = None
                if node_array[i].random in node_dict.keys():
                    node_array[i].random = node_dict[node_array[i].random]
                break
            else:
                node_array[i].next = node_array[i+1]
                if node_array[i].random in node_dict.keys():
                    node_array[i].random = node_dict[node_array[i].random]
                else:
                    node_array[i].random = None
                
                # copy_curr.next = node_array[i]
        
        return node_array[0]

        