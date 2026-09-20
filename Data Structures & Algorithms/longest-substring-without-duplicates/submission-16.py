class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_letters = {}
        max_len = 0
        curr_len = 0
        l,r = 0,0

        while r < len(s):
            #print(l,r)
            letter = s[r]
            if not letter in seen_letters or seen_letters[letter] < l:
                seen_letters[letter] = r
                #print("added", letter)
                r += 1
                curr_len = r - l
            else:
                #print("seen", letter, "already")
                curr_len = r - l
                if curr_len > max_len:
                    max_len = curr_len
                l = seen_letters[letter] + 1
                seen_letters[letter] = r
                curr_len = r - l
                r += 1
            #print(seen_letters)
        if curr_len > max_len:
            return curr_len
        return max_len