A = int(input())
B = list(map(int,input().split()))
C = list()
D=B.copy()
ans =0
for j in range(A):
    while 1:
        tmp = B[j] % 10 # 5
        ans= ans+tmp # 5
        B[j] = B[j]//10 # 12
        if B[j] == 0:
            C.append(ans)
            tmp= 0
            ans= 0
            break
max_value = max(C)
x_index = [index for index, value in enumerate(C) if value == max_value]
print(D[min(x_index)])