class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        
        for string in strs:
            newString = str(sorted(string))
            if newString not in output:
                output[newString] = []
            output[newString].append(string)

        print(output)

        return list(output.values())
    
# learnings
# take a simpler solution tbh

# different approaches
# 1. doing exactly what i did but with a default dict 
# 2. (better, no sorting) using a list of the alphabet characters as the key for the dict (stored as a tuple)