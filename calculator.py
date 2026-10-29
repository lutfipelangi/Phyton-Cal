import tkinter as tk

# --- Fungsi-fungsi Logika ---
def tombol_klik(item):
    # Lebih efisien: langsung tambahkan ke akhir layar
    layar.insert(tk.END, str(item))

def tombol_clear():
    layar.delete(0, tk.END)

def tombol_sama_dengan():
    try:
        hasil = str(eval(layar.get()))
        layar.delete(0, tk.END)
        layar.insert(0, hasil)
    except ZeroDivisionError:
        layar.delete(0, tk.END)
        layar.insert(0, "Error (Bagi 0)")
    except Exception:
        layar.delete(0, tk.END)
        layar.insert(0, "Error")

# --- Membuat Jendela Utama ---
root = tk.Tk()
root.title("Calculator Maspel")
root.geometry("320x450")
root.resizable(False, False)

# PERBAIKAN 1: Konfigurasi grid agar tombol membesar memenuhi layar
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# --- Membuat Layar Display ---
layar = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, justify="right")
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

# --- Daftar Tombol ---
tombol_list = [
    ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2)
]

# --- Membuat dan Menempatkan Tombol ---
for (teks, baris, kolom) in tombol_list:
    if teks == 'C':
        cmd = tombol_clear
    elif teks == '=':
        cmd = tombol_sama_dengan
    else:
        cmd = lambda x=teks: tombol_klik(x)
    
    # PERBAIKAN 2: Menambahkan sticky="nsew" agar tombol mengisi seluruh kotak grid
    tk.Button(root, text=teks, font=("Arial", 14), command=cmd).grid(row=baris, column=kolom, padx=2, pady=2, sticky="nsew")

# --- Menambahkan Nama Pembuat dan Versi di Bagian Bawah ---
footer_label = tk.Label(root, text="Dibuat oleh: Maspel | Versi 1.0", font=("Arial", 9, "italic"), fg="gray")
footer_label.grid(row=6, column=0, columnspan=4, pady=5)

# PERBAIKAN 3: Memaksa jendela kalkulator langsung aktif saat dibuka
root.focus_force()
layar.focus_set()

# Menjalankan aplikasi
root.mainloop()