def check(num):
    for i in num:
        if(i%2==0):
            print(i)
    for i in num:
        if(i%2!=0):
            print(i)

number=[2,5,8,6]
check(number)