toan = float(input("Nhập điểm toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))
tongdiem_3mon = (toan + ly + hoa)
if tongdiem_3mon >= 15 and toan >= 4 and ly >= 4 and hoa >= 4:
    print("Đậu")
elif toan and ly and hoa >= 5:
    print("Học đều các môn")
else:
    print("Thi hỏng")

    

