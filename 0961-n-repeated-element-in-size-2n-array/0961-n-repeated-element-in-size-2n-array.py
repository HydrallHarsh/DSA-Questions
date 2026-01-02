class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            maps[i] = maps.get(i,0) + 1
        for key,val in maps.items():
            if val * 2 == len(nums):
                    return key