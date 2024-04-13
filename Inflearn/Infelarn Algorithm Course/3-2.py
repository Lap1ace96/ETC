# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
# 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
# 만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이
# 됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120
# 의 약수의 개수를 출력하면 됩니다.
# 추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

# 숫자와 문자를 구분하는 섹션
# 앞자리를 0으로 만들지 않는 예외 처리 섹션
# 해당 자리에 맞는 숫자를 만들때 list 형식인데 이걸 어떻게 숫자로 만드나?

A = input()
B = list()
for i in A:
    if i.isdecimal():
        B.append(i)
ZLI = 0 # Zero Value Index
C=0
B_Converit = list(map(int,B))

for j in B_Converit:
    if j>=1:
        ZLI = C #0이 아닌 최초 인덱스를 구한다.
        break
    C=C+1
D=list()

while 1:
    if C<=len(B_Converit)-1:
        D.append(B_Converit[C])
        C=C+1
    else:
        break
E=len(D)-1
sum=0
for j in D:
    sum= sum + j*pow(10,E)
    E=E-1
    if E==-1:
        break

cnt = 0
for l in range(1,sum+1):
    if sum%l == 0:
        cnt=cnt+1
print(sum)
print(cnt)