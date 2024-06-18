N, M = map(int,input().split())
Ball = sorted(list(map(int,input().split())))


count = 0
for i in range(len(Ball)-1):
    for j in range(i+1,len(Ball)):
        if Ball[i] == Ball[j]:
            continue
        else:
            count =count + 1

print(count)