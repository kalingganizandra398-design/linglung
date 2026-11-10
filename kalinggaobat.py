daftar_nama_obat = [
    "Paracetamol", "Amoxicillin", "Ibuprofen", "Metformin", "Amlodipine",
    "Omeprazole", "Cetirizine", "Asam Mefenamat", "Vitamin C", "Antasida"
]

database_obat = []
TAHUN_SEKARANG = 2026

print("=== INPUT DETAIL DATA OBAT ===")
for nama in daftar_nama_obat:
    print(f"\n--- Input untuk Obat: {nama} ---")
    stok = int(input(f"Masukkan Stok {nama}: "))
    harga = float(input(f"Masukkan Harga {nama} (Rp): "))
    exp_year = int(input(f"Masukkan Tahun Kadaluarsa {nama} (YYYY): "))
    
    database_obat.append({
        "nama": nama,
        "stok": stok,
        "harga": harga,
        "exp_year": exp_year
    })

print("\n\n=== LAPORAN MANAGEMENT OBAT APOTEK ===")
for obat in database_obat:
    print(f"\nObat: {obat['nama']}")
    
    # 1. Pengecekan Masa Berlaku
    if obat['exp_year'] <= TAHUN_SEKARANG:
        print("-> Status Keamanan: [BAHAYA] Obat sudah kadaluarsa! Segera buang.")
    else:
        print("-> Status Keamanan: [AMAN] Obat layak dikonsumsi.")
        
    # 2. Pengecekan Stok
    if obat['stok'] == 0:
        print("-> Status Logistik: [KOSONG] Silahkan lakukan restock segera.")
    elif obat['stok'] < 10:
        print(f"-> Status Logistik: [KRITIS] Stok menipis (Sisa {obat['stok']}).")
    else:
        print(f"-> Status Logistik: [NORMAL] Stok mencukupi ({obat['stok']} unit).")
        
    # 3. Klasifikasi Harga
    if obat['harga'] > 15000:
        print("-> Klasifikasi Harga: Obat Kelas Premium/Mahal.")
    else:
        print("-> Klasifikasi Harga: Obat Kelas Reguler/Ekonomis.")
