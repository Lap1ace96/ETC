

import time
start = time.time()
# 맵 생성----------------------
N, M =map(int,input().split())
# 최초 위치-------------------------------------------
Locate_X, Locate_Y, Direction = map(int,input().split())
Complete_Map = list((Locate_X,Locate_Y)) # 가본 맵
count = 1 # 첫 카운트
# ------------------------------------------------------------------
Map = [[0 for i in range(N)]for _ in range(M)] # List Comprehension
for i in range(N):
    Mapping = list(map(int,input().split()))
    for j in range(M):
        Map[i][j] = Mapping[j] # Mappaing To Map
# -------------------------------------------------------------------
Turn_Count = 0

#Rotate 후의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def Turn_Left(Func_Direction):
    Func_Direction = Func_Direction +1
    if Func_Direction == 4:
        Func_Direction = 0
    return Func_Direction

while 1:
    Direction = Turn_Left(Direction)
    Temp_Locate_X = Locate_X+ dx[Direction]
    Temp_Locate_Y = Locate_Y+ dy[Direction]
    if Map[Temp_Locate_X][Temp_Locate_Y] == 0 and (Temp_Locate_X,Temp_Locate_Y) not in Complete_Map: # 육지면서, 안 가봤으면
        Locate_X, Locate_Y = Temp_Locate_X, Temp_Locate_Y
        Complete_Map.append((Locate_X,Locate_Y))
        count = count +1
        print(Locate_X,Locate_Y)
        Turn_Count = 0
    else :
        Turn_Count = Turn_Count +1

    if Turn_Count ==4:
        Temp_Locate_X = Locate_X
        Temp_Locate_Y = Locate_Y +1
        if Map[Temp_Locate_X][Temp_Locate_Y] ==0:
            Locate_X, Locate_Y = Temp_Locate_X, Temp_Locate_Y
        else:
            break
        Turn_Count = 0

print(count)
# Model Answer
#
# n, m = Map(int,input().split())
#
# d = [[0* m for _ in range(n)]]
# x,y,direction = map(int,input().split())
# d[x][y] = 1
#
# array = []
# for i in range(n):
#     array.append(list(map(int,input().split())))
#
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
#
# def turn_left():
#     global direction
#     direction = direction -1
#     if direction == -1:
#         direction = 3
#
# count = 1
# turn_time = 0
# while 1:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#
#     # 회전 이후에 정면에 가본게 없으면 이동을 한다.
#     if d[nx][ny] ==0 and array[nx][ny] ==0:
#         d[nx][ny] =1
#         x=nx
#         y=ny
#         count = count +1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time = turn_time +1
#     if turn_time ==4:
#         nx = x-dx[direction]
#         ny = y-dy[direction]
#         if array[nx][ny] ==0:
#             x= nx
#             y= ny
#         else:
#             break
#         turn_time = 0
#
# print(count)