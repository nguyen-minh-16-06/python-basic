# While loop = excute some code WHILE some condition remains TRUE

# While nên được sử dụng trong trường hợp người dùng nhập sai liên tục và cho họ nhập lại đến khi đúng để thoát ra khỏi vòng lặp

# VD 1:
name = input("Nhập tên của bạn: ")

while name == "":
    print("Bạn chưa nhập tên của mình!")
    # If haven't this input (Nếu không có lệnh nhập này), we will be stuck (chúng ta sẽ bị mắc kẹt) in an infinite loop (vòng lặp vô hạn),
    # we can't actually (chúng ta thực sự không thể) escape (thoát khỏi) this Loop (vòng lặp này)
    # we didn't give (chúng ta không đưa ra) ourselves an exit (cho chính chúng ta 1 lối thoát).
    name = input("Nhập tên của bạn: ")
print(f"Chào {name} nhá, chúc {name} 1 ngày thật vui vẻ !")

# VD 2:
age = int(input("Nhập tuổi của bạn: "))

while age < 0:
    print("Tuổi không xác định !")
    age = int(input("Nhập tuổi của bạn: "))
print(f"Hiện bạn đang {age} tuổi")

# VD 3:
food = input("Vui lòng nhập món ăn bạn thích (q để thoát): ")

while not food == "q":
    print(f"Bạn thích món {food}")
    food = input("Nhập món ăn khác mà bạn thích (q để thoát): ")
print("Hẹn gặp lại bạn !")

# VD 4:
num = int(input("Nhập 1 con số từ 1-10: "))

while num < 1 or num > 10:
    print(f"Số {num} is not valid (Không hợp lệ)")
    num = int(input("Vui lòng nhập 1 con số từ 1-10: "))
print(f"Con số {num} thật đẹp quá đi !!")
