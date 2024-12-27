# TỔNG QUÁT VỀ LIST
'''
List được giới hạn bởi các cặp ngoặc vuông [   ]
- những gì nằm bên trong [  ] được gọi là các phần tử của list
- các phần tử của list dc cách nhau bởi dấu ','
- list có khả năng chứa mọi giá trị đối tượng trong python và bao gồm cả chính nó
- list rỗng là list không có gì trong [   ]
'''

a = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [['NGUYEN'], ['MINH']]]
print(a)

# syntax 'list comprehension'
# Có nghĩa là tạo ra 1 list gắn vào biến b và in nó ra màn hình

# tạo ra 1 list từ 0 đến 30 (tạo ra 30 phần tử bắt đầu từ 0)
b = [minh for minh in range(30)]
print(b)

c = [[n, n * 1, n * 2] for n in range(1, 5)]
print(c)
