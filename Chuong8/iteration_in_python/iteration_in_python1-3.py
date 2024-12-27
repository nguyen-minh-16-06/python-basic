'''
   Lặp chuỗi(str) bằng Iterators trong Python
   											          '''
# Chuỗi
domain = "freetuts.net"
 
# Chuyển thành Iterator
idomain = iter(domain)
 
# Lấy ký tự đầu tiên
print(next(idomain))
 
# Lấy ký tự thứ 2
print(next(idomain))