#K번째 수
# N, K = map(int,input().split())
# Card = list(map(int,input().split()))
#
# res=set()
# for i in range(0,N):
#     for j in range(i+1,N):
#         for m in range(j+1,N):
#             res.add(Card[i]+Card[j]+Card[m])
# result =list(res)
# result.sort(reverse=True)
# print(result[K-1])

#Pre, 최솟값 구하기
# arr = [5,3,7,9,2,5,2,6]
# arrMin = float('inf')
#
# for i in range(len(arr)):
#     if arr[i] < arrMin:
#         arrMin = arr[i]
#
# print(arrMin)

# Representaive Value
# N=int(input())
# Score = list(map(int,input().split()))
# Avg = round(sum(Score)/len(Score))
# Min = 100000
# for idx, value in enumerate(Score):
#     tmp = abs(value-Avg)
#
#     if tmp <Min:
#         Min = tmp
#         idx_list = idx+1
#         value_list = value
#     elif tmp==Min:
#         if value>value_list:
#             idx_list = idx+1
#             value_list = value
#
# print(Avg, idx_list)

# Representaive Value, My Rule
# N= input()
# Score = list(map(int, input().split()))
# Avg = round(sum(Score)/len(Score))
# diff_Avg = list()
#
# for i in range(len(Score)):
#     diff_Avg.append(abs(Avg-Score[i]))
#
# diff_index = [i for i, x in enumerate(diff_Avg) if x == min(diff_Avg)]
# tmp=0
# for j in diff_index:
#     if Score[j] > tmp:
#         tmp = Score[j]
#         lAST_index = j
#
# print(Avg,lAST_index+1)
#
# ------------------정 N면체
# A, B = map(int,input().split())
# Sum_Result_List = list()
# if A>=B:
#     for i in range(A):
#         for j in range(B):
#             Sum_Result_List.append((i+1) + (j+1))
# else:
#     for i in range(B):
#         for j in range(A):
#             Sum_Result_List.append((i+1)+(j+1))
#
# Set_Sum_Result_List = set(Sum_Result_List)
# Change_Set_Sum_Result_List = list(Set_Sum_Result_List)
# # print(Sum_Result_List)
# # print(Change_Set_Sum_Result_List)
#
# Count = list()
# Fre = 0
# for i in range(len(Change_Set_Sum_Result_List)):
#     for j in range(len(Sum_Result_List)):
#         if Change_Set_Sum_Result_List[i] == Sum_Result_List[j]:
#             Fre = Fre+ 1
#     Count.append(Fre)
#     Fre = 0
# # print(Count)
# Enum_List = [i for i, x in enumerate(Count) if x == max(Count)]
# # print(Enum_List)
# for i in Enum_List:
#     print(Change_Set_Sum_Result_List[i],end=' ')


# Digit_Sum_Result P6
# A = int(input())
# B = list(map(int,input().split()))
# C = list()
# D=B.copy()
# ans =0
# for j in range(A):
#     while 1:
#         tmp = B[j] % 10
#         ans= ans+tmp
#         B[j] = B[j]//10
#         if B[j] == 0:
#             C.append(ans)
#             tmp= 0
#             ans= 0
#             break
# max_value = max(C)
# x_index = [index for index, value in enumerate(C) if value == max_value]
# print(D[min(x_index)])

# Prime Number
# def GetPrimeNoOpt(n):
#     res = []
#     for i in range(2, n+1):
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             res.append(i)
#     return res
#
# print(GetPrimeNoOpt(20))

# N, M = map(int, input().split())
# Prime_List = list()
# a=1
# for i in range(N,M+1):
#     for j in range(N,i): #i-1 까지 나누자.
#         if i%j==0: # 한 번이라도 나눠지면
#             a=0
#             break # 너는 소수가 아니다.
#     if a==1:
#         Prime_List.append(i)
#     a=1
# print(Prime_List)
#
# N=2
# M=20
# Prime_List=list()
#
# for i in range(N,M):
#     Is_Prime = True
#     for j in range(2,i):
#         if i==j: # 2일떄의 예외처리
#             Prime_List.append(i)
#         if i%j ==0 : # 혹시 나눠 진다면, 소수가 아니다.
#             Is_Prime = False
#             break
#     if Is_Prime == True:
#         Prime_List.append(i)
#
# print(Prime_List)

