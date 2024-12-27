""" HÀM REDUCE TRONG LAMBDA """

""" 
    SYNTAX :reduce(function, sequence[, initial])     
                                                 """

# function: hàm được áp dụng để kết hợp các phần tử.
# sequence: chuỗi hoặc iterable mà bạn muốn kết hợp.
# initial (tùy chọn): giá trị khởi tạo, nếu được cung cấp.

""" USE """
# Là một hàm trong Python nằm trong module functools.
# Được sử dụng để kết hợp các phần tử của một chuỗi (hoặc interable)
# Qua một hàm nhất định để tạo ra một giá trị duy nhất.


# Ban đầu phải import vì hàm reduce này có sẵn trong thư viện functools
from functools import reduce


# Ví dụ dùng reduce để tính tổng các số trong list:
minh = lambda x, y: x + y
numbers = [1, 2, 3, 4, 5]
a = reduce(minh, numbers)
print(a) # 1+2+3+4+5 = 15


# Ví dụ dùng reduce để tính tích các số trong list:
numbers = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x * y, numbers)
print(b) # ({[(1x2)x3]x4}x5) = 120


# Ví dụ dùng reduce để tính tổng các số trong list và giá trị khởi tạo (initial):
# - Có nghĩa là reduce sẽ bắt đầu tính tổng từ giá trị 10
# - Sau đó áp dụng hàm cộng lên từng phần tử của danh sách numbers
numbers = [1, 2, 3, 4, 5]
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial) # 10 + 1 + 2 + 3 + 4 + 5 = 25
