class Solution:
    def mirrorDistance(self, n: int) -> int:
        # n_s = 
        # rev = int(n_s)
        return abs(n - int(str(n)[::-1]))