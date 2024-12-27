''' FILE '''

# Ta cũng có thể sử dụng hàm print như là phương thức write trong việc ghi file.

with open('MINH.txt', 'w') as f:
    print('MINH DEP ZAI VCL', file=f)