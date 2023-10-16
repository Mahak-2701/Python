def show(num):
    smallest=min(num)
    largest=max(num)
    return smallest,largest


lst=[8,4,5,7,9]
smallest_num,largest_num=show(lst)
print("Smallest number in list is",smallest_num)
print("largest number in a list is",largest_num)