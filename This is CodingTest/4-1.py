# My Source

# A= int(input())
# Map = [[0 for i in range(A)] for _ in range(A)]
# B =list(map(str, input().split()))
# C = len(B)
# MyRow = MyCol = 0
# for i in range(C):
#     if B[i] == 'U':
#         if MyRow == 0:
#             continue
#         else:
#             MyRow = MyRow-1
#     elif B[i] == 'R':
#         if MyCol == (A-1):
#             continue
#         else:
#             MyCol = MyCol +1
#     elif B[i] == 'L':
#         if MyCol == 0:
#             continue
#         else:
#             MyCol = MyCol -1
#     elif B[i] == 'D':
#         if MyRow == (A-1):
#             continue
#         else:
#             MyRow = MyRow +1
#     print(MyRow,MyCol)
# print(MyRow+1 ,MyCol+1)

#Model Answer With Study
Map = int(input())
Plans = list(map(str,input().split()))
# L, R, U, D
Moving_Type = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x,y = 1,1
x_pro = 0
y_pro = 0
for plan in Plans:
    for i in range(len(Moving_Type)):
        if plan == Moving_Type[i]:
            x_pro = x+ dx[i]
            y_pro = y+ dy[i]
        if x_pro < 1 or y_pro < 1 or x_pro > Map or y_pro> Map: # 공간을 벗어나게 되면
            continue # 반복 구문 자체를 벗어나서 다시 시작한다.

        x = x_pro
        y = y_pro
    print(x, y)
print(x,y)


#What I Learned → Commit

