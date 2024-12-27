#Import From Module

"""Bạn có thể chọn chỉ nhập các phần từ một module bằng cách sử dụng từ khóa from"""
from module_in_python import person1
print(person1["age"])
"""Lưu ý: Khi nhập bằng từ khóa from, không sử dụng tên module khi đề cập đến các thành phần trong mô-đun.
Ví dụ: Person1["age"], không phải module_in_python.person1["age"]"""