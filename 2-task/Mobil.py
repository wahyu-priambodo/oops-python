# TUGAS OOP 2
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# Link: https://toyotapromobekasi.id/daftar-harga

# Class `Mobil` sebagai template untuk membuat objek mobil
class Mobil:
  # constructor untuk menginisialisasi atribut-atribut pada objek mobil
  def __init__(self, nama_mobil, tipe_mobil, model_dan_harga, custom_colour=None):
    self.nama_mobil = nama_mobil
    self.tipe_mobil = tipe_mobil
    self.model_dan_harga = model_dan_harga
    self.custom_colour = custom_colour
  
  # method untuk menampilkan semua list mobil yang tersedia
  def tampilkan_semua_mobil(list_semua_mobil):
    # menampilkan semua list mobil dari nama mobil - custom colour (jika ada)
    for mobil in list_semua_mobil:
      print("-"*34)
      # untuk menampilkan nama dan tipe mobil
      print(f"{mobil.nama_mobil}\nTipe mobil: {mobil.tipe_mobil}")
      # untuk menampilkan model dan harga yang ada di dictionary
      for model, harga in mobil.model_dan_harga.items():
        print(f"- {model}: Rp{harga:,}")
        
      # jika mobil memiliki custom colour, maka tampilkan juga custom colournya
      # custom colour untuk mobil selain ALL NEW RAIZE adalah "PREMIUM COLOUR"
      if mobil.custom_colour != None and mobil.nama_mobil != "ALL NEW RAIZE":
        print(f"*) PREMIUM COLOUR: {mobil.custom_colour:,}")
      # custom colour untuk mobil ALL NEW RAIZE adalah "TWO TONE COLOUR"
      elif mobil.nama_mobil == "ALL NEW RAIZE":
        print(f"*) TWO TONE COLOUR: {mobil.custom_colour:,}")
      print("-"*34)
    print()

  # method untuk mencari mobil berdasarkan nomor urutan yang dipilih
  def cari_mobil(list_semua_mobil, pil_mobil):
    # cari dan tampilkan mobil berdasarkan nomor urutan yang dipilih
    # total mobil yang tersedia ada 19, jadi inputnya harus dalam range 1-19
    if 1 <= pil_mobil <= 19:
      print("\n-> Ketemu nih kak mobilnya!")
      print("-"*34)
      for i, mobil in enumerate(list_semua_mobil, start=1):
        # jika nomor urutan yang dipilih sesuai dengan nomor urutan mobil, maka tampilkan detail mobilnya
        if pil_mobil == i:
          # untuk menampilkan nama dan tipe mobil
          print(f"{mobil.nama_mobil}\nTipe mobil: {mobil.tipe_mobil}")
          # untuk menampilkan model dan harga yang ada di dictionary
          for model, harga in mobil.model_dan_harga.items():
            print(f"- {model}: Rp{harga:,}")
            
          # jika mobil memiliki custom colour, maka tampilkan juga custom colournya
          # custom colour untuk mobil selain ALL NEW RAIZE adalah "PREMIUM COLOUR"
          if mobil.custom_colour != None and mobil.nama_mobil != "ALL NEW RAIZE":
            print(f"*) PREMIUM COLOUR: {mobil.custom_colour:,}")
          # custom colour untuk mobil ALL NEW RAIZE adalah "TWO TONE COLOUR"
          elif mobil.nama_mobil == "ALL NEW RAIZE":
            print(f"*) TWO TONE COLOUR: {mobil.custom_colour:,}")
      print("-"*34)
      print()
    
    # jika inputnya < 1 atau > 19, maka tampilkan pesan error
    else: print("-> Maaf, inputnya gak sesuai kak!\n")
  
  # method untuk mengajukan kredit mobil
  def ajukan_kredit(tipe_pengajuan):
    # inisialisasi list dokumen persyaratan kosong
    dokumen_persyaratan = []
    
    # jika pilihan tipe pengajuan kreditnya 1, maka masukan dokumen persyaratan untuk perseorangan
    if tipe_pengajuan == 1:
      dokumen_persyaratan = [
        "KTP Suami + Istri",
        "Kartu Keluarga",
        "NPWP",
        "PBB / AJB Rumah",
        "Rekening tabungan 3 bln terakhir",
        "Slip gaji bila bekerja, SKU bila pelaku usaha"
      ]
    # jika pilihan tipe pengajuan kreditnya 2, maka masukan dokumen persyaratan untuk perusahaan
    elif tipe_pengajuan == 2:
      dokumen_persyaratan = [
        "Fotocopy akte pendirian & perubahannya",
        "Fotocopy pengesahan kehakiman",
        "Fotocopy SIUP, NPWP, SITU / Domisili, TDP",
        "Fotocopy Rek. Koran 3 bulan terakhir",
        "Fotocopy KTP direksi & komisaris"
      ]
    
    # return list dokumen persyaratan
    return dokumen_persyaratan

