count=0
sum=0
print("It will provide you the sum of the numbers you've entered and the numeber of times you entered an input")
while True :
    a=input("Type here something : ")
    count=count+1
    if a=="done" :
        break
    try :
        a=int(a)
        sum=sum+a
        continue
    except :
        print(a,"is a string.")
        continue
print("The sum is :",sum)
print("The number of time loop executed is :",count,"👍")
