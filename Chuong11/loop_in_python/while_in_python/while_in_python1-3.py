# Vòng lặp while-else và cách hoạt động:

# Trường hợp đặc biệt:
# Khi sài câu lệnh break trong while thì else sẽ không được thực hiện.
k = 0
while k < 3:
	print('Value of k is', k)
	k += 1
	if k == 1:
		break
else:
	print('k is not less than 3 anymore')
