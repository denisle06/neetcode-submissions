class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        num = sorted(nums)
        for i in num:
            oppo = target - i
            if oppo in num:
                hash[i] = oppo
                if oppo != i:
                    if nums.index(i) > nums.index(oppo):
                        return [nums.index(oppo), nums.index(i)]
                    else:
                        return [nums.index(i), nums.index(oppo)]
                elif len(nums) == 2:
                    return [0, 1]
                else:
                    first_loc = nums.index(i)
                    new_list = nums[nums.index(i)+1:]
                    remove_parts = len(nums[:nums.index(i) +1])
                    for a in new_list:
                        if a == i:
                            second_loc = new_list.index(a) + remove_parts
                    return [first_loc, second_loc]

            