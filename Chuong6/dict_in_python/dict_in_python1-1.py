# Được giới hạn bởi cặp ngoặc nhọn {}
# Tất cả những gì nằm trong {} là những phần tử của Dict.
# Có hai phần tử và mỗi phần tử có hai thông số key : value
# Đó là 1: 'apple' và 2: 'ball'
dict = {1: 'apple', 2: 'ball'}
#Có 2 cách truy xuất vào phần tử:

a = dict[1] #truy xuất vào phần tử có key là 1
print(a)
print(dict.get(2)) #Đây cũng là 1 cách truy xuất vào phần tử có key là 2
''' Sự khác nhau giữa 2 cách kia là:
- Đối với truy xuất theo dict[key] sẽ trả về lỗi nếu như không có key tồn tại
- Đối với truy xuất theo get() sẽ trả về none nếu như không có key tồn tại '''

#LƯU Ý :
'''Các key có thể là một số tự nhiên (1,2,3,4,...)
hoặc một chuỗi được đặt trong ngoặc đơn hoặc ngoặc kép ('NGUYEN',"MINH") '''
