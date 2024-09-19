

a= int(input())
result = []
for i in range(0, a):
    arr = str(input()).upper()
    arr_size = len(arr)
    for j in range(0,arr_size//2):
        if arr[j] != arr[arr_size-1-j]:
            print("#%d NO"%(i+1))
            break
    else:
        print("#%d YES"%(i+1))


# a=int(input())
#
# arr = list()
# arr_size = list()
# result = list()
# for i in range(0,a):
#     arr.append(input())
#     arr_size.append(len(arr[i]))
#     for j in range(0,arr_size[i]//2):
#         if arr[j] != (arr_size[i]-j):
#             result.append("No")
#     result.append("YES")
#
# print(result)
#
#


# 회문 문자열의 갯수가 짝수면 필요 없으나, 홀수라면 2/n만 해도 된다.
# 그게 회문 문자열의 특성임.