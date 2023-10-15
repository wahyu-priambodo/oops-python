# TUGAS OOP 3
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# File: customer.py

from mobil import list_semua_mobil

# Class Customer untuk mengajukan kredit dan membeli mobil
class Customer:
  # Constructor untuk menentukan pilihan customer (ajukan_kredit atau beli_mobil)
  def __init__(self, ajukan_kredit=False, beli_mobil=False):
    self.ajukan_kredit = ajukan_kredit
    self.beli_mobil = beli_mobil
  
  # method untuk customer mengajukan kredit, baik perseorangan maupun perusahaan
  def pengajuan_kredit(self, tipe_pengajuan):
    dokumen_persyaratan = []
    
    if tipe_pengajuan.lower() == "perseorangan" or tipe_pengajuan.lower() == "perusahaan":
      if tipe_pengajuan.lower() == "perseorangan":
        dokumen_persyaratan = [
          "KTP Suami + Istri",
          "Kartu Keluarga",
          "NPWP",
          "PBB / AJB Rumah",
          "Rekening tabungan 3 bln terakhir",
          "Slip gaji bila bekerja, SKU bila pelaku usaha"
        ]
      elif tipe_pengajuan.lower() == "perusahaan":
        dokumen_persyaratan = [
          "Fotocopy akte pendirian & perubahannya",
          "Fotocopy pengesahan kehakiman",
          "Fotocopy SIUP, NPWP, SITU / Domisili, TDP",
          "Fotocopy Rek. Koran 3 bulan terakhir",
          "Fotocopy KTP direksi & komisaris"
        ]
      
      # Untuk menampilkan semua dokumen persyaratan
      for i, dokumen in enumerate(dokumen_persyaratan, start=1):
        print(f"{i}. {dokumen}")
      print()
      
      lengkap = input("Apakah dokumen persyaratan sudah lengkap? (yes/no): ")
      # dokumen persyaratan lengkap
      if lengkap.lower() == "yes":
        print("-> Pengajuan kredit mobil kami approve!\n")
      # dokumen persyaratan tidak lengkap
      elif lengkap.lower() == "no":
        print("-> Pengajuan kredit mobil kami pending terlebih dahulu!\n"
              "-> Silahkan melengkapi dokumen persyaratan yang kurang!\n")
    # Inputnya tidak sesuai
    else:
      print("-> Maaf, inputnya tidak sesuai!\n")

  # method untuk mengkalkulasikan harga mobil yang dibeli
  def pembelian_mobil(self, nama_mobil_yang_dicari, model_mobil_yang_dicari):
    harga = 0
    found = False # Untuk melacak apakah mobil ditemukan
    
    for mobil in list_semua_mobil:
      if (mobil.nama_mobil == nama_mobil_yang_dicari) and (mobil.model_mobil == model_mobil_yang_dicari):
        print(f"Nama mobil: {mobil.nama_mobil}\n"
              f"Tipe mobil: {mobil.tipe_mobil}\n"
              f"Model mobil: {mobil.model_mobil}\n"
              f"Harga mobil: Rp. {mobil.harga_mobil:,}\n")
        
        # untuk menampilkan harga tambahan jika ada premium colour atau two tone colour
        if mobil.premium_color != 0:
          print(f"*) Premium colour + Rp. {mobil.premium_color:,}\n")
        elif mobil.two_tone_color != 0:
          print(f"*) Two tone colour + Rp. {mobil.two_tone_color:,}\n")
        
        beli = input("Apakah yakin ingin membeli mobil ini? (yes/no): ")
        if beli.lower() == "yes":
          harga += mobil.harga_mobil
          
          # Mobil punya premium/two tone colour
          if (mobil.premium_color != 0) or (mobil.two_tone_color != 0):
            tambahan_colour = input("Apakah ingin menambahkan premium/two tone colour? (yes/no): ")
            if tambahan_colour.lower() == "yes":
              harga += mobil.premium_color if mobil.premium_color != 0 else mobil.two_tone_color
              print(f"\n-> Mobil berhasil dibeli dengan harga Rp. {harga:,} (include additional colour)\n")
            elif tambahan_colour.lower() == "no":
              harga += 0
              print(f"\n-> Mobil berhasil dibeli dengan harga Rp. {harga:,}!\n")
            else:
              print("\n-> Maaf, inputnya tidak sesuai!\n")
          # Mobil tidak punya premium/two tone colour
          else:
            print(f"\n-> Mobil berhasil dibeli dengan harga Rp. {harga:,}!\n")
        # Mobil tidak jadi dibeli
        elif beli.lower() == "no":
          print("\n-> Mobil tidak jadi dibeli!\n")
        # Input tidak sesuai
        else:
          print("\n-> Maaf, inputnya tidak sesuai!\n")
        
        found = True # Mobil ditemukan
    
    if not found: # Mobil tidak ditemukan
      print("\n-> Maaf, mobil yang dicari tidak ada!\n")