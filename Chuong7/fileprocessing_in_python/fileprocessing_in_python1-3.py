# Đọc file bằng constructor nhận iterable:

file = open('LE NGUYEN MINH.txt')

# Sử dụng list hay tuple đều vẫn được:

datali = list(file)
#datatu = tuple(file)

file.close()
print(datali)