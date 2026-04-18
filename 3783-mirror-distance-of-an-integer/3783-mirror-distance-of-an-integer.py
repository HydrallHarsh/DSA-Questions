class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_s = str(n)
        n_s = n_s[::-1]
        rev = int(n_s)
        return abs(n - rev)