''' LƯU Ý: TRƯỜNG HỢP TÊN BIẾN LOCAL TRÙNG VỚI TÊN BIẾN GLOBAL '''
# Tuy nhiên 2 biến x này hoàn toàn khác nhau:
def make_global():
    global x
    x = 1 # Biến x trong hàm global trùng với biến x trong hàm local
          # Biến x global thì cũng có một giá trị riêng và một địa chỉ riêng.

def local():
    x = 5 # Biến x trong hàm local trùng với biến x trong hàm global.
          # Còn biến x dùng trong hàm local thì có một địa chỉ riêng và một giá trị riêng.
    print('x in local', x)

make_global() 
print(x) # Đây là biến x nằm trong global.

local()  # Đây là gọi các câu lệnh bên trong hàm local.

print(x) # Nếu như ta sử dụng biến x ở ngoài hàm thì Python sẽ tìm tới biến x của global.
         # Chứ không phải biến x của local.