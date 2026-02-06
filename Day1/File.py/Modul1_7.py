print("Program Perhitungan Gaji Karyawan")

# Input
nama = input("Masukkan nama karyawan: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Proses perhitungan
tunjangan = 20 / 100 * gaji_pokok
pajak = 15 / 100 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print("\n=== Rincian Gaji ===")
print("Nama           :", nama)
print("Gaji Pokok     : Rp", gaji_pokok)
print("Tunjangan      : Rp", tunjangan)
print("Pajak          : Rp", pajak)
print("Gaji Bersih    : Rp", gaji_bersih)

print("\nProgram selesai")
