# ARRAY (MẢNG/MA TRẬN)
""" BẢN CHẤT LÀ 1 MẢNG 2 CHIỀU """
'''CÓ NHIỀU TÍNH CHẤT TƯƠNG TỰ VỚI LIST'''
'''1 LIST là 1 danh sách 1 chiều => n phần tử đi theo 1 hướng'''

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[0][2])  # [hàng 1][truy xuất vào hàng 1, cột 3]
print(a[1][1])  # [hàng 2][truy xuất vào hàng 2, cột 2]
print(a[2][0])  # [hàng 3][truy xuất vào hàng 3, cột 1]
''' Bản chất [MA TRẬN] trong python là 1 list nằm bên trong 1 list '''

# NOTE : 1. Không được phép gán list này qua list kia nếu không có chủ đích.
b = [1, 2, 3]
c = list(b)
print(b)
print(c)
c[0] = 'MINH'  # Khi ta gán giá trị c[0] = 'MINH' => b[0] cũng được biến đổi thành 'MINH'
# Vì b & c này đang có cùng 1 giá trị nên đều cùng đưa về 1 vùng nhớ => thằng c thay đổi thì b cũng thay đổi
# Sửa lỗi này bằng cách sử dụng list constructor | c = list(b) |
print(b)
print(c)
