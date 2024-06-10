# 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

# 만약 0 부터 9 까지만 있다고 생각을 하게 된다면?
for i in range(len(array)):
    for j in range(i+1,len(array)):
        temp = array[i]
        if i == array[j]:
            array[i] = i
            array[j] = temp

    print(array)
