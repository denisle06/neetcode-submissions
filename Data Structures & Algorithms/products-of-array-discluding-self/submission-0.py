class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_hash = {}
        product_list = []
        for i in range(len(nums)):
            suffix_product = 1
            prefix_product = 1
            product_hash[i] = []
            for n in nums[0:i]:
                prefix_product *= n
            for n in nums[i+1:]:
                suffix_product *= n
            product_hash[i].append(prefix_product)
            product_hash[i].append(suffix_product)
        for i in range(len(nums)):
            product = product_hash[i][0] * product_hash[i][1]
            product_list.append(product)
        return product_list

                
