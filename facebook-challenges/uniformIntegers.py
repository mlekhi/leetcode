def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  digits = len(str(B))
  count = 0
  
  while digits:
    for i in range(1, 10):
      print(i)
      if A <= int(str(i) * digits) <= B:
        count += 1
    
    digits -= 1
  
  return count 