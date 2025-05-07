"""
Time Complexity: O(nlogn + mlogm)
Space Complexity: O(1) or O(n + m)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

"""
Solution 2: Hash Map
Time Complexity: O(n + m)
Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in len(s):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
"""