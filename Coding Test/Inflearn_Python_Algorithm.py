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





















