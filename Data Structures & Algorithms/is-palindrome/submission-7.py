class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(clean) - 1
        
        while l < r:
            if not clean[l] == clean[r]:
                return False
            l += 1
            r -= 1
        return True