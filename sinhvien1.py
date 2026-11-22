# CHUONG TRINH QUAN LY SINH VIEN

sinh_vien = [
    {"ma": "SV01", "ten": "Nguyen Van A", "diem": 8.5},
    {"ma": "SV02", "ten": "Tran Thi B", "diem": 7.0},
    {"ma": "SV03", "ten": "Le Van C", "diem": 9.0}
]

def hien_thi():
    print("\nDANH SACH SINH VIEN")
    for sv in sinh_vien:
        print(sv["ma"], "-", sv["ten"], "-", sv["diem"])

def tim_sinh_vien(ma):
    for sv in sinh_vien:
        if sv["ma"] == ma:
            return sv
    return None

hien_thi()

ma = input("\nNhap ma sinh vien can tim: ")
ket_qua = tim_sinh_vien(ma)

if ket_qua:
    print("Tim thay:", ket_qua)
else:
    print("Khong tim thay sinh vien!")