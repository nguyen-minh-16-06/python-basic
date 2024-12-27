''' 
   Iterators trong Python 
						  '''
# iterators là những đối tượng (object) được hỗ trợ những tính năng lặp riêng biệt,
# Không cần phải sử dụng những vòng lặp thông thường như vòng lặp FOR hay vòng lặp WHILE.

'''
   list, tuple, string là những iterators  
										  '''
# Vì ta có thể sử dụng hàm iter() để tạo chúng thành 1 iterators
# Sau đó sử dụng hàm next() để lặp qua từng phần tử.

'''
    Về mặt kỹ thuật thì một iterator object phải implement 
    	từ hai phương thức __iter__() và __next__()
    		được gọi chung là iterator protocol.
    											'''
''' Để giúp lập trình viên sử dụng dễ dàng hơn thì hai build-in function ra đời
		đó là iter() và next(). 
							   '''