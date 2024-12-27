''' SỬ DỤNG PRINT THÔNG QUA PARAMETER '''

'''
	Syntax:
		   print(*objects, sep = ' ', end = '/n', file = sys.stdout, flush = False)
		   																   			'''
# OBJECTS:

''' Chính là packing argument. 
Ở đây dễ hiểu là nó sẽ gom lại các argument của bạn lại thành một Tuple.'''

# Ví dụ: packing = 1, 2, 3, 4 
# => (1, 2, 3, 4)

# Nếu ta sử dụng print như này sẽ báo lỗi vì chương trình kh thể in ra 2 kiểu dữ liệu khác nhau:
print('MINH' + 16)

# Ta có thể sử dụng ép kiểu để print bằng cách: 
print('MINH' + str(16))

# Hoặc ta có thể sử dụng dấu phẩy (sep - separate) để phân chia ra:
print('MINH', 16)
print(123, [1, 2, 3], 'MINH')