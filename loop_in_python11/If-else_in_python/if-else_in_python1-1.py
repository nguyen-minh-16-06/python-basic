#VD 1:
x = int(input("Nhap mot so: "))
if x < 0:
   print('So am')
elif x == 0:
   print('So 0')
elif x == 1:
   print('So 1')
else:
   print('So duong')

#VD 2:
a = int(input('Nhap 1 so binh thuong:'))
if a % 2 == 0:
    print (str(a) + " là số chẵn")
else:
    print (str(a) + " là số lẻ")

#VD 3:
number1 = 20
number2 = 300
number3 = 70
# Giả sử số number1 là lớn nhất
max = number1
 # Kiểm tra xem số number2 có lớn hơn số max không
if max < number2:
# Nếu có thì phải đổi số lớn nhất thành number2
    max = number2
 # Tương tự, ta sẽ kiểm tra cho số thứ 3
if max < number3:
    max = number3
print ("Số lớn nhất là " + str(max))