class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            str_a = ""
            for i in digits:
                str_a += str(i)
            str_a = int(str_a)
            str_a += 1
            str_a = str(str_a)
            return list(map(int,str_a))

