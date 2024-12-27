'''CÁC PHƯƠNG THỨC LIST TRONG PYTHON'''

#Phương thức CLEAR trong list
a = [1,2,3,4,5,6]
b = a.clear() #Xoá hết các phần tử trong list => không cần tham số nào truyền vào
# Không có giá trị nào trả về, nó chỉ làm sạch list
# a là 1 list rỗng []
print(a)

#Phương thức APPEND trong list
c = [1,2,3]
print(c)
c.append([4,5]) #Được dùng để thêm 1 đối tượng vào một danh sách
# Đối tượng này có thể thuộc bất kì kiểu dữ liệu, chuỗi, số nguyên, boolean
# Thậm chí là 1 danh sách khác.
print(c)

#Phương thức EXTEND trong list
s = [1,2,3]
print(s)
s.extend([4,5]) #Hoạt động trên các đối tương có thẻ lặp và nối thêm mọi mục
# trong lần lặp vào danh sách.
# Sử dụng toán tử (+) không tương đương với sử dụng phương thức extend.
print(s)
