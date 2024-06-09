# 최소, bfs

from collections import deque

N,M = map(int,input().split())
Map = list()
for i in range(N):
    Map.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
     #상 하 좌 우
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if Map[nx][ny] ==0:
                continue
            if Map[nx][ny] ==1:
                Map[nx][ny] = Map[x][y] +1
                queue.append((nx,ny))
            # for i in range(N):
            #     print(Map[i][:], end="\n")
            # print('-----------',end="\n")
            if (nx, ny) == (N-1,M-1):
                return Map[N-1][M-1]

    # return Map[N-1][M-1]


print(bfs(0,0))
print()

