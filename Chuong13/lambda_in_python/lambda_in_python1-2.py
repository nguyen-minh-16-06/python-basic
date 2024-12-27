""" HÀM FILTER TRONG LAMBDA """

"""
    SYNTAX :filter(function or None, iterable)                 
                                               """

# function: là hàm điều kiện được áp dụng cho từng phần tử của iterable.
# iterable: là dãy dữ liệu (ví dụ: danh sách, tuple, chuỗi) mà bạn muốn lọc.

""" USE """
# - Là một hàm được sử dụng để lọc các phần tử của một iterable (danh sách, tuple, hoặc chuỗi)
# - Dựa trên một hàm điều kiện được xác định trước.
# - Áp dụng cho từng phần tử của iterable.
# - Và chỉ các phần tử thỏa mãn điều kiện sẽ được giữ lại trong kết quả.


# Ví dụ lọc lấy các số dương (lớn hơn 0)
funct = lambda x: x > 0
minh = [1, -3, 5, 0, 2, 6, -4, -9] # minh là 1 interable
print(list(filter(funct, minh)))


# list comprehension tương đương với hàm filter trên:
print([x for x in minh if x > 0])


# Ví dụ khác khi gửi None thay vì một function:
minhz = [0, None, 1, 'Minh', '', 'dep zai', 69, False]
print(list(filter(None, minhz)))
