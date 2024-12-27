'''CÁC PHƯƠNG THỨC LIST TRONG PYTHON'''

#Phương thức DEL trong list
a = [1,2,3,4]
del a[1] #Xoá 1 phần tử theo index trong list
print(a)

b = [1,2,3,4]
del b[1:3] # Xoá các phần tử trong 1 phạm vi chỉ định => xoá [2] và [3]
print(b)

c = [1,2,3,4]
del c[:] # Xoá toàn bộ các phần tử trong list
print(c)

