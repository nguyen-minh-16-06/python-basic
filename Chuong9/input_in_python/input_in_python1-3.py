''' END '''

# Có thể nhận ra rằng sau mỗi lần print thì chương trình sẽ tự xuống dòng.
# Đấy là nhờ paramater end. Nó sẽ thêm 1 kí tự newline (\n)

print('line 1')
print('line 2')

# Tuy nhiên khi chỉ định đối số end bằng một ký tự, 
# thì ký tự này sẽ thay thế cho việc xuống dòng và nối các đối tượng in ra màn hình lại. 
# Khi đó, chúng ta có thể thực hiện in không xuống dòng trong python.
# Và ta có thể thay đổi giá trị của paramater này bằng cách: 

print('a line without newline', end = ' ')