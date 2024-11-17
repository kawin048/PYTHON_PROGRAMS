num = int(input("ENTER YOUR NUMBER:"))
temp = num
sum=0
while(temp > 0):

    mod=temp%10
    mul=mod*mod*mod
    sum=sum+mul
    temp=temp//10

if sum ==  num:
    print("GIVEN NUMBER IS ARMSTRONG NUMBER:")
else:
    print("GIVEN NUM NOT A ARMSTRONG NUMBER")        


