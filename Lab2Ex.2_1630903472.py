# Exercise2

array1 = [7, 5, 10, 14, 3, 9, 7]
array2 = [9, 10, 3, 4, 2, 5, 7, 1]
print(len(array1),len(array2))
print(array1.index(7),array2.index(7))
array1.append(1)
array2.append(14)
array3 = array1
arraynew = array3.extend(array2)
array3 = sorted(array3)
array3.remove(7)
array4 = array3
array4 = array4[::-1]
print(array3,array4)