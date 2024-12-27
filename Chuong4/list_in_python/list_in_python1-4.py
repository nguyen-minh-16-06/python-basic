# Indexing & cắt list trong python
""" LIST và CHUỖI giống nhau trong rất nhiều điểm """

a = [1, 2, "a", "b", "c", [3, 4]]
b = a[0]     # [0] - [chỉ số index]
c = a[5][1]  # [5][1] - [chỉ số index][chỉ số index nằm trong list đó]
d = a[1:6]   # [1:6] - lấy index 1 cho đến index 6
# index bắt đầu từ '0' và kết thúc bởi 'n-1' với n chính là độ dài của list
print(b)
print(c)
print(d)

# Thay đổi nội dung list trong python
# NOTE: Không thể thay đổi nội dung của 1 chuỗi, nhưng list có thể làm được

s = [1, 2, "a", "b", "c", [3, 4]]
print(f"List khi chưa thay đổi là: {s}")
s[1] = "MINH"  # Thay đổi giá trị của index 1 = chữ 'MINH'
f = s[1]
print(f)
print(f"List sau khi thay đổi là: {s}")
