from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedNums = Counter(nums)

        sortedCounted = sorted(countedNums.items(), key=lambda item: item[1])
        # print(countedNums)
        # print(sortedCounted)

        output = []

        for i in range(k):
            output.append(sortedCounted[-1][0])
            sortedCounted.pop()

        return output

# there has to have been a smarter way

# 1. sorting (lowkey what i did)
# 2. using a heap (thought of this but chose laziness) -- saves time but not space
# 3. iterating through the counter to create a dictionary for each key with a particular count
# ^^ bucketing solution -- bucket each number in its count