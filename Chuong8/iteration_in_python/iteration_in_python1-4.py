'''
	Lặp mảng(list) bằng Iterators trong Python
										 '''
# my_iter.__next__() = next(my_iter)

# Danh sách mảng
my_list = [1, 6, 0, 6]
 
# Chuyển sang iterator
my_iter = iter(my_list)
 
# Lấy phần tử đầu tiên
print(next(my_iter))
 
# Lấy phần tử tiếp theo (thứ 2)
print(next(my_iter))
 
# Lấy phần tử tiếp theo (thứ 3)
print(my_iter.__next__())
 
# Lấy phần tử tiếp theo (thứ 4)
print(my_iter.__next__())