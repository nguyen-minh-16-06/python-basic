""" CÁC PHƯƠNG THỨC LIST CẦN THIẾT TRONG PYTHON """

# Phương thức APPEND trong list
a = [1, 2, 3]
print(f"Trước khi a.append: {a}")
a.append([4, 5])  # Được dùng để thêm 1 đối tượng vào một danh sách
# Đối tượng này có thể thuộc bất kì kiểu dữ liệu, chuỗi, số nguyên, boolean. Thậm chí là 1 danh sách khác.
print(f"Sau khi a.append([4, 5]): {a}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức POP trong list
b = [1, 2, 3]
print(f"Trước khi b.pop: {b}")
b_after_pop = b.pop(1)  # Bỏ đi phần tử thứ i trong list và trả về giá trị đó
print(f"Sau khi b.pop(1): {b}")
print(f"Phần tử được pop: {b_after_pop}\n")
# Nếu như pop không có giá trị bên trong d.pop() => phần tử cuối cùng nằm bên trong list sẽ được pop
c = [1, 2, "apple"]
print("LƯU Ý:")
print(f"Trước khi c.pop: {c}")
c_after_pop = c.pop()
print(f"Sau khi c.pop(): {c}")
print(f"Phần tử được pop khi giá trị bên trong c.pop() là rỗng: {c_after_pop}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức INSERT trong list
# Được dùng để chèn 1 giá trị, phần tử, đối tượng tại 1 index nhất định
d = [2, 3, 4, "banana", "apple"]
print(f"Trước khi d.insert: {d}")
d.insert(0, [0, 1])  # Tại vị trí 0 thêm 1 list [0, 1] vào list hiện tại
# Nếu như index lớn hơn số phần tử có trong list thì phần tử trong index sẽ bị đưa về cuối.
print(f"Sau khi d.insert(0, [0, 1]): {d}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức REVERSE trong list
e = [1, 2, 3, 4]
print(f"Trước khi e.reverse: {e}")
e.reverse()  # Ra một list đảo ngược lại
print(f"Sau khi e.reverse(): {e}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức SORT trong list
f = [9, 1, 2, 3]
print(f"Trước khi f.sort: {f}")
f.sort()  # Sắp xếp 1 list theo thứ tự tăng dần (tương đương với f.sort(reverse=False))
print(f"Sau khi f.sort(): {f}\n")

# Sắp xếp các phần tử của LIST theo thứ tự giảm/tăng dần
# Nếu ta sài reverse=True thì sort sẽ sắp xếp theo thứ tự giảm dần
g = ["a", "b", "c", "d", 'e', 'f', 'g', 'h']
print(f"Trước khi g.sort(reverse=True): {g}")
h = [9, 5, 6, 87, 19]
print(f"Trước khi h.sort(reverse=True): {h}")
g.sort(reverse=True)
h.sort(reverse=True)
print(f"Sau khi g.sort(reverse=True): {g}")
print(f"Sau khi h.sort(reverse=True): {h}\n")

# Nếu ta sài reverse=False thì sort sẽ sắp xếp theo thứ tự tăng dần (giống như sort mặc định)
g = ["a", "b", "c", "d", 'e', 'f', 'g', 'h']
print(f"Trước khi g.sort(reverse=False): {g}")
h = [9, 5, 6, 87, 19]
print(f"Trước khi h.sort(reverse=False): {h}")
g.sort(reverse=False)
h.sort(reverse=False)
print(f"Sau khi g.sort(reverse=False): {g}")
print(f"Sau khi h.sort(reverse=False): {h}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức REMOVE trong list
# Được dùng để loại bỏ 1 phần tử trong list
i = [1, 2, 3, [5, 6]]
print(f"Trước khi i.remove: {i}")
i.remove([5, 6])  # Xoá đi phần tử có giá trị là [5, 6]
# Nếu như ta xoá 1 phần tử không có trong list thì chương trình báo lỗi
print(f"Sau khi i.remove([5, 6]): {i}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức CLEAR trong list
j = [1, 2, 3, 4, 5, 6]
print(f"Trước khi j.clear: {j}")
j.clear()  # Xoá hết các phần tử trong list => không cần tham số nào truyền vào
# Không có giá trị nào trả về, clear chỉ làm sạch list
print(f"Sau khi j.clear(): {j}\n")  # => a là 1 list rỗng []

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức INDEX trong list
k = [1, 2, 3, 4, 5, 6]
print(f"Trước khi k.index: {k}")
k_after_index = k.index(3)  # Trả về phần tử nằm ở vị trí index nào trong list (tương tự như index của chuỗi)
# Nếu như không có số nào tồn tại trong list thì index sẽ báo lỗi
print(f"Sau khi k.index(3): {k_after_index}\n")
# Với index(3), tức là phần tử 3 nằm ở vị trí index 2 (index bắt đầu từ 0)

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức COUNT trong list
l = [1, 2, 1, 3, 4, 5, 6, 1]
print(f"Trước khi l.count: {l}")
l_after_count = l.count(1)  # Cho biết số lần xuất hiện của phần tử là bao nhiêu lần
# Nếu phần tử không có trong list thì count sẽ trả về kết quả = 0
print(f"Sau khi l.count(1): {l_after_count}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức COPPY trong list
m = [2, 3, 4, 5, 6, 7]
print(f"Bản gốc: {m}")
n = m.copy()  # Tạo ra 1 bản sao khác với bản gốc ban đầu (Có thể hiểu rằng copy() như 1 list constructor)
n[0] = "MINH"  # Thay đổi index vị trí 0 thành str
n[1] = 9.5  # Thay đổi index vị trí 1 thành 1 số
print(f"Bản sao m.copy(): {n}\n")

# ----------------------------------------------------------------------------------------------------------------------
# Phương thức EXTEND trong list
o = [1, 2, 3]
print(f"Trước khi o.extend: {o}")
o.extend([4, 5])  # Hoạt động trên các đối tương có thẻ lặp và nối thêm mọi mục trong lần lặp vào danh sách.
# Sử dụng toán tử (+) không tương đương với sử dụng phương thức extend.
print(f"Sau khi o.extend([4, 5]): {o}")
