"""
Brute Force
Time Complextiy: O(n^2)
Space Complextiy: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()'in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

"""
Solution 2: Stack
Time Complexity: O(n)
Space Complexity: O(n)

class Solution
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        
        for c in s:
            if c in closeToOpen:
                if stack[::-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
"""