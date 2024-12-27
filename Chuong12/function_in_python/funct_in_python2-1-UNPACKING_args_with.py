''' UNPACKING ARGUMENTS VỚI * '''

def minh(m, i, n, h): # Hàm này gồm 4 param (m, i, n, h) và không có arguments
	print(m)
	print(i, n)
	print('end', h)
# Có một vấn đề, 4 argument cần  truyền vào khi gọi hàm này lại nằm trong một List.
lst = ['123', 'Minh', 16.06, 'GAM'] 
''' minh(lst[0], lst[1], lst[2], lst[3]) # Dùng indexing truyền từng phần tử vào args. '''

# Và sẽ ra sao nếu như có 50 parameter (không còn là 4).
# Vậy nên ta sử dụng phương pháp unpacking args

minh(*lst)
# Khi sử dụng *, không chỉ có thể unpack được các List
# Mà có thể unpack các container khác như Tuple, Chuỗi, Generator, Set, Dict (chỉ lấy được key).

# LƯU Ý: Điều này chỉ có thể áp dụng với các positional args. Nếu sử dụng keyword chương trình sẽ báo lỗi.
''' 
	def a(*, s, d):	# Sau * là các keyword args.
		print(s, d)
	a(*('a', 'b')) # Chương trình sẽ báo lỗi nếu chạy, vì chỉ chấp nhận positional args. 
																						'''