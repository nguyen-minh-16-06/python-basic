'''CÁC PHƯƠNG THỨC LIST TRONG PYTHON'''

#Phương thức INSERT
a = [1,2,3]
print(a)
a.insert(0,9) #Tại vị trí 0 thêm phần tử 9 vào a
# (index, phần tử)
# Nếu như index lớn hơn số phần tử có trong list thì phần tử trong
# index sẽ bị đưa về cuối.
print(a)

#Phương thức POP trong list
#Nếu như pop không có giá trị bên trong ( ) | c.pop() | => phần tử cuối cùng nằm bên trong list
b = [1,2,3]
print(b)
c = b.pop(1) #Bỏ đi phần tử thứ i trong list và trả về giá trị đó
print(b)
print(c)

#Phương thức REMOVE trong list
s = [1,2,3]
print(s)
s.remove(2) #Xoá đi phần tử có giá trị là [2]
# Nếu như ta xoá 1 phần tử không có trong list thì chương trình báo lỗi
print(s)
