''' FLUSH '''
# Giá trị mặc định giá trị là False.
# Liên quan khá nhiều đến parameter end.

# Nhập hàm sleep từ thư viện time
from time import sleep

print('start...', end='', flush=True)
# Dừng chương trình 3 giây
# Đó là nhờ parameter flush. 
# Nếu là True, nó sẽ yêu cầu bộ đệm xuất những gì có trong bộ đệm ra.
sleep(0.5)
print('end...')