# TIPE MPV
DAFTAR_MODEL_VELOZ = {
  "1.5 MT": 286_000_000,
  "1.5 Q CVT": 309_100_000,
  "1.5 Q CVT TSS": 331_100_000,
}
DAFTAR_MODEL_AVANZA = {
  "1.3 MT": 233_100_000,
  "1.3 CVT": 247_800_000,
  "1.5 G MT": 255_100_000,
  "1.5 G CVT": 269_800_000,
  "1.5 G CVT TSS": 295_800_000
}
DAFTAR_MODEL_CALYA = {
  "1.2 E MT STD": 160_900_000,
  "1.2 E MT": 163_800_000,
  "1.2 G MT": 169_400_000,
  "1.2 G AT": 183_600_000
}
DAFTAR_MODEL_INNOVA = {
  "2.0 G MT": 369_600_000,
  "2.4 G MT": 397_100_000
}
DAFTAR_MODEL_ALPHARD_VELFIRE = {
  "2.5 G AT": 1_344_800_000,
  "2.5 VELFIRE": 1_359_600_000
}
DAFTAR_MODEL_INNOVA_ZENIX = {
  "Zenix 2.0 G CVT": 419_000_000,
  "Zenix 2.0 V CVT": 467_000_000,
  "Zenix 2.0 G HV CVT": 458_000_000,
  "Zenix 2.0 V HV CVT": 532_000_000,
  "Zenix 2.0 Q HV CVT": 611_000_000,
}

# TIPE SUV
DAFTAR_MODEL_RUSH = {
  "1.5 G MT": 278_800_000,
  "1.5 G AT": 289_600_000,
  "1.5 GR MT": 291_500_000,
  "1.5 GR AT": 302_200_000
}
DAFTAR_MODEL_RAIZE = {
  "1.2 G MT": 232_400_000,
  "1.2 G CVT": 247_300_000,
  "1.0 G MT": 251_900_000,
  "1.0 G CVT": 266_900_000,
  "1.0 GR CVT": 280_800_000,
  "1.0 GR CVT TSS": 302_500_000  
}
DAFTAR_MODEL_FORTUNER = {
  "2.8 VRZ (4x2)": 606_200_000,
  "2.8 VRZ GR (4x2)": 624_950_000,
  "2.8 VRZ GR (4x4)": 715_350_000
}
DAFTAR_MODEL_COROLLA_CROSS = {
  "1.8 HYBRID AT": 540_900_000
}

# TIPE HATCHBACK
DAFTAR_MODE_AGYA = {
  "1.2 G MT STD": 159_700_000,
  "1.2 G AT STD": 173_300_000,
  "1.2 GR MT": 165_500_000,
  "1.2 GR AT": 181_500_000
}
DAFTAR_MODEL_YARIS = {
  "1.2 G CVT 3 AB": 295_800_000,
  "1.5 S MT GR 3 AB": 308_100_000,
  "1.5 S CVT GR 3AB": 320_300_000,
  "1.5 S CVT GR 7AB": 325_700_000
}

# TIPE SEDAN
DAFTAR_MODEL_COROLLA_ALTIS = {
  "1.8 V AT": 514_200_000,
  "1.8 HYBIRD AT": 565_600_000,
}
DAFTAR_MODEL_CAMRY = {
  "2.5 V AT": 741_700_000,
  "1.5 L AT": 874_600_000
}
DAFTAR_MODEL_VIOS = {
  "1.5 E MT": 314_900_000,
  "1.5 G CVT": 355_200_000,
  "1.5 G CVT TSS": 368_400_000
}

