# fb

from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0
  prev = float('inf')
  
  for i in range(len(R) - 1, -1, -1):
    if R[i] >= prev:
      R[i] = prev - 1
      count += 1
    prev = R[i]
      
  if 0 not in R:
    return count
  else:
    return -1
