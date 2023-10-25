num=int(input("Eneter a number:"))
factorial=1
if num<0:
    print("factorial doesn't exists for negative number:")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in Range(1,num+1):
        factorial*=i
    print("the factoral of ",num ,"is",factorial)

