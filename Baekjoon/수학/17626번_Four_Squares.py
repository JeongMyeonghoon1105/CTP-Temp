import math

def square(n):
  if math.floor(n ** 0.5) ** 2 == n:
    return 1
  elif n == 0:
    return 0
  print(n)
  n -= math.floor(n ** 0.5) ** 2
  return 1 + square(n)

n = int(input())
print(square(n))
