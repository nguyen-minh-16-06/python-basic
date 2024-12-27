'''CÁC PHƯƠNG THỨC LIST TRONG PYTHON'''

#Phương thức REVERSE trong list
a = [1,2,3,4]
print(f'đây là a trước khi xài hàm REVERSE: {a}')
a.reverse() #Ra một list đảo ngược lại
print(f'đây là a sau khi xài hàm REVERSE: {a}')

#Phương thức SORT trong list
b = [9,1,2,3]
print(f'đây là b trước khi xài hàm SORT: {b}')
b.sort() #Sắp xếp 1 list theo thứ tự tăng dần
print(f'đây là b sau khi xài hàm REVERSE: {b}')

#Sắp xếp các phần tử của LIST theo thứ tự giảm dần
c = ['a','b','c','d','e','f','g']
d = [9,5,6,87,19]
#Nếu ta sài REVERSE=True thì sort sẽ sắp xếp theo thứ tự giảm dần
#Nếu ta sài REVERSE=False thì sort sẽ sắp xếp theo thứ tự tăng dần
c.sort(reverse=True)
d.sort(reverse=True)
print(c)
print(d)