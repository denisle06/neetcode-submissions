class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n in hash:
                return True
            hash[n] = []
        return False

            
         