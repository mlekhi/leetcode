# fb

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  hitProbability = 0
  
  for i in range(R):
    for j in range(C):
      hitProbability += G[i][j]
      
  return hitProbability / (R*C)