class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in valid_pairs.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                open_paren = stack.pop()
                if valid_pairs[open_paren] != char:
                    return False
        if stack:
            return False
        return True
                    
                
        