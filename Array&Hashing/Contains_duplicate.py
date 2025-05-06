from typing import List

"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False

"""
Solution 2: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
            return False

Solution 3: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
"""