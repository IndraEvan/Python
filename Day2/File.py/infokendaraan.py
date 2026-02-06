class vehicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f"Merk: {self.merk}")
        print(f"tahun: {self.tahun}")
        print(f"warna: {self.warna}")


class car(vehicle):
    def __init__(self, merk, tahun, warna, model):
        super().__init__(merk, tahun, warna)
        self.model = model

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Model: {self.model}")

if __name__ == "__main__":
    car = car("Toyota", 2022, "Merah", "Camry")

    print("Info Kendaraan:")
    car.tampilkan_info()