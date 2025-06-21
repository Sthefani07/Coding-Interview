from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked_nums_dict = {} #Dictionary to save key:value 
        
        for index, num in enumerate(nums):
                calculated_key = target - num
                if calculated_key in checked_nums_dict:
                        return[checked_nums_dict[calculated_key], index]
                checked_nums_dict[num] = index
           

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(s.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(s.twoSum([3, 3], 6))           # Output: [0, 1]