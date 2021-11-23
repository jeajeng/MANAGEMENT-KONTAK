#program management kontak
import function2
#list dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "yuhu",
    "email" : "yuhu@gmail.com",
    "telepon" : "083245678"
})
#menu program 
while True:
    print("MENU")
    print("1. Daftar kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function2.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function2.tambah_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function2.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function2.cari_kontak(daftar_kontak)
    else:
        print("menu tidak ditemukan")

print("PROGRAM SELESAI BERJALAN, SAMPAI JUMPA")        

