# 19. Write a program to find a size of a tuple in python. 
import sys 
# sample Tuples 
Tuple1 = ("A", 1, "B", 2, "C", 3) 
Tuple2 = ("abc", "Raju", "def", "Nikhil", "ghi", "Deepanshu") 
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")) 
# print the sizes of sample Tuples 
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes") 
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes") 
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes") 
