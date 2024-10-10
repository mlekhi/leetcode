class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # no data structures! O(1) space

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if target - numbers[i] == numbers[j]:
                    return [i + 1, j + 1]
                

# so, this is kind of the same thing i did for two sum pt.1
# the time complexity is O(n^2), which is bad

# better approach: using left and right pointers TO LEVERAGE THAT IT'S ALREADY SORTED