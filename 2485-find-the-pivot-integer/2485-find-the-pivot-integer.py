class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        x = -1
        for i in range(1, n):
            sum_n = (n * (n + 1)) / 2
            sum_i = (i * (i+1))/2
            sum_i_to_n = sum_n - (i * (i-1))/2
            if sum_i == sum_i_to_n:
                return i
            
        return x