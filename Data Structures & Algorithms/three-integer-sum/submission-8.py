class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)
        answer_list = []

        for i in range(len(sorted_num)):
            new_target = -(sorted_num[i])
            result = None

            j = i + 1
            k = len(sorted_num) - 1

            while j != k and j < len(sorted_num) - 1: 
                if sorted_num[j] + sorted_num[k] > new_target:
                    k -= 1
                elif sorted_num[j] + sorted_num[k] < new_target:
                    j += 1
                elif sorted_num[j] + sorted_num[k] == new_target:
                    triplet = [sorted_num[i], sorted_num[j], sorted_num[k]]
                    j += 1
                    if triplet not in answer_list: #and sorted_num[k] != sorted_num[i] != sorted_num[j] != sorted_num[k]:
                        answer_list.append(triplet)
                        
        return answer_list

            
                