""" HÀM MAP TRONG LAMBDA """

""" 
    SYNTAX :map(function, iterable)
                                """

# function: Hàm được áp dụng lên mỗi phần tử của iterable.
# iterable: là dãy dữ liệu (ví dụ: danh sách, tuple, chuỗi) chứa các phần tử cần ánh xạ.

""" USE """
# Được sử dụng để ánh xạ một hàm lên mỗi phần tử của một iterable,
# Chẳng hạn như một danh sách, và trả về một iterator của các kết quả.


# Ví dụ về lũy thừa của 1 dãy số

numbers = [1, 2, 3, 4, 5] # numbers là 1 interable
# Sử dụng map và lambda để tạo một danh sách các bình phương của các số.
squared_numbers = map(lambda x: x**2, numbers)
result = list(squared_numbers)
print(result)


# Chuyển đổi các chuỗi thành độ dài của chúng:

strings = ["hello", "world", "python"] # strings là 1 interable
# Sử dụng map để ánh xạ hàm len lên từng chuỗi trong danh sách
string_lengths = map(len, strings)
result = list(string_lengths)
print(result)

"""
    SYNTAX ĐẦY ĐỦ CỦA HÀM MAP LÀ : map(func, *iterable)
                                                        """
# Một biến chứa hàm lambda:
func = lambda x, y: x + y

# Các interable:
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

# Cú pháp đầy đủ của map
full = map(func, num1, num2) # (lấy giá trị đầu tiên của num1 + giá trị đầu tiên của num2 theo công thức x+y)
                             # (lấy giá trị thứ hai của num1 + giá trị thứ 2 của num2 theo công thức x+y)
                             # ...Và sẽ lấy cho đến khi hết giá trị trong mỗi list thì kết thúc chương trình.

# Ép kiểu list
results = list(full)
print(results)