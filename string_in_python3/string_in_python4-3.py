#Phương thức find trong chuỗi string
a = 'LE NGUYEN MINH'
b = a.find('N') #Đưa về 1 giá trị số nguyên (chỉ số index) của nơi mà find tìm thấy kí tự
print(b)

#Phương thức rfind trong chuỗi string
c = 'LE NGUYEN MINH'
d = c.rfind('E') #Đưa về 1 giá trị số nguyên của nơi mà find tìm thấy chuỗi trên từ phải sang trái, trả về -1 nếu không tìm thấy chuỗi hoặc kí tự trong chuỗi
print(d)

#Phương thức index, rindex trong chuỗi string
s = 'LE NGUYEN MINH'
f = s.index('N') #Cách hoạt động cũng giống như find, rfine chỉ khác khi không tìm thấy chuỗi thì nó sẽ báo lỗi
#invaluabe
print(f)

#Phương thức isdigit trong chuỗi string
x = '5'
y = x.isdigit() #Giúp ta kiểm tra xem trong chuỗi có là 1 số hay không, nếu không thì => false
print(y)

z = '5a'
u = z.isdigit()
print(u)

#Phương thức isspace trong chuỗi string
v = '   '
n = v.isspace() #Đưa về true nếu tất cả các kí tự trong chuỗi là khoảng trắng và ngược lại
print(n)