def cantor(l):
  if l == 1:
    return '-'
  return cantor(l // 3) + ' ' * (l // 3) + cantor(l // 3)

while True:
  try:
    l = 3 ** int(input())
    print(cantor(l))
  except EOFError:
    break
