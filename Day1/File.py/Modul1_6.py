print("Program Cek Ketuntasan Nilai Siswa")

while True:
    nilai_siswa = int(input("Masukkan nilai siswa: "))

    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        ulang = input("Nilai belum tuntas. Input ulang? (Ya/Tidak): ")

        if ulang.lower() == "ya":
            continue
        else:
            print("Tidak Tuntas")
            break

print("Program selesai")
