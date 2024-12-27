'''Chuỗi trần sẽ không quan tâm đến escape sequence đó là thêm 1 chữ r vào trước chuỗi'''
print(r'Haiz, \neu 1 ngay nao do')

#VD về toán tử cộng

strA = 'NGUYEN'
strB = 'MINH'
strC = strA + '\n' + strB
print(strC)

#VD về toán tử nhân
#python hỗ trợ toán tử nhân cho chuỗi => tạo ra n chuỗi tương ứng 1 cách nhanh chóng

strA = 'NGUYEN\n'
strB = 'MINH'
strc = strA*5
print(strc)

#VD về 'in'
#Nếu như strB tồn tại trong strA thì kết quả đưa ra là 'true' và ngược lại

strA = 'NGUYEN'
strB = 'N'
sTrC = strB in strA
print(sTrC)