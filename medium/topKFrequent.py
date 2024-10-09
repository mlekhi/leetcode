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