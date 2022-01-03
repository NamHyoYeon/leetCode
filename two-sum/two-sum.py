from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        flag = 0
        # 그리디 알고리즘
        for i in range(len(nums)):
            if flag == 1:
                break
            diff = target - nums[i]
            for j in range(len(nums)):
                if (diff == nums[j]) and (i!=j):
                    result.append(i)
                    result.append(j)
                    flag = 1
                    break
        
        return result
        