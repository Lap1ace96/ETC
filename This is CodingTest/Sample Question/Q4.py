#그리디, 만들 수 없는 거스름돈

N=int(input())
arr = list(map(int,input().split()))

target = 1
for i in arr:
    if target < i:
        break
    target+=i

print(target)