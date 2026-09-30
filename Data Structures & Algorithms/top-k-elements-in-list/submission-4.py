class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}
        ans = []

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        for key, value in count_dict.items():
            ans.append([value, key])


        ans.sort(reverse=True)

        for i in range(len(ans)):
            if len(ans) > k:
                ans.pop()
            else:
                return [ans[j][1] for j in range(k)]