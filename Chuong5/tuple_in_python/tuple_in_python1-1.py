#KHÁI NIỆM VỀ TUPLE
''' Được giới hạn bởi cặp ngoặc ( )
    Các phần tử của tuple được phân cách nhau bởi dấu ','
    Tuple có khả năng chứa mọi giá trị
    Tốc độ truy xuất của tuple nhanh hơn list
    dung lượng chiếm trong bộ nhớ nhỏ hơn list
    bảo vệ dữ liệu cuủa bạn sẽ không bị thay đổi
    có thể dùng làm key của dictionary'''
#Bản chất của tuple cũng là 1 container cũng được sử dụng rất nhiều trong
#các chương trình python

tup = (1,2,(3,4,5),'Minh') #Có thể vừa chứa nhiều kiểu dữ liệu
#như int hoặc chuỗi mà list không làm được
#Có thể tự chứa chính nó trong bên trong nó
print(tup)