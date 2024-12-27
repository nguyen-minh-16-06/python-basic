''' So sánh giữa hai iterable cùng loại '''
 # Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord.
 # ord('A') = 65, ord('a') = 97.
 # Có thể tham khảo giá trị của nó trong ASCII Table.

a = 'MINH' == "MINH"
print(a)
True 

b = 'LE' == 'MINH'
print(b)
False

'''
	Khi bạn so sánh bằng các toán tử ==, >=, <= thì Python sẽ so sánh hết các phần tử.
		Còn nếu bạn dùng các toán tử như >, <, != thì Python sẽ không cần đi hết các giá trị iterable. 
			Nếu như ở vị trí i nào đó mà đã hai giá trị không bằng nhau thì nó sẽ dừng lại.
																							'''
'a' > 'ABC' 
# ord('a') không bằng ord('A'),
# Không cần so sánh tiếp và ord('a') > ord('A') là đúng => True
True
'aaa' < 'aaAcv' 
# ord('a') không bằng ord('A') ở vị trí thứ 2
# Không cần so sánh tiếp và ord('a') < ord('A') là sai => False
False
'aaa' < 'aaaAcv' 
# 3 phần tử đầu tiên bằng nhau. 
# Ở phần tử thứ tư, ta sẽ so sánh 0 và ord('A') và dĩ nhiên ord('A') > 0 => True
True																							