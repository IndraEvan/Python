import math

class shape:
    def hitung_luas(self):
        pass

class square(shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2
    
class triangle(shape):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
    
if __name__ == "__main__":
    bentuk1 = square(5)
    bentuk2 = circle(3)
    bentuk3 = triangle(4, 6)

    daftar_bentuk = [bentuk1, bentuk2, bentuk3]

    for bentuk in daftar_bentuk:
        luas = bentuk.hitung_luas()
        if isinstance(bentuk, square):
            print(f"Luas persegi: {luas}")
        elif isinstance(bentuk, circle):
            print(f"Luas Lingkaran: {luas}")
        elif isinstance(bentuk, triangle):
            print(f"Luas Segitiga: {luas}")