class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        copy = set()
        for a in nums:
            if a in copy:
                return True
            copy.add(a)
        return False