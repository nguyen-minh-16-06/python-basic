#Phương thức count trong chuỗi string
a = 'LE NGUYEN MINH'
b = a.count('N',0,10) #Tìm số lượng phần từ có trong một chuỗi
                  #start, end: lấy từ vị trí 0 đến vị trí 10 của chuỗi
print(b)

#Phương thức starswith trong chuỗi string
c = 'LE NGUYEN MINH'
d = c.startswith('LE') #Đưa về giá trị true nếu như chuỗi đó bắt đầu bằng 1 chuỗi nào đó và ngược lại
e = c.startswith('NGUYEN', 3, 2) #Từ vị trí thứ 3 chuỗi 'NGUYEN' sẽ được bắt đầu
print(d)
print(e)

#Phương thức endswith trong chuỗi string
s = 'LE NGUYEN MINH'
f = s.endswith('H') #Đưa về giá trị true nếu như chuỗi đó kết thúc bằng 1 chuỗi nào đó và ngược lại
print(f)