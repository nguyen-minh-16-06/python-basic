''' HÀM TÌM GIÁ TRỊ LỚN, NHỎ NHẤT - MAX, MIN '''
''' 
	Syntax: 
		   max(iterable, *[, default=obj, key=func])
		   						  					 '''

itera = (x for x in range(3))
print(itera)
print(max(itera))

# Hoặc: 
''' 
	Syntax: 
		   max(arg1, arg2, *args, *[, key=func])
		   						  				 '''
itera = (x for x in range(3))
print(itera)
print(max(16,0,6))


''' Trường hợp khác '''

# Nếu như trường hợp không có giá trị nào max cả thì hàm sẽ trả ra giá trị default như dưới.
iters = (y for y in range(3))
print(max([], default = 'Minh'))