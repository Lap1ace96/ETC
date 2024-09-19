

String = input()
Value = 0
for i in String:
    if i.isdecimal():
        Value = Value *10 + int(i)

print(Value)
cnt =0
for j in range(1,Value+1):
    if Value % j ==0:
        cnt=cnt+1

print(cnt)