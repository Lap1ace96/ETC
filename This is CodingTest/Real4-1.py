N = 8
Map = [[0 for i in range(N)] for _ in range(N)] # 리스트 컴프리헨션 굳이 필요하지 않다.

Locate = input()
Moving = [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(-1,-2),(1,2),(-1,2)]

Row = ord(Locate[0]) - ord('a') + 1
Col = int(Locate[1])

print(Row, Col) # 1,1로써 시작함.
cnt = 0
for a,b in Moving:
    Row_Pro = Row + a
    Col_Pro = Col + b
    if Row_Pro < 1 or Col_Pro < 1 or Row_Pro > 8 or Col_Pro > 8 :
        Row_Pro = Row
        Col_Pro = Col
        continue
    Row_Pro = Row
    Col_Pro = Col
    cnt = cnt +1
print(cnt)