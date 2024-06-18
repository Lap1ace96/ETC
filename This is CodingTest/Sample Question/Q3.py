#list out of index가 항상 뜬다.
#이걸 어떻게 해결을 해야 하지?
# 옆을 비교 하는 걸 다르게 생각해야 하나?
N=input()
count_list = [0,0]

# 초반 초기값에 대한 값을 넣어야 함.
if N[0]=='0':
    count_list[0] = 1
else:
    count_list[1] = 1

for i in range(0,len(N)-1):
    if N[i] != N[i+1]: #다를 때
        if N[i+1] == '0':
            count_list[0] += 1
        else:
            count_list[1] += 1

print(min(count_list))