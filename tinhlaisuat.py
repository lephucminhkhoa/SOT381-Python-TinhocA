von = 100_000_000      
lai_suat = 0.07       
print("Số tiền có được sau mỗi năm (lãi đơn):")
for nam in range(1, 6):     
    tong_tien = von + von * lai_suat * nam
    print(f"Năm {nam}: {tong_tien:,} VND")
