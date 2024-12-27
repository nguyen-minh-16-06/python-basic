#Phương thức mã hoá (encode) trong chuỗi string
a = 'ảo thật đấy'
b = a.encode(encoding='utf-8', errors='strict') #Thậm chí không cần có hàng (encoding='utf-8', errors='strict') ta vẫn có thể mã hoá được
print(b)

#Phương thức join trong chuỗi string
c = 'NGUYEN MINH'
d = c.join(['1','2','3','4']) #c = '1NGUYEN MINH2NGUYEN MINH3NGUYEN MINH4'
print(d)

#Phương thức replace trong chuỗi string
s = 'MINH'
r = s.replace('I', 'H')
#r = s.replace('N', 'H', 2) #Với 2 là thứ tự thay, ví dụ như 'NGUYEN MINH' thay 2 chữ N thành chữ H
print(r)

#Phương thức strip trong chuỗi string
z = 'NGUYEN MINH'
f = z.strip('N') #Đưa z về 1 chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi
print(f)

#Phương thức l/rstrip trong chuỗi string
q = 'NGUYEN MINH'
p = q.rstrip('NH') #Đưa q về 1 chuỗi với việc cắt bên phải của chuỗi
print(p)

x = 'NGUYEN MINH'
y = x.lstrip('NG') #Đưa x về 1 chuỗi với việc cắt bên trái của chuỗi
print(y)