'''
	Một số hàm hỗ trợ cho iterable object trong Python
													   '''
# Một điều lưu ý: 
# Các hàm này buộc phải lấy các giá trị của iterable để xử lí
# Do đó nếu bạn đưa vào một iterator. Thì bạn sẽ không sử dụng iterator đó được nữa.

''' HÀM TÍNH TỔNG - SUM '''
''' 
	Syntax: 
		   sum(iterable, start=0)
		   						  '''
# Cho x chạy từ 0 -> 2
itera = (x for x in range(3))
'''Cộng lại hết cả 3 phần tử bằng hàm sum => itera = 3
		Sau đó cộng thêm 2 nữa = 5 (Vì ban đầu ta đã đến số 3, thì mặc định
			của start = 0 khi ta đổi thành 2 thì nó sẽ bắt đầu từ 2 nghĩa là + thêm 2)'''
print(sum(itera,2))
'''
	LƯU Ý: Khi ta sử dụng hàm sum rồi thì không thể sử dụng bất kì hàm nào nữa cả
			Ví dụ khi ta sử dụng hàm next() thì chương trình sẽ báo lỗi
																		'''
