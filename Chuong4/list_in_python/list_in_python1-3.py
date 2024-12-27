#Một số toán tử về list
a = [1,2]
a +=['one','two'] # (a +=) là viết tắt của (a = a +)
print (a)

#NOTE :
''' 1 list CỘNG với list thì ĐƯỢC  
1 chuỗi CỘNG với list thì KHÔNG ĐƯỢC '''

''' VD về toán tử CỘNG '''
# a = 'MINH'
# a = a +['one','two']
# => KHÔNG PHẢI 1 tập hợp là đều cộng với nhau được

''' VD về toán tử NHÂN '''
b = [1,2]
b *=2 #CÓ THỂ nhân list lên nhiều lần nhưng KHÔNG THỂ nhân 2 list với nhau
#nhân list với 1 số nào đó để nó nhân nó lên 'n' lần
print(b)

''' VD về toán tử in '''
c = [1,2]
d = 1 in c #kiểm tra 1 có nằm bên trong a hay không, nếu có => TRUE và ngược lại
print(d)