# TIPE SPORT
DAFTAR_MODEL_GR86 = {
  "GR 86 2.4L M/T": 922_000_000,
  "GR 86 2.4L A/T": 938_500_000
}
DAFTAR_MODEL_SUPRA = {
  "SUPRA 3.0L A/T": 2_051_000_000
}

# TIPE COMMERCIAL
DAFTAR_MODEL_HIACE = {
  "COMUTTER MT": 545_000_000,
  "PREMIO MT": 630_000_000
}
DAFTAR_MODEL_HILUX = {
  "SC 2.0 MT BSN": 269_900_000,
  "SC 2.4 MT DSL": 290_900_000,
  "SC 2.4 MT 4X4 DSL": 393_800_000,
  "DC E MT 4X4 DSL": 431_000_000,
  "DC G MT 4X4 DSL": 464_000_000,
  "DC V AT 4X4 DSL": 513_600_000
}

# Objek semua brand mobil
veloz = Mobil("ALL NEW VELOZ", "MPV", DAFTAR_MODEL_VELOZ, 1_500_000)
avanza = Mobil("ALL NEW AVANZA", "MPV", DAFTAR_MODEL_AVANZA)
calya = Mobil("ALL NEW CALYA", "MPV", DAFTAR_MODEL_CALYA)
innova = Mobil("ALL NEW INNOVA", "MPV", DAFTAR_MODEL_INNOVA)
alphard_velfire = Mobil("ALL NEW ALPHARD & VELFIRE", "MPV", DAFTAR_MODEL_ALPHARD_VELFIRE, 3_100_000)
innova_zenix = Mobil("ALL NEW INNOVA ZENIX", "MPV", DAFTAR_MODEL_INNOVA_ZENIX, 3_000_000)
rush = Mobil("ALL NEW RUSH", "SUV", DAFTAR_MODEL_RUSH)
raize = Mobil("ALL NEW RAIZE", "SUV", DAFTAR_MODEL_RAIZE, 2_700_000)
fortuner = Mobil("ALL NEW FORTUNER", "SUV", DAFTAR_MODEL_FORTUNER)
corolla_cross = Mobil("ALL NEW COROLLA CROSS", "SUV", DAFTAR_MODEL_COROLLA_CROSS, 3_800_000)
agya = Mobil("ALL NEW AGYA", "HATCHBACK", DAFTAR_MODE_AGYA)
yaris = Mobil("ALL NEW YARIS", "HATCHBACK", DAFTAR_MODEL_YARIS)
corolla_altis = Mobil("ALL NEW COROLLA ALTIS", "SEDAN", DAFTAR_MODEL_COROLLA_ALTIS, 3_000_000)
camry = Mobil("ALL NEW CAMRY", "SEDAN", DAFTAR_MODEL_CAMRY, 3_000_000)
vios = Mobil("ALL NEW VIOS", "SEDAN", DAFTAR_MODEL_VIOS, 1_500_000)
gr86 = Mobil("ALL NEW GR 86", "SPORT", DAFTAR_MODEL_GR86)
supra = Mobil("ALL NEW SUPRA", "SPORT", DAFTAR_MODEL_SUPRA)
hiace = Mobil("ALL NEW HIACE", "COMMERCIAL", DAFTAR_MODEL_HIACE)
hilux = Mobil("ALL NEW HILUX", "COMMERCIAL", DAFTAR_MODEL_HILUX)

# list semua objek mobil yang telah dibuat 
list_semua_mobil = [veloz, avanza, calya, innova, alphard_velfire, innova_zenix, rush, raize, fortuner, corolla_cross, agya, yaris, corolla_altis, camry, vios, gr86, supra, hiace, hilux]


