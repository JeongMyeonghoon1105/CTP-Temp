def f(result, n, k):
  if n == 3:
    result[k].append('***')
    result[k+1].append('* *')
    result[k+2].append('***')
  else:
    for i in range(3):
      result = f(result, n // 3, k)
    result = f(result, n // 3, k + n // 3)
    for i in range(k + n // 3, k + n // 3 + n // 3):
      for j in range(n // 3):
        result[i].append(' ')
    result = f(result, n // 3, k + n // 3)
    for i in range(3):
      result = f(result, n // 3 , k + (n // 3) * 2)
  return result

n = int(input())
result = [[] for i in range(n)]
result = f(result, n, 0)

for i in result:
  print(''.join(i))
