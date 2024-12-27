''' GLOBAL <Variable> '''
# Có thể tạo ra các biến toàn cục để tái sử dụng lại.
# Hoặc là khởi tạo chương trình.

def slogan():
    # khởi tạo với global không có giá trị nhé.
    global minh
    # Sau khi khởi tạo xong, ta mới gán giá trị.
    minh = 'dzai'

# Phải chạy hàm trước khi print hàm.
slogan() # Bởi vì khi chạy qua hàm slogan thì global đã tạo ra 1 biến minh mới để sài lại được.
print(minh)