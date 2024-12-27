# Indexing và cắt tuple
'''Giống như trong chuỗi'''

tup = (1,5,9)
a = tup[0] #Lưu ý truy xuất index ta vẫn dùng ngoặc vuông không sài ngoặc tròn
print(a)
#Lấy độ dài trong tuple
b = len(tup) #Có 3 phần tử trong 1 tuple
c = tup[-1] #Truy xuất tới phần tử cuối của tuple
# Hoặc ta có thể sài tup[len(tup)-1]
d = tup[::-1] #Đảo ngược tuple
s = tup[:-1] #Lấy phần tử thứ bao nhiêu đến bao nhiêu
print(b)
print(c)
print(d)
print(s)