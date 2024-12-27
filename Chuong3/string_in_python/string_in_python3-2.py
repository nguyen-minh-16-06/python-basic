#TỔNG QUÁT

'''  a = 'minh'
        b = a.center(width,[fillchar]) Đưa về một chuỗi được căn giữa với chiều rộng (width)
            'fillchar' có thể có hoặc không => python sẽ dùng kí tự khoảng trắng để thay thế '''

#Phương thức center trong chuỗi string
a = 'MINH'
b = a.center(30, '-') #Đưa hàm a vào trung tâm của khoảng trống center
#LƯU Ý
'''Kí tự fillchar là một chuỗi có độ dài là 1,VD: 'K' => true
                                              VD: 'K*' => false'''
print(b)

#Phương thức rjust trong chuỗi string
c = 'MINH'
d = c.rjust(30, '-')
print(d)

#Phương thức ljust trong chuỗi string
s = 'MINH'
r = s.ljust(30, '-')
print(r)