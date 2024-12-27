""" GENERATOR IN PYTHON """
"""
- Là iterator, một dạng của iterable.
- Nhưng khác là không thể tái sử dụng.
- Generator không lưu trữ tất cả các giá trị của bạn ở bộ nhớ, mà nó sinh ra lần lượt.
																					  """
kteam_gen = (value for value in range(3))
for value in kteam_gen:
	print(value)

""" 
- Nếu như ta tái sử dụng Generator lại 1 lần nữa thì
- Đương nhiên, sẽ không có giá trị nào được in ra nữa
- Vì khi nó sinh ra giá trị đầu tiên là 0, rồi ta lại 
- Tiếp tục gọi nó thì nó sẽ sinh ra giá trị 1, nghĩa là 
- Sẽ vứt đi giá trị 0, và nếu ta yêu cầu nó sinh ra giá trị 
- Mới thì nó sẽ vứt đi giá trị phía trước. Lặp lại cho đến khi kết thúc.

			for value in kteam_gen:
				print(value)
																		"""
def gen():
    for i in range(4):
        x = yield i   # cái này là lấy giá trị i xuất ra ngoài luôn, nên x chỗ này lúc nào cũng là None
        print('value sent from you', x)