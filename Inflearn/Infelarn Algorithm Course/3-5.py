#수들의 합
a, b= map(int,input().split())
arr = list(map(int,input().split()))
lt = 0
rt = 1
tot = arr[lt]
cnt = 0

while lt<a:
    if tot < b:
        if rt<a:
            tot = tot + arr[rt]
            rt =rt + 1
        else:
            break
    elif tot == b:
        cnt = cnt + 1
        tot = tot - arr[lt]
        lt = lt + 1
    else:
        tot = tot - arr[lt]
        lt = lt +1
print(cnt)