#DAFTAR KONTAK
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=============")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

#TAMBAH DATA
def tambah_kontak():
    nama = input("Nama :")
    email = input("Email :")
    telepon = input("Telepon :")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

#HAPUS DATA
def hapus_kontak(daftar_kontak):
    telepon = input("no telp yang akan dihapus : ")
    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("dataa tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("BERHASIL MENGHAPUS DATA KONTAK")

#CARI DATA
def cari_kontak(daftar_kontak):
    cari = input("Nama yang dicari :")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(cari.lower()) != -1:
            print("=============")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")