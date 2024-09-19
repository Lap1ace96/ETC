# 두 리스트 합치기
# sort를 써보자
# 그리고, sort 아닌 method로도 구현을 해보자.

a= int(input())
arr1 = list(map(int,input().split()))
b= int(input())
arr2 = list(map(int,input().split()))

arr3 = []
p1=p2=0
while p1<a and p2<b:
    if arr1[p1] <= arr2[p2]:
        arr3.append(arr1[p1])
        p1=p1+1
    else:
        arr3.append(arr2[p2])
        p2=p2+1
# list 작은거 우선 정리 해놓고, 나머지 얘들 붙이기 그대로 붙이기
if p1<a:
    arr3=arr3+arr1[p1:]
if p2<b:
    arr3=arr3+arr2[p2:]
print(arr3)


# arr3 = arr1+arr2
# arr3.sort()
# print(arr3)