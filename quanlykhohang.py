so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
print("Các sản phẩm cần nhập thêm (số lượng < 10):")
for n in range(len(so_luong)):
    if so_luong[n] < 10:
        print(f"- {ten_san_pham[n]}: {so_luong[n]} chiếc")
