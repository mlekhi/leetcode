from typing import List
import itertools
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  S.sort(reverse=True)
  problemSet = {1: 0, 2:0}
  
  problemSet[2] += S[0] // 2
  problemSet[1] += S[0] % 2
  
  print(problemSet)
  
  for i in range(1, len(S)):
    if problemSet[1] == 0 and S[i]%2 != 0:
      problemSet[2] -= 1
      problemSet[1] += 2
    
  return sum(problemSet.values())