import tkinter as tk
from tkinter import ttk

BIAYA_PER_JAM = 2000
data_parkir = []

def hitung_biaya():
    try:
        plat = entry_plat.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())

        lama = keluar - masuk
        if lama < 0:
            biaya_label.config(text="0")
            return

        biaya = lama * BIAYA_PER_JAM
        biaya_label.config(text=str(biaya))

        data = (plat, masuk, keluar, biaya)
        data_parkir.append(data)

        tabel_keluar.insert("", "end", values=data)

        # sort untuk tabel bayar terbesar
        tabel_bayar.delete(*tabel_bayar.get_children())
        for d in sorted(data_parkir, key=lambda x: x[3], reverse=True):
            tabel_bayar.insert("", "end", values=d)

    except:
        biaya_label.config(text="0")

# WINDOW
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("900x500")

# TITLE
tk.Label(root, text="Aplikasi Parkir Kelompok 6", font=("Arial", 14, "bold")).place(x=20, y=10)

# INPUT
tk.Label(root, text="No Plat Polisi").place(x=20, y=50)
entry_plat = tk.Entry(root, width=25)
entry_plat.place(x=150, y=50)

tk.Label(root, text="Waktu Masuk").place(x=20, y=80)
entry_masuk = tk.Entry(root, width=25)
entry_masuk.place(x=150, y=80)

tk.Label(root, text="Waktu Keluar").place(x=20, y=110)
entry_keluar = tk.Entry(root, width=25)
entry_keluar.place(x=150, y=110)

tk.Label(root, text="Biaya").place(x=20, y=140)
biaya_label = tk.Label(root, text="0", width=22, anchor="w", relief="sunken")
biaya_label.place(x=150, y=140)

tk.Button(root, text="Hitung", command=hitung_biaya).place(x=150, y=170)

# BIAYA PER JAM
tk.Label(root, text="Biaya Per Jam", fg="red", font=("Arial", 14)).place(x=550, y=60)
tk.Label(root, text="Rp. 2.000", fg="red", font=("Arial", 28, "bold")).place(x=520, y=90)

# TABLE KELUAR TERAKHIR
tk.Label(root, text="List Pelanggan Urut Terakhir Keluar", fg="blue").place(x=20, y=220)
tabel_keluar = ttk.Treeview(root, columns=("plat","masuk","keluar","biaya"), show="headings", height=6)
for col in ("plat","masuk","keluar","biaya"):
    tabel_keluar.heading(col, text=col.title())
    tabel_keluar.column(col, width=100)
tabel_keluar.place(x=20, y=250)

# TABLE BAYAR TERBESAR
tk.Label(root, text="List Pelanggan Banyak Bayar", fg="blue").place(x=450, y=220)
tabel_bayar = ttk.Treeview(root, columns=("plat","masuk","keluar","biaya"), show="headings", height=6)
for col in ("plat","masuk","keluar","biaya"):
    tabel_bayar.heading(col, text=col.title())
    tabel_bayar.column(col, width=100)
tabel_bayar.place(x=450, y=250)

root.mainloop()
