class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_list = {}  #hash for value
        for n in strs:  
            sort = sorted(n) #sort the string
            sort = "".join(sort) #make the string again
            if sort not in sub_list:  #value assigned to sorted string
                sub_list[f"{sort}"] = []
                sub_list[f"{sort}"].append(n)
            else:
                sub_list[f"{sort}"].append(n)
        value = sub_list.values()
        return value
        
        
