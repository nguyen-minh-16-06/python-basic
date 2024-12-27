#Bây giờ chúng ta sử dụng mô-đun vừa tạo bằng cách sử dụng câu lệnh import
import module_in_python
#Nhập module có tên module_in_python, và gọi hàm greeting
module_in_python.greeting("Minh")
"""LƯU Ý: - Khi sử dụng hàm từ module,hãy sử dụng cú pháp: module_name.function_name.

- Module có thể chứa các hàm như đã được mô tả,
nhưng cũng có thể chứa các biến thuộc mọi loại (function,list, dict, objects, v.v.):"""
#VD; Nhập mô-đun có tên module_in_python và truy cập từ điển person1:
import module_in_python
a = module_in_python.person1["age"]
print(a)

"""
- Bạn có thể tạo bí danh khi nhập mô-đun bằng cách sử dụng từ khóa as:"""
import module_in_python as mx
a = mx.person1["country"]
print(a)

"""
- Có một số mô-đun tích hợp sẵn trong Python mà bạn có thể nhập bất cứ khi nào bạn muốn."""
import platform
x = platform.system()
print(x)

"""
- Có một hàm tích hợp để liệt kê tất cả các tên hàm (hoặc tên biến) trong một mô-đun. Hàm dir():"""
import platform
z = dir(platform)
print(z)