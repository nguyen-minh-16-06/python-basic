""" RETURN TRONG PYTHON """
# SYNTAX: return [object]
""" 
    object là một đối tượng bất kì 
    - có thể là số (number)
    - chuỗi (string)
    - list, tuple, hàm (sẽ biết rõ hơn khi tìm hiểu decorator), 
    - thậm chí là bỏ trống – trường hợp bỏ trống thì object return về được tính là None.
                                                                                        """
"""     USE:
    - Khi return được gọi, hàm được kết thúc và kết quả được trả ra ngoài.
    - Kết quả trả ra ngoài nên được đưa cho một biến nào đó hứng.
    - Nếu không có thì coi như bạn gọi hàm không để làm gì.                                                                                          
                                                            """
def cal_rec_per(width, height):
    per = (width + height) * 2
    return per

rec_1_width = 5
rec_1_height = 3

# khởi tạo một biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)

# Trường hợp này in ra giá trị của hàm cal_rec_per với args là width = 7 và height = 4.
print(cal_rec_per(7, 4))
