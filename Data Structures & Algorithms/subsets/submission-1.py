class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #return the permitation of a set
        #there is two way to tackle this. 
        #one is top down, that means first we consider all different permutation
        #of 1, then 12, then 123

        #Bottom up would be the opposite: 123, then 12 with 3 being the free, then
        #1 with 2 3 being free

        #a bottom up approach would be the best here.
        #first we consider the whole set. Then as we remove the element from the 
        #original set, we append it to the free set. For each element in free set
        #we append it to orig set to make the answer, then move forward.

        #simulation: 12345
        #12345 -> 1234 5 -> 123 4 5 : 1234, 1235 -> 12 3 4 5: 123, 124, 125 ->
        #1 2 3 4 5: 12, 13, 14, 15

        #this work only with 1 at the top. Maybe after this, i need to advance to 2
        #simulation: Remove 1. Now we have 2345 -> 2 3 4 5, 2 3 4 5, 23 4 5 -> 23 4
        #23 5

        #we need to advance one element

        #wrong approach. Look at the correct below


        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

