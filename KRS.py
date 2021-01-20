input("=== Iqbal Ibrahim ===")
input("=== 0110120081 ===")
input("=== Tugas 1 DDP ===")
print()

# SOAL PERTAMA #

print("Fitur pengisian rencana studi")
nim = int(input("Masukkan NIM : "))
nim = str(nim)
banyak_data = len(nim)

if banyak_data == 9:
    tahun = nim[4:6]
    if tahun == "20":
        generasi    = "tahun pertama"
        max_sks     = 20

 elif tahun == "19":
        generasi    = "tahun kedua"
        max_sks     = 22

 elif tahun == "18":
        generasi    = "tahun ketiga"
        max_sks     = 24

 elif tahun == "17":
        generasi    = "tahun keempat"
        max_sks     = 26

  else:
        print("NIM TIDAK TERDAFTAR")
        exit()
    jumlah_sks = 0;
    print("Anda mahasiswa " + generasi + ". Anda bisa mengambil paling banyak " ,max_sks, " SKS")
    status = "y"
    while status == "y":
        print()
        print("Jumlah SKS yang diambil" , jumlah_sks)
        matkul = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai : ")
        if matkul == "x" or matkul == "X":
            status = "x"
        else:
            matkul_sks = int(input("Masukkan beban SKS mata kuliah tersebut : "))
            jumlah_sks += matkul_sks
            if jumlah_sks > max_sks:
                print("Jumlah SKS melebihi SKS maksimal. Pengisian rencana studi selesai.")
                status = "x"
            else:
                print("Berhasil mengambil mata kuliah " + matkul + " dengan bobot ", matkul_sks)
                
            
elif banyak_data > 9:
    print("NIM LEBIH DARI 10 KARAKTER")
    exit()
else:
    print("NIM KURANG DARI 10 KARAKTER")
    exit()