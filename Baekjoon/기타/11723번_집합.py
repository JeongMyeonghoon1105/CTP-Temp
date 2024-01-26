s = []

def add(x):
  if x not in s:
    s.append(x)

def remove(x):
  for i in range(len(s)):
    if s[i] == x:
      s.pop(i)
      return

def check(x):
  if x in s:
    return 1
  return 0

def toggle(x):
  if check(x):
    remove(x)
    return
  add(x)

def all():
  s = [i for i in range(1, 21)]
  return s

def empty():
  s = []
  return s

m = int(input())
for i in range(m):
  inp = input()

  if inp == 'all':
    s = all()
  elif inp == 'empty':
    s = empty()
  else:
    func, x = inp.split()
    x = int(x)

    if func == 'add':
      add(x)
    elif func == 'remove':
      remove(x)
    elif func == 'check':
      print(check(x))
    elif func == 'toggle':
      toggle(x)

