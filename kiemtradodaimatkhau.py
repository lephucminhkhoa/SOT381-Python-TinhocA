n = input(" Nhập mật khẩu cần kiểm tra: ")
if len(n) >= 8:
    print(n, " Độ dài mật khẩu trên 8 kí tự ")
else:
    print(n, " Độ dài mật khẩu dưới 8 kí tự ")