'''CÁC PHƯƠNG THỨC LIST TRONG PYTHON'''

#Phương thức COUNT trong list
a = [1,2,1,3,4,5,6]
b = a.count(1) #Cho ta biết số lần xuất hiện của n phần tử là bao nhiêu lần
#syntax : x.count(n)
print(b)

#Phương thức INDEX trong list
c = [1,2,3,4,5,6]
d = c.index(2) #Đưa ra vị trí của phẩn tử đó nằm trong list
#tương tự như index của chuỗi
#Nếu như không có số nào tồn tại trong list thì index sẽ báo lỗi
print(d)

#Phương thức COPPY trong list
s = [2,3,4,5,6,7]
f = s.copy() # Tạo ra 1 bản sao khác với bản gốc ban đầu (ta có thể hiểu rằng copy() như 1 list constructor)
f[0] = 'MINH'
print(f)
print(s)
