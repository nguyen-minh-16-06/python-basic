'''
	Xử lí file trong python
							'''
# Mở file trong python bằng cách sử dụng file = open('abcxyz.txt')

# Đóng file trong python bằng cách sử dụng file.close()
''' Phương thức đóng file này sẽ không an toàn trong 1 số trường hợp nên:
	Ta sử dụng từ khóa with, nó sẽ đảm bảo rằng file sẽ luôn được đóng khi lệnh kết thúc.
	 		Syntax:
	 		 		with open("abcxyz.txt") as file:
	Và ta cũng không cần phải gọi hàm close() vì nó tự động thực hiện ngầm.
																			'''

''' 
	LƯU Ý: - Nếu ta open file tên thì chương trình sẽ chạy
	đến file .txt cùng thư mục với file python của mình.
	- Còn nếu ta chạy file nhưng kh có thư mục nào cả thì chương trình sẽ báo lỗi
	trừ khi ta chạy file dưới dạng ổ đĩa
										 '''

'''MODE xử lý file trong python'''

'''
	Syntax:
		open('file.txt', mode = 'r')
									'''
file = open('LE NGUYEN MINH.txt', 'r')
print(file)

# Có nhiều loại mode:
''' 
	- r : mở để ĐỌC (Mặc định có sẵn).
	- r+ : mở để GHI và ĐỌC.
	- w : mở để GHI, ,tạo file mới nếu file không tồn tại, làm sạch file nếu nó đã tồn tại.
	- w+ : mở để GHI và ĐỌC, tạo file mới nếu file không tồn tại, làm sạch file nếu nó đã tồn tại.
	- a : mở để GHI, nếu không tồn tại sẽ tạo ra 1 file mới với tên mà chúng ta truyền vào.
	- a+ : mở để GHI và ĐỌC, nếu không tồn tại sẽ tạo ra 1 file mới với tên mà chúng ta truyền vào.
	- + : mở file ở cả hai chế độ ĐỌC và GHI. 
											'''