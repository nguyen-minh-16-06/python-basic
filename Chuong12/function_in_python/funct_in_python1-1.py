''' FUNCTION TRONG PYTHON '''

#SYNTAX:

# def <function_name>(parameter_1, parameter_2,....,parameter_3)
#		functinon_block

# Khái niệm về hàm cứ coi là 1 biến.
# Nhưng khi gọi hàm này ra để dùng. 
# Nó không gán, lưu trữ dữ liệu mà nó lưu trữ 1 khối lệnh để ta có thể tái sử dụng lại.
# 1 hàm phải có (), nếu không có thì coi nó là 1 biến.

def Minh():
	pass	# pass này là một lệnh “giữ chỗ” (placeholder statement) 
			# Để giúp cho các block của Python không bị thiếu câu lệnh 
			# Trong trường hợp bạn chưa biết viết gì cho phù hợp.
def minh():
	print('ToitenMinh')

minh() # Gọi hàm minh ra thì hàm này sẽ thực thi khối lệnh bên trong nó
minh() # Đó là print(...)
minh() # Nếu ta gọi n lần thì nó thực thi n lần.