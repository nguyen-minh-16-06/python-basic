# Tuple và chuỗi đều là 1 dạng hash object
# 1 hash object là 1 đối tượng ta không thể thay đổi nội dung của nó

# Ma trận trong tuple
tup = ((1, 5, 9), (1, 5, 9), (1, 5, 9))
print(tup)

# Phương thức count trong tuple
Tup = (1, 1, 2, 5, 6)
a = Tup.count(1)  # số lần phần tử xuất hiện trong tuple
print(a)

# Phương thức index trong tuple

tUp = (1, 2, 3, 4, 6)
b = tUp.index(4)  # Lấy ra vị trí xuất hiện của phần tử đó trong tuple
# Nếu không có giá trị trong tuple thì chương trình báo lỗi
print(b)

""" Tuple khác list ở chỗ : - Tuple không cho phép ta sửa chữa nội dung và list thì ngược lại """
