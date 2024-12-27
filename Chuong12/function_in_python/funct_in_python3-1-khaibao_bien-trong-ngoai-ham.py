''' BIẾN CỤC BỘ VÀ BIẾN TOÀN CỤC '''

# KHAI BÁO BIẾN Ở NGOÀI HÀM.
minh = 'NMINH'
def introduce():
    print("My name is", minh)
introduce()

# KHAI BÁO BIẾN Ở TRONG HÀM VÀ SỬ DỤNG HÀM.
# Việc khai báo biến ở trong 1 hàm, thì có nghĩa là biến đó chỉ đc sử dụng trong hàm đó thôi.
# Nếu ra ngoài hàm thì biến đc khai báo bên trong không có tác dụng nữa.
def introduce():
    minhz = 'NMINH'
    print("My name is", minhz)
introduce()
# print(minhz) - Chương trình sẽ báo lỗi vì chưa được khởi tạo và khai báo.
#              - Bởi vì chỉ khai báo biến minhz trong hàm thôi, chỉ có hàm đó mới nhận diện đc minhz.
#              - Còn nếu đưa ra ngoài thì chương trình chả biết đấy là biến nào cả.
# LƯU Ý: BIẾN KHAI BÁO Ở HÀM NÀO, THÌ CHỈ HÀM ĐÓ BIẾT THÔI, CÒN HÀM KHÁC THÌ KHÔNG BIẾT.
