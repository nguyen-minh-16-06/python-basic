#Phương thức capitalize trong chuỗi string
a = 'le nguyen Minh'
b = a.capitalize() #
print(f"Đưa về một chuỗi với kí tự đầu viết hoa và các kí tự còn lại là chữ thường: {b}")

#Phương thức upper trong chuỗi string
c = 'le nguyen minh'
d = c.upper()
print(f"Tất cả các chữ đều được viết hoa: {d}")

#Phương thức lower trong chuỗi string
e = 'LE NGUYEN MINH'
f = e.lower()
print(f"Tất cả các chữ đều được viết thường: {f}")

#Phương thức swapcase trong chuỗi string
s = 'Le Nguyen Minh'
r = s.swapcase() #Chữ viết hoa => viết thường
                 #Chữ viết thường => viết hoa
print(r)

#Phương thức title trong chuỗi string
q = 'le nguyen minh'
p = q.title() #Đưa về một chuỗi với định dạng tiêu đề (các từ được viết hoa chữ cái đầu tiên
              #còn lại là viết thường
print(p)