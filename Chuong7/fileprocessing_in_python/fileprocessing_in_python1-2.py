''' Phương thức READ file trong Python '''

'''Syntax: <File>.read(size=-1)'''

  # Nếu size bị bỏ trống hoặc là một số âm.
  # Nó sẽ đọc hết nội dung của file đồng thời đưa con trỏ file tới cuối file.
  # Nếu không nó sẽ đọc tới n kí tự (với n = size) hoặc cho tới khi nội dung của file đã đọc xong.
# Sau khi đọc được nội dung, nó sẽ trả về dưới một dạng chuỗi.
# Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0.

# Vi du:
# Mở file và đọc file cho người dùng:
file = open('LE NGUYEN MINH.txt','r')
data = file.read()
print(data)
file.close() # Đọc xong thì đóng file.

# Nếu như muốn đọc lại thì ta lại tiếp tục open và cho đọc file.
file2 = open('LE NGUYEN MINH.txt')
data2 = file2.read()
print(data2)
file.close()