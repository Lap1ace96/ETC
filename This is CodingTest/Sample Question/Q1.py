# 모험가 길드
# Sorting을 한다는 가정 하

N= int(input())
adventure = list(map(int,input().split()))

# N=5
# adventure = [1, 1, 1, 1, 2]
# adventure.sort()

# 1 2 2 2 3
index = 0
Fear = 0
count = 0
while 1:
    Fear =adventure[index]
    index = index + Fear
    if index >= len(adventure):
        break
    count = count + 1

print(count)