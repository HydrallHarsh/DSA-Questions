class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_char = letters[0]
        min_val = 50
        for i in letters:
            t = int(ord(i) - ord(target))
            if (t > 0 and t < min_val):
                min_val = min(t, min_val)
                min_char = i
        return min_char