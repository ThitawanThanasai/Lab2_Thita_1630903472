# Exercise 5

array1 = [[1, "Rubber", 0, "Out of stock"], [2, "Ruler", 5, "In stock"], [3, "Pencil", 1, "In stock"]]
print(len(array1))
array1.append([4,"Pen",10,"In stock"])
array1.append([5,"Colour pencil",5,"In stock"])
array1.append([6,"A4 Paper",0,"Out of stock"])
print(array1)
for i in array1:
    if i[3] == "In stock":
        print(i)
for i in array1:
    if i[3] == "Out of stock":
        print(i)
array1[1][2] = array1[1][2] - 1
array1[2][2] = array1[2][2] - 1
array1[3][2] = array1[3][2] - 2
array1[4][2] = array1[4][2] - 1
for i in array1:
    if i[2] == 0:
        i[3] = "Out of stock"
print(array1)