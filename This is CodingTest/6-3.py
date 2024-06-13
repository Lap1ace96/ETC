#삽입 정렬
#못 풀었음.
#
# array = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[i] < array[j]: # 5<7
#             temp = array[j] #7
#             array[j] = array[i]
#             array[i] = temp
#             print('얍')
#         else:
#             break
#
# print(array)

# array = [7,5,9,0,3,1,6,2,4,8]
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i,0,-1): # range 중간 0을 하는 이유는(-1 아님), 삽입정렬의 특성상 j-1을 Indexing 하기 떄문
        if array[j-1] > array[j]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1]=temp
        else:
            break
print(array)