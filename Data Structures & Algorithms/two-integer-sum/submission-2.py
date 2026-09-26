class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            x = target - num
            if x in nums:
                for j, num in enumerate(nums):
                    if x == num and j > i:
                        ans.append(i)
                        ans.append(j)
                        return ans