import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama": entry_nama.get(),
        "Tanggal Lahir": entry_ttl.get(),
        "Asal Sekolah": entry_sekolah.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "Telepon": entry_telp.get(),
        "Alamat": text_alamat.get("1.0", "end").strip()
    }

    messagebox.showinfo("Data Tersimpan", "Data siswa berhasil disimpan!")
    print(data)  # bisa diganti simpan ke file

def hapus_data():
    entry_nama.delete(0, "end")
    entry_ttl.delete(0, "end")
    entry_sekolah.delete(0, "end")
    entry_nisn.delete(0, "end")
    entry_ayah.delete(0, "end")
    entry_ibu.delete(0, "end")
    entry_telp.delete(0, "end")
    text_alamat.delete("1.0", "end")

# WINDOW
root = tk.Tk()
root.title("MainWindow")
root.geometry("800x600")
root.configure(bg="#e6e6e6")

# HEADER
header = tk.Frame(root, bg="#b2f0f0", height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="DATA SISWA BARU",
    bg="#b2f0f0",
    font=("Arial", 18, "bold")
).pack(pady=18)

# FORM FRAME
form = tk.Frame(root, bg="#e6e6e6")
form.pack(padx=40, pady=20, fill="x")

def buat_label_entry(text, row, default=""):
    tk.Label(form, text=text, anchor="w", bg="#e6e6e6").grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(form, width=60)
    entry.grid(row=row, column=1, pady=5)
    entry.insert(0, default)
    return entry

entry_nama = buat_label_entry("Nama Lengkap", 0, "Siswa Baru")
entry_ttl = buat_label_entry("Tanggal Lahir", 1, "7 Juli 2007")
entry_sekolah = buat_label_entry("Asal Sekolah", 2, "SMP")
entry_nisn = buat_label_entry("NISN", 3, "12345")
entry_ayah = buat_label_entry("Nama Ayah", 4, "Ayah")
entry_ibu = buat_label_entry("Nama Ibu", 5, "Ibu")
entry_telp = buat_label_entry("Nomor Telepon / HP", 6, "987654321")

# ALAMAT
tk.Label(form, text="Alamat", bg="#e6e6e6").grid(row=7, column=0, sticky="nw", pady=5)
text_alamat = tk.Text(form, width=58, height=5)
text_alamat.grid(row=7, column=1, pady=5)
text_alamat.insert("1.0", "Rumah")

# FOOTER
footer = tk.Frame(root, bg="#8fd3d3", height=60)
footer.pack(fill="x", side="bottom")

btn_hapus = tk.Button(footer, text="Hapus", bg="#c96f4a", fg="white", width=10, command=hapus_data)
btn_hapus.pack(side="right", padx=20, pady=15)

btn_simpan = tk.Button(footer, text="Simpan", bg="#c96f4a", fg="white", width=10, command=simpan_data)
btn_simpan.pack(side="right", pady=15)

root.mainloop()
