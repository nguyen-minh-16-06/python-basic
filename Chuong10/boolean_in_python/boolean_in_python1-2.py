''' Toán tử is trong python '''
# Giúp ta hiểu sự khác nhau giữa toán tử == và is.
lst = [1, 2, 3]
lst_ = [1, 2, 3]
_lst = lst

# 2 biến chắc chắn sẽ bằng nhau (vì giá trị của nó bằng nhau):
print(lst == lst_)
# Nhưng chắc chắn rằng lst không phải là lst_ (có giá trị giống nhau nhưng không giống nhau):
print(lst is lst_)
print(_lst is lst)

# Từ đây sẽ có 1 kết luận rằng:
# Khi so sánh hai giá trị (đối tượng) bằng toán tử == thì Python sẽ so sánh bằng giá trị của chúng.
# Còn nếu so sánh bằng toán tử is thì Python sẽ lấy giá trị của hàm id để so sánh.
print(id(lst))
print(id(_lst))
print(id(lst_))

#LƯU Ý: 
# Không nên so sánh 2 số như thế này:
x = 699 is 699
print(x) # True

# Chỉ khác biệt khi:
a = 699
b = 699
print(a is b) # False

# Nhưng, một số trường hợp khác:
# Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20 
# thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.

# True
a = -5
b = -5
print(a is b)

# True
c = 256
d = 256
print(c is d)

# True
a = 'abc'
b = 'abc'
print(a is b)