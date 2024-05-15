#격자판 최대 합
# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합


N= int(input())
arr = list()
sum_arr =list()
row=col=0

for i in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N): #row와 col 구하기
    for j in range(N):
        # rol
        col = col + arr[i][j]
        # row
        row = row + arr[j][i]

    if col >= row:
        sum_arr.append(col)
        row = 0
        col = 0
    else:
        sum_arr.append(row)
        row = 0
        col = 0

sum1=sum2=0
for i in range(N): # 대각선 구하기
    sum1=sum1+arr[i][i]
    sum2=sum2+arr[i][N-i-1]

sum_arr.append(sum1)
sum_arr.append(sum2)

print(max(sum_arr))
