#write a program that list that contains numbers from 99 to 50 and converts into ascending order.
lis=[87,89,56,98,58,93,75,85]
lis.sort()
print(lis)


#write a program that has one list of 5 fruits names and you should create 5 different copies of it and each list should have 1 different item and should not match.
fruit=['apple','banana','cherry','papaya','orange']
print(fruit)
fruits_copy=fruit.copy()
fruits_copy.append('pomegrante')
print(fruits_copy)


#write a program that should have 5 different key value pairs in a dictionary and you can perform insertion and deletion operations and you should print the dictionary after every operation yo do or not.
#but the final result should be an {} empty dictionary.
student = {
    "name": "ALI",
    "course": "BCA",
    "id":123,
    "fees":23456
}
item=student.items()
print(item)
student['grade']=[8.9]
for key, value in student.items():
    print(key, ":", value)
print("*******")
remove=student.pop('fees')
for key, value in student.items():
    print(key, ":", value)

student.clear()
print(item)