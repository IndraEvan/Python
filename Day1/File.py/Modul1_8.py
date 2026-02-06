print("Program Penentuan Kategori Umur")

# Input umur
umur = int(input("Masukkan umur: "))

# Proses penentuan kategori
if umur <= 10:
    kategori = "Anak-anak"
elif umur <= 18:
    kategori = "Remaja"
elif umur <= 35:
    kategori = "Dewasa"
elif umur <= 65:
    kategori = "Parubaya"
else:
    kategori = "Tua"

# Output
print("Kategori umur:", kategori)
print("Program selesai")
