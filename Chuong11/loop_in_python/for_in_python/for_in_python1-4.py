''' Vòng lặp for lồng nhau trong Python '''

# VD Viết chương trình in ra bảng cửu chương bằng vòng lặp for:
for i in range(1, 10):
    for j in range(1, 10):
        print(f" {i} x {j} = {i * j:<2}", end=" ")
    print(end="\n")
print(end="\n")

''' Sử dụng lệnh if else trong vòng lặp for '''
# VD In ra các số chẵn và số lẻ từ 1 đến 100:

for i in range(1, 100):
    if i % 2 == 0:
        print(i, " là số chẵn")
    else:
        print(i, " là số lẻ")
