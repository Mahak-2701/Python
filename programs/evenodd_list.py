def check(num):
    even=[]
    odd=[]
    for i in num:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)

number=[2,5,8,6]
check(number)