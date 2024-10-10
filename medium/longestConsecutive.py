class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maximums = []

        nums = sorted(list(set(nums)))
        output = 1
        prev = nums[0]
    
        print(nums, prev, output)
    
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                output += 1
            else:
                maximums.append(output)
                output = 1
            print(nums[i], prev, output)

            prev = nums[i]

        if nums[-1] == prev + 1:
            output += 1
        maximums.append(output)

        return max(maximums)
    
# complexity: O(nlogn), O(n)
# you could do far better than sorting

# 1. hash set -- making nums a set, seeing if num - 1 is in set, maintaining currentLength and longest vars
# 2. hash map -- log each number in dict and update its value based on how many consecutive it has