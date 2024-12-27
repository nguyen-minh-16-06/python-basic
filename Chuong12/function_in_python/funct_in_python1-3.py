''' Positional argument và keyword argument '''

def minhz(a, b, c, d):
	pass # lệnh giữ chỗ.

''' POSITIONAL ARGUMENT '''
# 16 và 'NGUYENMINH' gọi là positional argument.
# positional argument : CÓ NGHĨA LÀ TRUYỀN THEO ĐÚNG THỰ TỨ.
minhz(16, 'NGUYENMINH')

''' KEYWORD ARGUMENT '''
# a = 16, b = 'NGUYENMINH' là những keyword argument, default value.
# Và ta có thể thay ( a =, b = thành b =, a = ) vẫn được ( Thay đổi vị trí truyền param, args vào).
# keyword argument : CÓ NGHĨA LÀ TRUYỀN KHÔNG CẦN THEO ĐÚNG THỨ TỰ, CÓ THỂ THAY ĐỔI ĐƯỢC.
minhz(a = 16, b = 'NGUYENMINH')

# TRƯỜNG HỢP KHÁC:
# Ta có thể cho cả positional và keyword cùng nhau
# NHƯNG: POSITIONAL PHẢI Ở PHÍA TRƯỚC KEYWORD:
minhz(16, 'MINH', c = 1, d = 2)
	 #POSITIONAL    	KEYWORD.

# VÍ DỤ CỤ THỂ:
# def Minh_with_sone(name, verb):
#     print('MINH', verb, name)
# Minh_with_sone('HTML', verb='likes') ( Chạy được )
# Minh_with_sone(verb='like', 'CSharp') ( Báo lỗi )

# VÍ DỤ:
# def minh(a, b=2, c=3, d=4):
#	f = (a + d) * (b + c)
#	print(f)
# minh(1, d = 5)