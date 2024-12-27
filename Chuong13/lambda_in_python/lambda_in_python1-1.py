""" LAMBDA IN PYTHON """
"""
	SYNTAX:
			lambda argument_1, argument_2, …, argument_n : expression 
																	  """
# - Là một expression, không phải là một câu lệnh.
# - Là một dòng expression duy nhất, không phải là một khối lệnh.
# - Lambda function có thể có nhiều tham số, nhưng nội dung bên trong chỉ có một biểu thức.
# - Với lambda chỉ cần ghi giá trị mà không cần ghi return.
# - Có thể sử dụng các câu lệnh điều kiện mà không cần phải sử dụng tới lệnh “if”.
# - Ưu tiên dùng cho việc tạo ra những hàm đơn giản, còn phức tạp thì sử dụng đến từ khóa “def”.


# Ví dụ:
average = lambda a, b, c: (a + b+ c)/3
print(average(1,2,3))


""" 
	default arguments 
					  """

power_a = lambda x, a=2: x ** a
print(power_a(2))


"""
	Global & Local 
				   """

def minh():
	s = lambda x: x + " is a girl friend Minh's "
	return(s) #trả về một hàm nặc danh
call_mem = minh() #lấy biến call_mem giữ hàm nặc danh
print(call_mem('My')) #giá trị chuỗi được đưa vào cho biến x
print(call_mem) #ra 1 generator


""" 
	Ví dụ mà lambda chiếm ưu thế hơn so với 'def': 
												   """

_lst = [lambda x: x**2, lambda x: x**3, lambda x: x**4] # một list với các phần tử là các hàm nặc danh
print(_lst[0](2)) # _lst[index](giá trị)

# Có thể sử dụng vòng lặp for
for func in _lst:
	print(func(3))  # 3**2, 3**3, 3**4


""" 
	Câu điều kiện cho lambda 
							"""

find_greater = lambda x, y: x if x > y else y
print(find_greater(1, 3))