class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        maps = {}
        length = len(nums)
        for i in nums:
            maps[i] = maps.get(i,0) + 1
        print(maps)
        for key,val in maps.items():
            if val * 2 == length:
                    return key