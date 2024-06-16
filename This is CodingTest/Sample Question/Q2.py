# str을 먼저 각 자리 별로 int 형으로 만들어야 함.
# 그걸 계산하되 , 0과 1은 + 해야함.
# 앞이 0이면, result를 어떻게 해야 하는지 고민해야함. --> 초기값 0 에 대해 IF를 사용하였음.
N=str('24054')
N_Change = list()
result =0
for i in range(len(N)):
    N_Change.append(int(N[i]))

for i in N_Change:
    if i == 0:
        continue
    elif i ==1 :
        if result ==0:
            result = i
        result = result + i
    else:
        if result == 0:
            result = i
            continue
        result = result * i

print(result)