''' PACKING ARGUMENTS với * '''
def minh(*args, nminh): # LƯU Ý: Không được phép để 2 param làm nhiệm vụ packing.
	# Nghĩa là trong 1 hàm chỉ có 1 param là packing.
	# Nếu sau 1 packing param còn những param khác thì khi gọi hàm.
	# Muốn truyền giá trị vào những param đó thì ta phải sử dụng keyword args (K DÙNG POSITIONAL ĐC).
	print(args)
	print(nminh)
minh(*(x for x in range(70)), nminh='Ahihi') # unpack sau đó là pack