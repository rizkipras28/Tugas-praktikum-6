def hitung_nilai_akhir(nilai_tugas,nilai_uts,nilai_uas):
    return(nilai_tugas * 0.3)+(nilai_uts * 0.35)+(nilai_uas * 0.35)

#dictionery untuk menyimpan data mahasiswa
data_mahasiswa = {}

#variabel untuk nomor urut mahasiswa
nomor = 1

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("nama:")
    nim = input("nim:")
    nilai_tugas = float(input("nilai tugas:"))
    nilai_uts = float(input("nilai uts:"))
    nilai_uas = float(input("nilai uas:"))

    #hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, (nilai_uts), (nilai_uas))

    #simpan data ke dalam distionery
    data_mahasiswa[nim] = {
        'nama' : nama,
        'nilai_tugas' : nilai_tugas,
        'nilai_uts' : nilai_uts,
        'nilai_uas' : nilai_uas,
        'nilai_akhir' : round(nilai_akhir)
        }

    #menanyakan apakah ingin menambah data lagi
    tambah = input("tambah data (y/t)?")
    if tambah.lower()!='y':
        break

#menampilkan daftar mahasiswa
print("\nDaftar mahasiswa:")
print(f"{'no':<3} {'nama':<10} {'nim':<10} {'tugas':<6} {'uts':<6} {'uas':<6} {'akhir':<6}")
for i, (nim,info) in enumerate(data_mahasiswa.items(), start=1):
    print(f"{i:<3}{info['nama']:<10} {nim:<10} {info['nilai_tugas']:<6}"
          f"{info['nilai_uts']:<6} {info['nilai_uas']:<6} {info['nilai_akhir']:<6}")
    
