class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)

        return len(nums) != len(numsSet)