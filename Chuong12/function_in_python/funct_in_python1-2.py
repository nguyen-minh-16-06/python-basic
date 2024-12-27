def minh(text): # paramater chính là [ (text) - (biến khởi tạo) ]
	# Khi gọi hàm, ta phải truyền 1 paramater (tham số) tương ứng.
	# Paramater là 1 biến, và biến này là giá trị truyền từ BÊN NGOÀI vào ('Minh')
	print(text)
	# Sẽ không cố định statements (câu lệnh) nằm bên trong hàm def này.

# Làm điều này vì nó dễ dàng thay đổi, update.
# Và rất khó để thay đổi giá trị cố định bên trong hàm, có thể dẫn đến sai.
# Vậy nên hợp lí nhất thì hãy sử dụng hàm def để truyền từ bên ngoài vào dễ dàng sửa đổi, update.
# Cái nằm trong dấu () là paramater, và sài nó như sài biến.
# Nó như 1 cầu nối trung gian giữa nơi gọi hàm và nội bộ của hàm.
# Và là cầu nối trung gian nên nó sẽ lấy dữ liệu từ minh('Minh') và đưa vào trong print(text) để xài.

minh('Minh') # arguments chính là 'Minh' - ( là giá trị)

# Có thể đưa nhiều param và args hoàn toàn không sao cả.
# LƯU Ý: Nếu hàm có bao nhiêu param thì phải truyền vào đúng số agru, nếu không chương trình báo lỗi.
def Minh(text, age):
	print(text, end = ' ')
	print(age)

Minh('MINH', 16)

# Khởi tạo 1 hàm, và cho default agrs là 1 list.
def f(nminh=[]):
	# Mỗi lần gọi hàm nminh thì lại append 'M' vào.
	nminh.append('M')
	# in nminh ra.
	print(nminh)
f()
f()

''' print(nminh) '''
# LƯU Ý: Nếu ta print(nminh) này ra thì chương trình sẽ báo lỗi.
# Vì nminh chỉ thuộc phạm vi hàm f thôi. Nên nếu ta gọi bên ngoài sẽ không được.
# Hay còn gọi là biến cục bộ (chỉ được sài trong phạm vi thằng tạo ra nó).
