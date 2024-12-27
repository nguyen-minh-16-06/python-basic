# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# Vòng lặp lồng nhau = Một vòng lặp trong một vòng lặp khác (bên ngoài, bên trong)
#               vòng lặp bên ngoài:
#                   vòng lặp bên trong:

# VD 1: for lồng for
# Xài range(1, 4) tương tự với range(3)
# Giống nhau: Lặp qua 3 hàng với range(1, 4) chạy từ 1 -> 3, còn range(3) chạy từ 0 -> 2
# Khác nhau: Với range(1, 4) bắt đầu từ 1, còn range(3) chạy từ 0
for i in range(3):
    for j in range(1, 10):
        print(j, end=" ")
    print(end="\n")
#   print() # Tương tự như trên

# VD 2: for lồng while
for i in range(3):
    j = 0
    while j < 2:
        print("For lồng while !")
        j += 1
    print(end="\n")

# VD 3: while lồng while
i = int(input("Nhập i: "))
while i < 3:
    j = 0
    while j < 2:
        print("While lồng while !")
        j += 1
    i += 1
    print(end="\n")

# VD 4: while lồng for
x = int(input("Nhập x: "))
while x < 3:
    for y in range(2):
        print("While lồng for")
        y += 1
    x += 1
    print(end="\n")

# VD 5: Thực hành
rows = int(input("Nhập số hàng: "))
columns = int(input("Nhập số cột: "))
symbol = input("Nhập hình sử dụng: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
