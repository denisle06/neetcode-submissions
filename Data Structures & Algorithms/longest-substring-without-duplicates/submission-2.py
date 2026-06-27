class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        hashmap = {}
        maxlen = 1
        
        if s == "" or s == None:
            return 0

        for r in range(len(s)):
            while s[r] in hashmap.keys():
                hashmap.pop(s[l])
                l += 1
            
            hashmap[s[r]] = "1"
            maxlen = max(maxlen, r - l + 1) 
            
        
        return maxlen
                
            
        
        