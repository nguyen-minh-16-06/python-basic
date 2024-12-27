#kiểu dữ liệu cơ bản
strA = '69' + '5' #kiểu dữ liệu chuỗi
strB = 69 + 5 #kiểu dữ liệu số

#Ép kiểu
strC = int('69') + 5 #ép kiểu dữ liệu số nguyên vào một chuỗi
strD = str(69) + '5' #ép kiểu dữ liệu chuỗi vào một số
strE = float(6) #ép kiêu dữ liệu số thực
strF = int(6.9) #ép kiểu dữ liệu số nguyên (chỉ lấy phần nguyên)

#thay thế một từ sang một từ khác
a = 'NMINH'
b = a.replace('N','D')
print(b)