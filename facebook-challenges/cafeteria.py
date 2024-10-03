# fb

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  print(S)
  additionalDiners = 0
  
  distance = S[0] - 1
  additionalDiners += distance // (K+1)
  print(distance, additionalDiners)
  
  for i in range(len(S)-1):
    distance = S[i+1] - S[i] - K-1
    print(S[i+1], S[i], distance)
    
    additionalDiners += distance//(1 + K)
    print(additionalDiners)
  
  distance = N - S[-1]
  additionalDiners += distance // (K + 1)
  print(distance, additionalDiners)

  return additionalDiners