N=int(input())
M= list(map(int,input().split()))
score_value = list()
a=int(0)
Noraml_Value =1

while a<N-1:
    if (M[a]==1):
        score_value.insert(a,Noraml_Value)
        for i in range(a+1,N):
            if (M[a]== M[i]):
                Noraml_Value= Noraml_Value+1
                score_value.insert(i,Noraml_Value)
                if (i==(N-1)):
                    a=i
            else:
                Noraml_Value =1
                a=i
                break
    elif (M[a]==0):
        score_value.insert(a,0)
        a=a+1
        if (a==(N-1)):
            if (M[a]==1):
                score_value.insert(a,1) # 예외처리

print(sum(score_value))