strA = 'NGUYENMINH'

#Vị trí nằm trong phạm vi mà chuỗi có
strC = strA[0]
print(strC)

#Một số trường hợp không thể xác định được phạm vi của chuỗi
# strB = strA[10] IndexError: string index out of range (vị trí nằm ngoài phạm vi mà chuỗi có)
# strB = strA[1.2] (không thể là số thực)
# strB = strA['1'] (không thể là 1 chuỗi được mà phải là 1 số nguyên)

#len là 1 hàm lấy ra độ dài bên trong (  ) của nó
a = strA[len(strA)-1]
print(a)

#Lấy độ dài của chuỗi nhập vào từ biến name
name = input("Nhập tên của bạn vào: ")
result = len(name)

print(result)

#VD về cắt chuỗi
strB = 'NGUYENMINH'

strB = strA[1:5] #Lấy từ vị trí 1->4 và không lấy vị trí 5

#lấy hết từ vị trí 1->cuối
strB = strA[1:len(strA)]
strB = strA[1:None]
strB = strA[None:None]
strB = strA[:None]
strB = strA[None:]
strB = strA[:]

#VD cắt từ phải qua trái
strB = strA[None:None:2] #[Vị trí đầu:vị trí hai:bước nhảy]
print(strB)