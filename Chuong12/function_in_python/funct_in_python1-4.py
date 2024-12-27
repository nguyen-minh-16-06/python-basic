# Khi tạo một hàm mà có một parameter *.
# Thì Python sẽ hiểu đó không phải là parameter mà chính là syntax. 
# Nó biến các param sau * thành các keyword only argument (chỉ nhận giá trị theo kiểu keyword argument).

def minh(pos_or_key_arg, *, key_arg1, key_arg2):
	print(pos_or_key_arg)
	print(key_arg1)
	print(key_arg2)
minh(1, key_arg1=2, key_arg2='Minh')
# Ta có thể cho key_arg1 = 1, key_arg2 = 2 (default value)
# Thì gọi hàm ta có thể không cần gọi key1, key2 (minh(1)).