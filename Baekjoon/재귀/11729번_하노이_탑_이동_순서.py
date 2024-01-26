def hanoi(n, fr, by, to):
  if n == 0:
    return
  hanoi(n-1, fr, to, by)
  print(str(fr) + ' ' + str(to))
  hanoi(n-1, by, fr, to)

N = int(input())
print(2 ** N-1)
hanoi(N, 1, 2, 3)
