# Format specifiers = {value:flags} format a value based on what flags are inserted
# Công cụ xác định định dạng = {value:flags} định dạng một giá trị dựa trên những cờ được chèn vào

# 01. {value:.(number)f} = round to that many decimal places (fixed point)
#                          làm tròn đến số thập phân gần nhất (1 điểm cố định)
a = 3.14159
b = -987.658
c = 12.34

print(f"01. a sau khi định dạng là: {a:.3f}")
print(f"01. b sau khi định dạng là: {b:.2f}")
print(f"01. c sau khi định dạng là: {c:.1f}")
print("-----------------------------------")

# 02. {value:(number)} = allocate that many spaces
#                        phân bổ khoảng trắng
print(f"02. a sau khi định dạng là: {a:10}")
print(f"02. b sau khi định dạng là: {b:10}")
print(f"02. c sau khi định dạng là: {c:10}")
print("-----------------------------------")

# 03. {value:03} = allocate and zero pad that many spaces
#                  Phẩn bổ 0 vào những khoảng trắng
print(f"03. a sau khi định dạng là: {a:010}")
print(f"03. b sau khi định dạng là: {b:010}")
print(f"03. c sau khi định dạng là: {c:010}")
print("-----------------------------------")

# 04. {value:<} = left justify
#                 căn chỉnh trái
print(f"04. a sau khi định dạng là: {a:<10}")
print(f"04. b sau khi định dạng là: {b:<10}")
print(f"04. c sau khi định dạng là: {c:<10}")
print("-----------------------------------")

# 05. {value:>} = right justify
#                 căn chỉnh phải
print(f"05. a sau khi định dạng là: {a:>10}")
print(f"05. b sau khi định dạng là: {b:>10}")
print(f"05. c sau khi định dạng là: {c:>10}")
print("-----------------------------------")

# 06. {value:^} = center align
#                 căn giữa
print(f"06. a sau khi định dạng là: {a:^10}")
print(f"06. b sau khi định dạng là: {b:^10}")
print(f"06. c sau khi định dạng là: {c:^10}")
print("-----------------------------------")

# 07. {value:+} = use a plus sign to indicate positive value
#                 sử dụng dấu cộng để biểu thị giá trị dương
print(f"07. a sau khi định dạng là: {a:+}")
print(f"07. b sau khi định dạng là: {b:+}")
print(f"07. c sau khi định dạng là: {c:+}")
print("-----------------------------------")

# 08. {value:=} = place sign to leftmost position
#                 đặt dấu hiệu vào vị trí ngoài cùng bên trái
print(f"08. a sau khi định dạng là: {a:=}")
print(f"08. b sau khi định dạng là: {b:=}")
print(f"08. c sau khi định dạng là: {c:=}")
print("-----------------------------------")

# 09. {value: } = insert a space before positive numbers
#                 chèn khoảng trắng trước số dương
print(f"09. a sau khi định dạng là: {a: }")
print(f"09. b sau khi định dạng là: {b: }")
print(f"09. c sau khi định dạng là: {c: }")
print("-----------------------------------")

# 10. {value:,} = comma separator
#                 dấu phẩy phân cách
a = 3000.14159
b = -9870.658
c = 1200.34
print(f"10. a sau khi định dạng là: {a:,}")
print(f"10. b sau khi định dạng là: {b:,}")
print(f"10. c sau khi định dạng là: {c:,}")
print("-----------------------------------")

# 11. {value:+,.2f} = combine all format
#                     Kết hợp toàn bộ định dạng
print(f"11. a sau khi định dạng là: {a:+,.2f}")
print(f"11. b sau khi định dạng là: {b:+,.2f}")
print(f"11. c sau khi định dạng là: {c:+,.2f}")
