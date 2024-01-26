# 인접이중리스트 구성
# 새로 입력된 좌표가 기존의 좌표 중 어느 것과도 인접하지 않으면
#   새로운 행에 저장
# 새로 입력된 좌표가 기존의 좌표 중 하나와 인접하면
#   인접하는 좌표 옆에 붙이기
# 인접하려면 --> (x 같음 and y +- 1) or (x +- 1 and y 같음)
# 지렁이 개수 세기

adjLst = []

t = int(input())
for i in range(t):
  m, n, k = map(int, input().split())
  for j in range(k):
    x, y = map(int, input().split())
    

