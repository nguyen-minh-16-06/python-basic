# Biểu thức điều kiện viết tắt một dòng cho câu lệnh if-else (toán tử ba ngôi)
#                        In hoặc gán một trong hai giá trị dựa trên một điều kiện
#                        X if condition else Y

num = 5
print("Positive" if num > 0 else "Negative")
print("EVEN" if num % 2 == 0 else "ODD")

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Số lớn nhất là {max_num} và số bé nhất là {min_num}")

age = 13
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 30
weather = "HOT" if temperature > 20 else "COLD"
print(weather)

user_role = "Admin"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)
