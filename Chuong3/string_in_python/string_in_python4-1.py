#TỔNG QUÁT

#Phương thức split trong chuỗi string
a = 'LE NGUYEN MINH'
b = a.split(' ', 1) #Đưa về 1 list kiểu dữ liệu bằng cách chia các phần tử bằng kí tự set
#tham số maxsplit (mặc định là -1) được địnnh nghĩa là số lần được tách thông qua maxsplit
print(b)

#Phương thức rsplit trong chuỗi string
c = 'LE NGUYEN MINH'
d = c.rsplit(' ', 1)
print(d)

#Phương thức partition trong chuỗi string
s = 'LE NGUYEN MINH'
f = s.partition('NGUYEN') #partition cắt các phần tử ở trước, sau của chuỗi 'NGUYEN' từ trái sang phải
print(f)

#Phương thức rpartition trong chuỗi string
q = 'LE NGUYEN MINH'
p = q.rpartition('NGUYEN') #partition cắt các phần tử ở trước, sau của chuỗi 'NGUYEN' từ phải sang trái
print(p)

