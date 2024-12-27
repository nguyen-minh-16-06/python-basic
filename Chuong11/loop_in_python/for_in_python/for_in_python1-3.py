# Kết hợp hàm len để in ra các phần tử của mảng dựa vào chỉ số index.

fruits = ["banana", "apple", "mango"]
for i in range(len(fruits)):
    print("Current fruit :", fruits[i])

'''
     Kết hợp với else xử lý lần lặp bị từ chối đầu tiên
         , tức là kết thúc vòng lặp thì chạy lệnh trong else.
                                                              '''

for i in range(5):
    print(i, end = " ")
else:
    print("\nGiá trị cuối cùng của i là: ", i)
