# VD1:
x = int(input("Nhập một số: "))
if x < 0:
    print("Số âm")
elif x == 0:
    print("Số 0")
elif x == 1:
    print("Số 1")
else:
    print("Số dương")

# VD2:
a = int(input('Nhập 1 số bình thường:'))
if a % 2 == 0:
    print(str(a) + " là số chẵn")
else:
    print(str(a) + " là số lẻ")

# VD3:
number1 = 20
number2 = 300
number3 = 70
# Giả sử số number1 là lớn nhất
_max = number1
# Kiểm tra xem số number2 có lớn hơn số max không
if _max < number2:
    # Nếu có thì phải đổi số lớn nhất thành number2
    _max = number2
# Tương tự, ta sẽ kiểm tra cho số thứ 3
if _max < number3:
    _max = number3
print("Số lớn nhất là " + str(_max))
