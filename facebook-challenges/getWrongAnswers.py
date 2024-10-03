# fb

def getWrongAnswers(N: int, C: str) -> str:
  wrongAnswers = []
  
  for i in range(len(C)):
    if C[i] == "A":
      wrongAnswers.append("B")
    else:
      wrongAnswers.append("A")

  return ''.join(wrongAnswers)