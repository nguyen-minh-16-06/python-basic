# Python compound interest calculator

so_du = 0
lai_suat = 0
nam = 0

while True:
    so_du = float(input("Vui lòng nhập số dư gốc ban đầu: "))
    if so_du < 0:
        print("Số dư không thể bé hơn hoặc bằng không!")
    else:
        break

while True:
    lai_suat = float(input("Vui lòng nhập lãi suất: "))
    if lai_suat < 0:
        print("Lãi suất không thể bé hơn hoặc bằng không!")
    else:
        break

while True:
    nam = float(input("Vui lòng nhập số năm: "))
    if nam < 0:
        print("Năm không thể bé hơn hoặc bằng không!")
    else:
        break

total = so_du * pow((1 + lai_suat / 100), nam)
print(f"Số dư sau {nam} năm là: {total:.2f}VNĐ")
