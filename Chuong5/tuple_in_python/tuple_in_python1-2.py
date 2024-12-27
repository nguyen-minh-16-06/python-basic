#Constuctor/Comprehension tuple
tup = (i for i in range(10) if i % 2 == 0)
# Giống với list constructor a = tuple('MINH') => print(a) = ('M','I','N','H')
a = tuple(tup)
# Khác biệt là tuple sẽ tạo ra 1 tuple chứ không tạo ra list
# Nếu ta muốn sử dụng comprehension ở bên trong tuple thì ta phải thông qua 1 bước trung gian
print(a)
# Các toán tử của tuple GIỐNG với các toán tử của chuỗi
# Nhưng toán tử của list GẦN GIỐNG với toán tử của chuỗi
