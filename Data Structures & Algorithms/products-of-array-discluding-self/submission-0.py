class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        result = 1
        zero_result = 1
        
        for num in nums:
            result *= num
            
        for i, num in enumerate(nums):
            if num != 0:
                output.append(result // num)
            else:
                nums.pop(i)
                for num in nums:
                    zero_result *= num
                output.append(zero_result)
                nums.insert(i,0)

        return output