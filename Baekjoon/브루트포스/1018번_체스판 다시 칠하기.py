import sys

n, m = map(int, input().split())
board = []

for i in range(n):
  board.append(sys.stdin.readline()[:-1])

sample = [
  [
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
  ],
  [
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'],
  ]
]

row = 0
col = 0
while row <= n - 8:
  while col <= m - 8:
    pass
    col += 1
  row += 1

# count = [0, 0]
# char1 = board[0][0]
# if char1 == 'B':
#   char2 = 'W'
# else:
#   char2 = 'B'

# state = True

# for i in range(n):
#   for j in range(m):
#     if state and char1 != board[i][j]:
#       count[0] += 1
#     elif not state and char2 != board[i][j]:
#       count[0] += 1
#     state = not state
#   state = not state

# state = True

# for i in range(n):
#   for j in range(m):
#     if state and char2 != board[i][j]:
#       count[1] += 1
#     elif not state and char1 != board[i][j]:
#       count[1] += 1
#     state = not state
#   state = not state

# print(min([count[0], m*n-count[0], count[1], m*n-count[1]]))
