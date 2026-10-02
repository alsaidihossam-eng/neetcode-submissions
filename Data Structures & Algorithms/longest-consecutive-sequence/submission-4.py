class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        max_count = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                current_count = 0
                while (current_count + num) in numSet:
                    current_count +=1
                if current_count > max_count:
                    max_count = current_count

        return (max_count)