class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequence_starter = []
        for n in nums: 
            if n - 1 not in nums:
                sequence_starter.append(n)
        for i in sequence_starter:
            leng = 0
            while i + leng in nums:
                leng += 1
            if leng > longest:
                longest = leng
        return longest

                


