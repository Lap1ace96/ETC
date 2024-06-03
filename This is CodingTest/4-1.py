# L : 왼쪽

A= int(input())
Map = [[0 for i in range(A)] for _ in range(A)]
B =list(map(str, input().split()))
C = len(B)
MyRow = MyCol = 0
for i in range(C):
    if B[i] == 'U':
        if MyRow == 0:
            continue
        else:
            MyRow = MyRow-1
    elif B[i] == 'R':
        if MyCol == (A-1):
            continue
        else:
            MyCol = MyCol +1
    elif B[i] == 'L':
        if MyCol == 0:
            continue
        else:
            MyCol = MyCol -1
    elif B[i] == 'D':
        if MyRow == (A-1):
            continue
        else:
            MyRow = MyRow +1
    print(MyRow,MyCol)
print(MyRow+1 ,MyCol+1)