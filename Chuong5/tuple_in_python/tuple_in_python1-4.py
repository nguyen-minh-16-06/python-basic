# Indexing và cắt tuple

# Truy xuất phần tử trong tuple
tup = (1, 5, 9)
a = tup[0]  # Lưu ý truy xuất index ta vẫn dùng ngoặc vuông
print(f"Truy xuất phần tử trong tuple: {a}")

# Lấy độ dài trong tuple
b = len(tup)  # Có 3 phần tử trong 1 tuple
print(f"Lấy độ dài trong tuple: {b}")

# Truy xuất tới phần tử cuối của tuple
c = tup[-1]
print(f"Truy xuất tới phần tử cuối của tuple: {c}")

# Hoặc ta có thể sài tup[len(tup)-1]
d = tup[::-1]  # Đảo ngược tuple
print(f"Đảo ngược tuple: {d}")
s = tup[:-1]  # Lấy phần tử thứ bao nhiêu đến bao nhiêu
print(f"Lấy phần tử thứ bao nhiêu đến bao nhiêu trong tuple: {s}")
