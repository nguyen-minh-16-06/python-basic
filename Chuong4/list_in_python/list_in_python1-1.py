# TỔNG QUÁT VỀ LIST
"""
List được giới hạn bởi các cặp ngoặc vuông [   ]
- Những gì nằm bên trong [  ] được gọi là các phần tử của list
- Các phần tử của list dc cách nhau bởi dấu ','
- List có khả năng chứa mọi giá trị đối tượng trong python và bao gồm cả chính nó
- List rỗng là list không có gì trong [   ]
"""

a = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [['NGUYEN'], ['MINH']]]
print(a)

# syntax 'list comprehension for i in range()'
# Có nghĩa là tạo ra 1 list gắn vào biến 1 biến và in nó ra màn hình

# Tạo ra 1 list từ 0 đến 30 (tạo ra 30 phần tử bắt đầu từ 0)
b = [i for i in range(30)]
print(b)

c = [[n, n * 1, n * 2] for n in range(1, 5)]
print(c)

# ----------------------------------------------------------------------------------------------------------------------
# Lấy từng phần tử trong list
fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
print(fruits[3])
# Mỗi giá trị trong list được coi là 1 phần tử, và nếu cố gắng truy xuất một phần tử nằm ngoài
# thì sẽ báo lỗi list index out of range (tức là nằm ngoài phạm vi trong list)
# print(fruits[4])

# Truy xuất toàn bộ phần tử:
print(fruits[:])

# Nếu muốn truy xuất 3 phần tử đầu tiên thì sử dụng:
print(fruits[0:4])

# Thậm chí không cần thiết số 0 ở trước dấu 2 chấm:
print(fruits[:4])
print(fruits[:-1])

# Tương tự với tham số ở sau:
print(fruits[::2])

# Có thể lấy các phần tử ngược lại nếu như cho bước nhảy từ -1
print(fruits[::-1])

# Có thể lặp lại chúng bằng for loop:
for fruit in fruits:
    print(fruit)

# Có thể xem thêm các chức năng khác bằng cách sử dụng hàm dir() và xem cách sử dụng bằng hàm help:
# print(dir(fruits))
# print(help(fruits))

# Cách để kiểm tra xem 1 list có bao nhiêu phần tử, sử dụng hàm len():
print(len(fruits))

# Cách kiểm tra 1 phần tử có trong list hay không bằng cách sử dụng toán tử in:
print("apple" in fruits)
print("pineapple" in fruits)

# Ta có thể thay đổi giá trị trong list hoàn toàn khả thi, tương tự cho index = 1, 2, 3
fruits[0] = "pineapple"
print(fruits)
