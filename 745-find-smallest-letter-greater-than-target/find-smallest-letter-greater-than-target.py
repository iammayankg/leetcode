class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # min_char = letters[0]
        for ch in letters:
            if ord(ch) > ord(target):
                return ch
        return letters[0]
        