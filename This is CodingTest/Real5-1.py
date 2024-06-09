#음료수 얼려먹기, DFS

N, M = map(int,input().split())
Map = list()
for i in range(N):
    Map.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False

    if Map[x][y] == 0: #여기서, 해당 좌표가 0인지에 따라 들어감
        Map[x][y] =1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #주변의 모든 0을 1로 바꾸고 시작한다.
    else:
        return False

Count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == 1:
            Count = Count +1

print(Count)

# Model_Answer

# def dfs(x,y):
#     if x<=-1 or x>=N or y<=-1 or y>=M:
#         return False
#
#     if Map[x][y] ==0:
#         Map[x][y] = 1 # 방문
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False
#
#
#
# N, M = map(int, input().split())
# Map = list()
# for i in range(N):
#     Map.append(list(map(int,input())))
#
# Cnt = 0
#
# for i in range(N):
#     for j in range(M):
#         if dfs(i,j) == True:
#             Cnt = Cnt +1
#
#
# print(Cnt)