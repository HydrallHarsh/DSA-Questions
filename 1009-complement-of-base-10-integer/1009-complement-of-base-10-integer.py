class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_num = bin(n)[2:]
        comp = []
        for i in bin_num:
            if i == '0' :
                comp.append('1')
            else:
                comp.append('0')
        return int("".join(comp),2)