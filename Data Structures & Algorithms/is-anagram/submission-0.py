class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in letter_counts:
                letter_counts[char] = letter_counts[char] + 1
            else:
                letter_counts[char] = 1
        for char in t:
            if char in letter_counts:
                letter_counts[char] = letter_counts[char] - 1
                if letter_counts[char] < 0:
                    return False
            else:
                return False
        for char in letter_counts:
            if letter_counts[char] != 0:
                return False
        return True

        