class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  #for i in range defines the number of empty arrays that goes in the freq array
        for n in nums:
            count[n] = 1 + count.get(n, 0) #get retrieve the value from the count dict
        for n, c in count.items():  
            freq[c].append(n) #n happened c number of time
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

            
        