# Class `Menu` untuk menampilkan dan memilih menu
class Menu:
  # constructor untuk menginisialisasi atribut pilihan
  def __init__(self, pilihan):
    self.pilihan = pilihan
  
  # method untuk menampilkan menu
  def tampilkan_menu():
    print("==== TUNAS TOYOTA BEKASI ====")
    print("1. Tampilkan semua mobil\n"
          "2. Cari mobil\n"
          "3. Ajukan kredit\n"
          "4. Keluar\n")
  
  # method untuk menampilkan menu
  def pilihan1():
    print()
    # menampilkan nama, tipe, model, dan harga mobil
    print("\nDaftar Mobil & Harga:")
    Mobil.tampilkan_semua_mobil(list_semua_mobil)
  
  # method untuk mencari mobil
  def pilihan2():
    # menampilkan nama-nama mobilnya saja
    print("\nDaftar Mobil:")
    for i, mobil in enumerate(list_semua_mobil, start=1):
      print(f"{i}. {mobil.nama_mobil}")
    
    # cari mobil berdasarkan nomor urutan yang dipilih
    pil_mobil = int(input("\nCari mobil apa kak? (1-19): "))
    
    # memanggil method `cari_mobil` untuk mencari mobil berdasarkan nomor urutan yang dipilih
    Mobil.cari_mobil(list_semua_mobil, pil_mobil)
    
    # setelah menampilkan detail mobilnya, user dapat mencari mobil yang lain
    cari_lagi = input("Mau cari mobil yang lain? (yes/no): ")
    if cari_lagi.lower() == "yes": Menu.pilihan2()
  
  # method untuk pengajuan kredit mobil
  def pilihan3():
    # di awal, pilih tipe pengajuan kredit (perseorangan atau perusahaan)
    print("\nPilih tipe pengajuan kredit dulu kak:\n"
          "1. Perseorangan\n"
          "2. Perusahaan\n")
    pil_kredit = int(input("Pilih tipe pengajuan kredit: "))
    Mobil.ajukan_kredit(pil_kredit)

    # jika pilihan kredit = 1 atau 2, maka tampilkan dokumen persyaratan kredit sesuai tipe pengajuannya
    if pil_kredit == 1 or pil_kredit == 2:
      # jika pilihan user 1, maka tipe kreditnya perseorangan. Jika 2, maka tipe kreditnya perusahaan
      tipe_kredit = "perseorangan" if pil_kredit == 1 else "perusahaan"
      
      # untuk menampilkan semua dokumen persyaratan kredit yang ada di list
      print(f"\nDokumen persyaratan kredit `{tipe_kredit}`")
      for i, dokumen in enumerate(Mobil.ajukan_kredit(pil_kredit), start=1):
        print(f"{i}. {dokumen}")
      
      pengajuan = input("\nApakah dokumen persyaratannya udah lengkap kak? (yes/no): ")
      # jika dokumen persyaratan sudah lengkap semua, maka pengajuan kreditnya diterima (approved)
      if pengajuan == "yes":
        print("\n-> Pengajuan kredit kami approve ya kak. Terima kasih sudah berbelanja!\n")
      # jika dokumen persyaratan belum lengkap, maka pengajuan kreditnya ditolak (pending)
      elif pengajuan == "no":
        print("\n-> Maaf, pengajuan kredit sementara kami pending dulu ya kak\n"
              "-> Silahkan melengkapi semua dokumen persyaratannya dulu yaa. Terima kasih!\n")
      else:
        print("-> Maaf, inputnya gak sesuai kak!\n")
        
    # jika pilihan kredit != 1 atau 2, maka tampilkan pesan error
    else:
      print("-> Maaf, inputnya gak sesuai kak!\n")
  
  # method untuk keluar dari program
  def keluar():
    print("Terima kasih sudah mampir!")
    exit()

# Definisi main program
if __name__ == "__main__":
  import os # import library os untuk clear screen
  
  # program akan berjalan terus-menerus sampai user memilih opsi keluar
  while True:
    os.system("clear") if os.name == "posix" else os.system("cls") # untuk clear screen terminal/cmd
    Menu.tampilkan_menu() # di awal, tampilkan menu terlebih dahulu
    pil_menu = int(input("Pilih menu dulu yuk kak (1-4): "))
    
    # menjalankan menu sesuai pilihan user
    if pil_menu == 1:
      Menu.pilihan1()
    elif pil_menu == 2:
      Menu.pilihan2()
    elif pil_menu == 3:
      Menu.pilihan3()
    elif pil_menu == 4:
      Menu.keluar()
    else:
      # jika opsi yang dipilih tidak ada, maka tampilkan pesan error
      print("Maaf kak, opsinya gak ada!")
    
    # setelah menjalankan menu, user dapat kembali ke menu awal atau tidak
    kembali = input("Balik ke menu awal? (yes/no): ")
    if kembali == "yes": continue # kembali ke menu awal
    else: Menu.keluar() # keluar dari program
