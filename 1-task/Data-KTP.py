# TUGAS OOP 1
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B

class DataKTP:
  def __init__(self, nik, nama, ttl, jk, alamat, agama, status, pekerjaan, kewarganegaraan, lifetime):
    self.nik = nik
    self.nama = nama
    self.ttl = ttl
    self.jk = jk
    self.alamat = alamat
    self.agama = agama
    self.status = status
    self.pekerjaan = pekerjaan
    self.kewarganegaraan = kewarganegaraan
    self.lifetime = lifetime
  
  def siapa_aku(self):
    print("==== DATA e-KTP ====")
    print(f"NIK\t\t\t: {self.nik}")
    print(f"Nama\t\t\t: {self.nama}")
    print(f"Tempat, Tanggal Lahir\t: {self.ttl}")
    print(f"Jenis Kelamin\t\t: {self.jk}")
    print(f"Alamat\t\t\t: {self.alamat}")
    print(f"Agama\t\t\t: {self.agama}")
    print(f"Status Perkawinan\t: {self.status}")
    print(f"Pekerjaan\t\t: {self.pekerjaan}")
    print(f"Kewarganegaraan\t\t: {self.kewarganegaraan}")
    print(f"Berlaku Hingga\t\t: {self.lifetime}\n")

# Tugas: Mencari 5 e-KTP orang random di internet dan tampilkan informasi yang tertera
# 1. img src: https://www.gurusiana.id/read/abdurraufshaleng/article/makna-di-balik-nomor-ktp-atau-nik-yang-tersimpan-di-dompet-anda-10009
orang1 = DataKTP(7312042510720002, "ABDURRAUF, S.Pd, M.Pd", "CELLENGENGE, 25-10-1972", "LAKI-LAKI", "JL. MERDEKA NO.43", "ISLAM", "KAWIN", "PEGAWAI NEGERI SIPIL (PNS)", "WNI", "SEUMUR HIDUP")
orang1.siapa_aku()

# 2. img src: https://img.harianjogja.com/posts/2021/02/14/1063655/ektptsunami281218.jpg
orang2 = DataKTP(3601120705880002, "RUSLI", "PANDEGLANG, 17702-1988", "LAKI-LAKI", "KP BADONGAN", "ISLAM", "BELUM KAWIN", "WIRASWASTA", "WNI", "22-02-2017")
orang2.siapa_aku()

# 3. img src: https://dukcapil.pesawarankab.go.id/images/artikel/uploads/268_FOTO.JPG.jpg
orang3 = DataKTP(1809015306970005, "VINA AMELIA", "KESUGIHAN, 13-06-1997", "PEREMPUAN", "KESUGIHAN KARANG ANYAR", "ISLAM", "BELUM KAWIN", "BELUM/TIDAK BEKERJA", "WNI", "SEUMUR HIDUP")
orang3.siapa_aku()

# 4. img src: https://cdc.ui.ac.id/wp-content/uploads/2022/07/ktp.jpeg
orang4 = DataKTP(3305010404990003, "LANGGENG RIFA'I", "INHIL, 04-04-2000", "LAKI-LAKI", "KEMUSUK", "ISLAM", "BELUM KAWIN", "PELAJAR/MAHASISWA", "WNI", "SEUMUR HIDUP")
orang4.siapa_aku()

# 5. img src: https://mmc.tirto.id/image/otf/700x0/2017/12/28/penghayat-kepribaden-6--tirto-_ratio-16x9.jpg
orang5 = DataKTP(3175101607500004, "SUBARYO", "PEKALONGAN, 16-07-1950", "LAKI-LAKI", "PRIMKOPTI BLOK B.6 NO.2", "KEPERCAYAAN", "KAWIN", "WIRASWASTA", "WNI", "SEUMUR HIDUP")
orang5.siapa_aku()