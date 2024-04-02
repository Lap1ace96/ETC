# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

Card = [i for i in range(1,21)]
tmp=0
for _ in range(10):
    a, b= map(int, input().split()) # index 항상 +1
    for _ in range((b-a+1)//2):
        tmp = Card[a-1]
        Card[a-1] = Card[b-1]
        Card[b-1] = tmp
        a=a+1
        b=b-1
    tmp = 0

for i in range(20):
    print(Card[i], end=' ')
