import time

my_time = int(input("Nhập thời gian: "))

for i in range(my_time, 0, -1):
    second = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("TIME'S UP!")
