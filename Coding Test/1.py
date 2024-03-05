a= int(input("몇단을 만들고 싶으세요?"))
for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end="")
    for k in range(0,i*2-1):
        print("*",end="")
    print("")