'''
	Lặp tuple bằng Iterators trong Python
										 '''								
# Danh sách dạng tuple
words = ("Xin", "chào", "các", "bạn")
 
# Chuyển nó thành Iterators
iword = iter(words)
 
# Sử dụng next để lấy từng phần tử.
print(next(iword)) # Xin
print(next(iword)) # Chào
print(next(iword)) # Các
print(next(iword)) # Bạn