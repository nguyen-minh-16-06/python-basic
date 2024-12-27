# while expression:
    # while-block

k = 5
# Khi k = 5 thì in ra giá trị đầu tiên k = 5
# Rồi k - 1 = 4, trừ dần như vậy cho đến khi k = 0 thì không lớn hơn 0 nữa thì hết loop
while k > 0:
    k -= 1
    print("k =", k)

# Sử dụng vòng lặp để xử lí chuỗi, list, tuple:
s = "NGUYENMINH"

# vị trí bắt đầu muốn xử lí của chuỗi
idx = 0

# lấy độ dài chuỗi làm mốc kết thúc
length = len(s)

while idx < length:
    print(idx, 'stands for', s[idx])
    idx += 1
