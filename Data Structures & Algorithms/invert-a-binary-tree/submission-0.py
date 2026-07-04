# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #save original root. 
        #If self.left = none or self.right = none. continue
        #swap left and right. root = root.left. root = root.right
        #what is the terminate condition of this while loop? 
        #In a recursive approach, ideally the root should descend to far left at
        #then climb up 1 level automatically and go right. 
        
        #1 -> 2 -> 4 could be done by declare root = root.left. How to climb up
        #from 4 to 2? Recursively, because 4.left is null, it attempt to visit
        #4.right. Because 4.right is also null, it go out of the executing branch
        #then 2.right is selected. The same thing happen. Now we need to know 
        #that 2.right is already traversed. How could we accomplish this? 
        #By saving the node into an array, this could be solved easily. Then
        #the solution would be 2n time and n space. Which is good

        #the terminate condition would be when root is original root, and 2 of
        #the branch are already visited

        #if root is none, abort. Else, visit root.right and root.left and swap

        original_root = root
        if root == None:
            return
        else:
            
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            
            self.invertTree(root.left)
            self.invertTree(root.right)

        return original_root
    

            
            
