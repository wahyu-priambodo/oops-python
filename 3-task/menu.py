# TUGAS OOP 3
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# File: menu.py

from mobil import list_semua_mobil # import variable list_semua_mobil dari file mobil.py
from dealer import Dealer # import class Dealer dari file dealer.py
from customer import Customer # import class Customer dari file customer.py
from collections import defaultdict # import defaultdict untuk mengelompokkan mobil berdasarkan merek dan tipe

# Class Menu untuk menampilkan dan menjalankan menu yang dipilih user
class AppMenu:
  # method untuk menampilkan menu
  def tampilkan_menu():
    print("==== TUNAS TOYOTA BEKASI ====")
    print("1. Tampilkan Semua Mobil\n"
          "2. Tambah Mobil\n"
          "3. Cari Mobil (lihat list semua mobil di opsi 1)\n"
          "4. Ubah Mobil\n"
          "5. Hapus Mobil\n"
          "6. Ajukan Kredit\n"
          "7. Beli Mobil\n"
          "8. Keluar\n")
  
  # method untuk menampilkan list semua mobil
  def menu1():
    print('\n==== LIST SEMUA MOBIL ====')
    # Membuat dictionary untuk mengelompokkan mobil berdasarkan merek dan tipe
    dict_mobil = defaultdict(dict)

    # Mengelompokkan mobil berdasarkan merek dan tipe
    for mobil in list_semua_mobil:
      merek = mobil.nama_mobil
      tipe = mobil.tipe_mobil
      model_mobil = mobil.model_mobil
      harga_mobil = mobil.harga_mobil
      premium_color = mobil.premium_color
      two_tone_color = mobil.two_tone_color

      # Jika merek mobil belum ada di dict_mobil, maka buat key merek dan value berupa dictionary kosong
      if merek not in dict_mobil:
        dict_mobil[merek] = {}
      # Jika merek mobil sudah ada di dict_mobil, maka buat key tipe dan value berupa list kosong
      if dict_mobil[merek].get(tipe):
        dict_mobil[merek][tipe].append((model_mobil, harga_mobil, premium_color, two_tone_color))
      # Jika tipe mobil belum ada di dict_mobil[merek], maka buat key tipe dan value berupa list kosong
      else:
        dict_mobil[merek][tipe] = [(model_mobil, harga_mobil, premium_color, two_tone_color)]

    # Mencetak mobil berdasarkan kelompok
    for merek, tipe_mobil in dict_mobil.items():
      print('-'*35)
      print(merek)
      for tipe, models in tipe_mobil.items():
        print(f"Tipe mobil: {tipe}")
        for model, harga, premium_color, two_tone_color in models:
          print(f"- {model}: Rp{harga:,}")
        # jika ada harga tambahan, maka tampilkan harga tambahan
        if premium_color != 0: # untuk premium colour
          print(f"*) Premium colour + Rp{premium_color:,}")
        if two_tone_color != 0: # untuk two tone colour
          print(f"*) Two tone colour + Rp{two_tone_color:,}")
        print('-'*35)
    
    print() # baris baru untuk memisahkan menu dengan list semua mobil
  
  # method untuk menambahkan mobil bobil ke dalam list_semua_mobil
  def menu2():
    print('\n==== CREATE/TAMBAH DATA MOBIL ====')
    nama_mobil = input("Masukkan nama mobil: ")
    tipe_mobil = input("Masukkan tipe mobil: ")
    model_mobil = input("Masukkan model mobil: ")
    harga_mobil = int(input("Masukkan harga mobil: "))
    premium_color = int(input("Masukkan harga premium color (ketik 0 jika tidak ada): "))
    two_tone_color = int(input("Masukkan harga two tone color (ketik 0 jika tidak ada): "))
    dealer = Dealer(tambah_mobil=True)
    dealer.create_mobil(nama_mobil.upper(), tipe_mobil.upper(), model_mobil.upper(), harga_mobil, premium_color, two_tone_color)
  
  # method untuk menampilkan mobil yang dicari
  def menu3():
    print('\n==== READ/LIHAT DATA MOBIL ====')
    dealer = Dealer(lihat_mobil=True)
    nama_mobil_yang_dicari = input("Masukkan nama mobil yang dicari: ")
    model_mobil_yang_dicari = input("Masukkan model mobil yang dicari: ")
    dealer.read_mobil(nama_mobil_yang_dicari, model_mobil_yang_dicari)
  
  # method untuk mengubah data model_mobil dan harga_mobil yang ada di dalam list_semua_mobil
  def menu4():
    print('\n==== UPDATE/UBAH DATA MOBIL ====')
    dealer = Dealer(ubah_mobil=True)
    nama_mobil_yang_dicari = input("Masukkan nama mobil yang ingin diubah: ")
    model_mobil_yang_dicari = input("Masukkan model mobil yang ingin diubah: ")
    dealer.update_mobil(nama_mobil_yang_dicari, model_mobil_yang_dicari)
  
  # method untuk menghapus data mobil yang ada di dalam list_semua_mobil
  def menu5():
    print('\n==== DELETE/HAPUS DATA MOBIL ====')
    dealer = Dealer(hapus_mobil=True)
    nama_mobil_yang_dicari = input("Masukkan nama mobil yang dihapus: ")
    model_mobil_yang_dicari = input("Masukkan model mobil yang dihapus: ")
    dealer.delete_mobil(nama_mobil_yang_dicari, model_mobil_yang_dicari)
  
  # method untuk mengajukan kredit mobil
  def menu6():
    print('\n==== PENGAJUAN KREDIT ====')
    customer = Customer(ajukan_kredit=True)
    tipe_pengajuan = input("Masukkan tipe pengajuan (perseorangan/perusahaan): ")
    customer.pengajuan_kredit(tipe_pengajuan)
  
  # method untuk membeli mobil berdasarkan input nama_mobil dan model_mobil yang diberikan customer
  def menu7():
    print('\n==== BELI MOBIL ====')
    customer = Customer(beli_mobil=True)
    nama_mobil_yang_dicari = input("Masukkan nama mobil yang dibeli: ")
    model_mobil_yang_dicari = input("Masukkan model mobil yang dibeli: ")
    customer.pembelian_mobil(nama_mobil_yang_dicari, model_mobil_yang_dicari)
  
  # method untuk keluar dari program (menu 8)
  def keluar():
    print("Terima kasih sudah berkunjung!")
    exit()