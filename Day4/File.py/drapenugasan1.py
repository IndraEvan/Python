import tkinter as tk

def hitung_total():
    try:
        harga = float(entry_harga.get())
        qty = float(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        label_total.config(text="Total: Rp.0.00")

# Window
root = tk.Tk()
root.title("Hitung Total")
root.geometry("300x220")

# Harga
tk.Label(root, text="Harga:").pack(pady=(15, 0))
entry_harga = tk.Entry(root, width=25)
entry_harga.pack()

# Kuantitas
tk.Label(root, text="Kuantitas:").pack(pady=(10, 0))
entry_qty = tk.Entry(root, width=25)
entry_qty.pack()

# Button
tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=15)

# Total
label_total = tk.Label(root, text="Total: Rp.0.00", font=("Arial", 11))
label_total.pack()

root.mainloop()
