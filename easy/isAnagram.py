from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram = defaultdict(int)
        anagram2 = defaultdict(int)

        for i in range(len(s)):
            anagram[s[i]] += 1
            anagram2[t[i]] += 1
        
        # print(anagram, anagram2)

        return anagram == anagram2
