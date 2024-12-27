# % được hiểu là thay thế cho %s nằm bên trong chuỗi
a = 'My name is %s %s' %('NGUYEN','MINH')

#ta có thể hoàn toàn gán biến 's' vào trong 1 biến khác 'result' và tái sử dụng lại
s = '%s %s'
result = s %('1', '2')

#Định dạng bằng chuỗi f-string
f = '%.f' %(3.4999) #làm tròn thành số 3
s = '%.f' %(3.5999) #làm tròn thành số 4

#VD1
a = 'NM'
rs = f'{a} - dep trai' #Nếu thêm f vào trước chuỗi ta sẽ làm mất đi dấu {} và nó sẽ biến đổi thành NM
print(rs)

#VD về một thông tin cá nhân
name = 'NGUYEN MINH' #nếu tạm thời chưa có dữ liệu cho biến này thì ta sài {{ }} để tạm thời
address = '94 NGUYEN HUE'
phone = '0901796848'
result = f'Student: {{name}}\nAdress: {address}\nPhone: {phone}'
print(result)

#VD2
s = '1: {one}, 2:{two}'.format(one=111, two=222) #có thể đặt tên
r = '1: {1}, 2:{0}'.format(111, 222) #hoặc không cần đặt gì cũng đc, chỉ cần cho theo index là được
print(r)