#에라토스테의 체

# n=int(input())
# ch = [0]*(n+1)
# cnt = 0
# for i in range(2,n+1):
#     if ch[i]==0:
#         cnt = cnt+1
#         for j in range(i,n+1,i):
#             ch[j]=1
# print(cnt)

# 8. Reverse_Prime
# A= int(input())
# B= list(map(int,input().split()))
#
# def reverse(x):
#     res = 0
#     while x>0:
#         t= x%10
#         res = res*10 +t
#         x= x//10
#     return res
#
# def isPrime(x):
#     cnt = 0
#     if x==1:
#         return False
#     for i in range(2,x):
#         if (x%i==0): # 무언가 나누어 떨어지면?
#             cnt = cnt+1
#         if (cnt>2):
#             return False
#         else:
#             return True
#
#
# for i in B:
#     tmp = reverse(i)
#     if isPrime(tmp):
#         print(tmp, end= ' ')

#9 Dice_Game
# N=int(input())
# Maximum = list()
# for i in range(N):
#     a, b, c = map(int, input().split())
#     if (a==b)&(b==c):
#         Maximum.append(10000+a*1000)
#     elif (a==b): # a와 b가 같을경우
#         Maximum.append(1000+a*100)
#     elif (a==c): # a와 c가 같을경우
#         Maximum.append(1000+a*100)
#     elif (b==c): # b와 c가 같을경우
#         Maximum.append(1000 + b * 100)
#     else:
#         Maximum.append(max(a,b,c)*100)
# print(max(Maximum))

# #10, Score

#N=int(input())
# #M=list(map(int,input().split()))
# N=int(input())
# M= list(map(int,input().split()))
# score_value = list()
# a=int(0)
# Noraml_Value =1
#
# while a<N-1:
#     if (M[a]==1):
#         score_value.insert(a,Noraml_Value)
#         for i in range(a+1,N):
#             if (M[a]== M[i]):
#                 Noraml_Value= Noraml_Value+1
#                 score_value.insert(i,Noraml_Value)
#                 if (i==(N-1)):
#                     a=i
#             else:
#                 Noraml_Value =1
#                 a=i
#                 break
#     elif (M[a]==0):
#         score_value.insert(a,0)
#         a=a+1
#         if (a==(N-1)):
#             if (M[a]==1):
#                 score_value.insert(a,1) # 예외처리
#
# print(sum(score_value))

# 회문 문자열 검사
# N=int(input())
# for i in range(N):
#     s=input()
#     s=s.upper()
#     size=len(s)
#     for j in range(size//2): # 최신화
#         if s[j] != s[-1-j]:
#             print('#%d'%(i+1) + " NO")
#             break
#     else:
#         print('#%d YES'% (i+1))
#
#          # 인덱스 접근을 -로
# ADDIT
# N=int(input())
# for i in range(N):
#     s=input()
#     s=s.upper()
#     if s==s[::-1]: # S의 리버스와 같냐?
#         print("#%d YES"%(i+1))
#     else:
#         print("#%d NO" % (i + 1))

# 숫자만 추출
# s=input()
# res = 0
# for x in s: # 하나씩 하나씩
#     if x.isdecimal():
#         res = res * 10 + int(x) #10씩 곱하자
# print(res)
# cnt=0
# for i in range(1,res+1):
#     if res%i==0:
#         cnt=cnt+1
# print(cnt)
# 카드 역배치
# Card = [i for i in range(1,21)]
# tmp=0
# for _ in range(10):
#     a, b= map(int, input().split()) # index 항상 +1
#     for _ in range((b-a+1)//2):
#         tmp = Card[a-1]
#         Card[a-1] = Card[b-1]
#         Card[b-1] = tmp
#         a=a+1
#         b=b-1
#     tmp = 0
#
# for i in range(20):
#     print(Card[i], end=' ')


