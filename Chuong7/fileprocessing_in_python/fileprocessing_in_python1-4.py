''' Phương thức WRITE xử lý file trong python '''
'''
	Syntax:
			<File>.write(text)
							   '''
# Phương thức này sẽ trả về số kí tự mà chúng ta ghi vào.

file = open('LE NGUYEN MINH.txt', 'a+')
data = file.write('\nToi wa dep zai')
file.close()
print(data)
