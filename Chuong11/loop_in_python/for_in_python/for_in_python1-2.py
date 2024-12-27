''' Hàm RANGE trong vòng lặp for '''
'''
    Hàm range sẽ trả về một mảng trong đó tổng số phần tử sẽ phụ thuộc vào các tham số truyền vào.
       syntax : range(start, end, step)
            start: là giá trị bắt đầu
            end: là giá trị kết thúc
            step: là khoảng cách giữa các phần tử, hay còn gọi là bước nhảy
'''

''' Trường hợp có 1 tham số: '''
# Nếu bạn chỉ truyền một tham số n thì nó sẽ tạo một mảng từ 0 -> (n - 1).
# Mã giả:
# i = 0 (1)
# i = 1 (2)
# i = 2 (3)
# i = 3 (4)
# i = 4 (5)
for i in range(5):
    print(i, end=' ')
else:
    print("")

''' Trường hợp có 2 tham số: '''
# Nếu bạn truyền 2 tham số thì sẽ tạo một mảng với bước nhảy là 1 phần tử đầu của mảng là start, phần tử cuối cùng của mảng là (end - 1).
# Mã giả:
# i = 5 Nếu start là 5 thì sẽ bắt đầu từ 5
# i = 6
# i = 7
# i = 8
# i = 9 Nếu end là 10 thì sẽ kết thúc tại 9
for i in range(5, 10):
    print(i, end=' ')
else:
    print("")

''' Trường hợp có 3 tham số: '''
# Trường hợp này sẽ tạo một mảng như trường hợp 2, nhưng vì bước nhảy là 2 nên sẽ bỏ qua 1 phần tử.
# Mã giả:
# i = 1, step 2 thì nhảy sang 3
# i = 3, step 2 thì nhảy sang 5
# i = 5, step 2 thì nhảy sang 7
# i = 7, step 2 thì nhảy sang 9
# i = 9, là số cuối cùng nên không thực hiện bước nhảy nữa.
for i in range(1, 10, 2):
    print(i, end=' ')
else:
    print("")
