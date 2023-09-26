'''10. Design a menu driven program that shows 4 options : and there work is written
1. Prime Numbers: take starting and stopping point , then show result
2. Even Numbers: take starting and stopping point , then show result
3 Odd Numbers: take starting and stopping point , then show result
4 Exit : print a message = thankyou , goodbye'''
def even(start,end):
    print("\t\t :: Even Numbers ::\n")
    for n in range(start, end + 1):
        if n % 2 == 0:
            print(n)

def prime(start,end):
    print("\t\t :: prime Numbers ::\n")
    for i in range(start,end+1):
        prime='true'
    for j in range(2,i):
        if i%j==0:
            prime='false'
            break
    if prime=='true':
        print(i)

def odd( start,end):
    print("\t\t :: Odd Numbers ::\n")
    for n in range(start, end + 1):
        if n % 2 != 0:
            print(n)


while True:
    print("1.even ")
    print("2.prime")
    print("3.odd")
    print("4.Exit. ")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        num1 = int(input("Enter Starting Number :"))
        num2 = int(input("Enter Ending Number :"))
        even(num1,num2)
    elif choice == 2:
        num1 = int(input("Enter Starting Number :"))
        num2 = int(input("Enter Ending Number :"))
        prime(num1, num2)
    elif choice == 3:
        num1 = int(input("Enter Starting Number :"))
        num2 = int(input("Enter Ending Number :"))
        odd(num1, num2)
    elif choice == 4:
        print("Thankyou for using calculator . ")
        break
    else:
        print("Invalid choice!!!")
        continue
