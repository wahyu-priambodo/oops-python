# TUGAS OOP 3
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# File: dealer.py

from mobil import Mobil, list_semua_mobil

# class Dealer untuk menambahkan, melihat, mengubah, dan menghapus data mobil (CRUD)
class Dealer:
  # Constructor untuk set operasi yang akan dijalankan
  def __init__(self, tambah_mobil=False, lihat_mobil=False, ubah_mobil=False, hapus_mobil=False):
    self.tambah_mobil = tambah_mobil
    self.lihat_mobil = lihat_mobil
    self.ubah_mobil = ubah_mobil
    self.hapus_mobil = hapus_mobil
  
  # method untuk menambahkan mobil bobil ke dalam list_semua_mobil
  def create_mobil(self, nama_mobil_baru, tipe_mobil_baru, model_mobil_baru, harga_mobil_baru, premium_color_baru, two_tone_color_baru):
    mobil_baru = Mobil(nama_mobil_baru, tipe_mobil_baru, model_mobil_baru, harga_mobil_baru, premium_color_baru, two_tone_color_baru)
    list_semua_mobil.append(mobil_baru)

    print("\n-> Mobil baru berhasil ditambahkan!\n")
  
  # method untuk menampilkan mobil yang dicari
  def read_mobil(self, nama_mobil_yang_dicari, model_mobil_yang_dicari):
    found = False # Untuk melacak apakah mobil ditemukan
    for mobil in list_semua_mobil:
      if (mobil.nama_mobil == nama_mobil_yang_dicari.upper()) and (mobil.model_mobil == model_mobil_yang_dicari.upper()):
        print(f"Nama mobil: {mobil.nama_mobil}\n"
              f"Tipe mobil: {mobil.tipe_mobil}\n"
              f"Model mobil: {mobil.model_mobil}\n"
              f"Harga mobil: Rp. {mobil.harga_mobil:,}\n")
        
        # untuk menampilkan harga tambahan jika ada premium colour atau two tone colour
        if mobil.premium_color != 0:
          print(f"*) Premium colour + Rp. {mobil.premium_color:,}\n")
        elif mobil.two_tone_color != 0:
          print(f"*) Two tone colour + Rp. {mobil.two_tone_color:,}\n")
        
        found = True # Mobil ditemukan
    
    if not found: # Mobil tidak ditemukan
      print("-> Maaf, mobil yang dicari tidak ada!\n")
  
  # method untuk mengubah data model_mobil dan harga_mobil yang ada di dalam list_semua_mobil
  def update_mobil(self, nama_mobil_yang_dicari, model_mobil_yang_dicari):
    found = False # Untuk melacak apakah mobil ditemukan
    
    for mobil in list_semua_mobil:
      if (mobil.nama_mobil == nama_mobil_yang_dicari.upper()) and (mobil.model_mobil == model_mobil_yang_dicari.upper()):
        print(f"Nama mobil: {mobil.nama_mobil}\n"
              f"Tipe mobil: {mobil.tipe_mobil}\n"
              f"Model mobil: {mobil.model_mobil}\n"
              f"Harga mobil: Rp. {mobil.harga_mobil:,}\n")
        
        konfirmasi = input("Apakah yakin ingin mengubah model mobil yang ini? (yes/no): ")
        if konfirmasi.lower() == "yes":
          ubah = input("Apa yang ingin diubah? (model/harga): ")
          
          if ubah.lower() == "model":
            mobil.model_mobil = input("Masukkan nama model mobil yang baru: ")
          elif ubah.lower() == "harga":
            mobil.harga_mobil = int(input("Masukkan harga mobil yang baru: "))
            
          print("-> Data mobil berhasil diubah!\n")
        elif ubah.lower() == "no":
          print("-> Data mobil tidak jadi diubah!\n")
        else:
          print("-> Maaf, inputnya tidak sesuai!\n")
        
        found = True # Mobil ditemukan
        
    if not found: # Mobil tidak ditemukan
      print("-> Maaf, mobil yang dicari tidak ada!\n")
  
  # method untuk menghapus data model_mobil yang ada di dalam list_semua_mobil
  def delete_mobil(self, nama_mobil_yang_dicari, model_mobil_yang_dicari):
    found = False # Untuk melacak apakah mobil ditemukan
    
    for mobil in list_semua_mobil:
      if (mobil.nama_mobil == nama_mobil_yang_dicari.upper()) and (mobil.model_mobil == model_mobil_yang_dicari.upper()):
        print(f"Nama mobil: {mobil.nama_mobil}\n"
              f"Tipe mobil: {mobil.tipe_mobil}\n"
              f"Model mobil: {mobil.model_mobil}\n"
              f"Harga mobil: Rp. {mobil.harga_mobil:,}\n")
        
        hapus = input("Apakah yakin ingin menghapus model mobil yang ini? (yes/no): ")
        if hapus.lower() == "yes":
          list_semua_mobil.remove(mobil)
          print("-> Data mobil berhasil dihapus!\n")
        elif hapus.lower() == "no":
          print("-> Data mobil tidak jadi dihapus!\n")
        else:
          print("-> Maaf, inputnya tidak sesuai!\n")
        
        found = True # Mobil ditemukan
    
    if not found: # Mobil tidak ditemukan
      print("-> Maaf, mobil yang dicari tidak ada!\n")