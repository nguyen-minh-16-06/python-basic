# KHÁI NIỆM VỀ TUPLE
""" - Được giới hạn bởi cặp ngoặc ( )
    - Các phần tử của tuple được phân cách nhau bởi dấu ','
    - Tốc độ truy xuất của tuple nhanh hơn list, dung lượng chiếm trong bộ nhớ nhỏ hơn list
    - Bảo vệ dữ liệu sẽ không bị thay đổi có thể dùng làm key của dictionary
"""
# Bản chất của tuple cũng là 1 container cũng được sử dụng rất nhiều trong các chương trình python
# Có thể tự chứa chính nó trong bên trong nó
tup = (1, 2, (3, 4, 5), "Minh")
print(tup)
