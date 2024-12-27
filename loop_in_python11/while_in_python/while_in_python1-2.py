# Break, continue trong vòng lặp:

''' BREAK '''
# Dùng để kết thúc vòng lặp.
# Cứ nằm trong block của vòng lặp nào thì nó sẽ kết thúc ngay khi chạy câu lệnh này.
# Ví dụ như trong T.HỢP block a chứa block b, trong vòng lặp b chạy câu lệnh break thì
# chỉ kết thúc vòng lặp b mà thôi, vòng lặp a thì không.

fen = []
k_number = 1
while True: # vòng lặp vô hạn vì giá trị True này là hằng nên ta không thể tác động được
	if k_number % 2 == 0: # nếu k_number là một số chẵn
		fen.append(k_number) # thêm giá trị của k_number vào list
	if len(fen) == 5: # nếu list này đủ 5 phần tử
		break # thì kết thúc vòng lặp
	k_number += 1
print(k_number)
print(fen)

''' CONTINUE '''
# Câu lệnh này sẽ chạy tiếp vòng lặp.
# Khi sử dụng statement này nó sẽ không quan tâm những thằng bên dưới.

k_number = 0
while k_number < 10:
	k_number += 1 # tăng một đơn vị cho k_number và tiếp tục vòng lặp
	if k_number % 2 == 0: # nếu k_number là số chẵn
		continue # k = 1 không % 2 = 0 thì sẽ kh chạy tiếp continue và chạy xuống câu lệnh phía dưới
		# => 1 is odd number.
	print(k_number, 'is odd number')
print(k_number)