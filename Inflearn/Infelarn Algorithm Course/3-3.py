#카드 역배치(정올 기출)
#index를 조심하자.(카드의 시작은 1번, list는 0번 부터)


N=[i for i in range(1,21)]
temp = 0
for i in range(0,10):
    a,b = map(int,input().split())
    for _ in range((b-a+1)//2):
        temp = N[a-1]
        N[a-1] = N[b-1]
        N[b-1] = temp
        a = a+1
        b = b-1
    temp = 0

for i in range(20):
    print(N[i],end=" ")
