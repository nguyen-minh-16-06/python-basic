# Constuctor/Comprehension tuple
tup = (i for i in range(10) if i % 2 == 0)
# Giống với list constructor a = tuple('MINH') => print(a) = ('M','I','N','H')
# Nếu ta muốn sử dụng comprehension ở bên trong tuple thì ta phải thông qua 1 bước trung gian
a = tuple(tup)  # Khác biệt là tuple sẽ tạo ra 1 tuple chứ không tạo ra list
print(a)
