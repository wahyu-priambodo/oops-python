# TUGAS OOP 2
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B

class Mahasiswa:
  def __init__(self, nama, nilai):
    self.nama = nama
    self.nilai = nilai
    
  def tampilkan_nama(self):
    print(f"==== MAHASISWA ====")
    print(f"Nama Mahasiswa\t\t: {self.nama}")
  
  def kalkulasi(self):
    print(f"Nilai Anda\t\t: {self.nilai}")
    if self.nilai >= 81 and self.nilai <= 100:
      print(f"Huruf Mutu/Sebutan Mutu\t: A (Sangat Istimewa)")
    elif self.nilai >= 76 and self.nilai <= 80.9:
      print("Huruf Mutu/Sebutan Mutu\t: A- (Istimewa)")
    elif self.nilai >= 72 and self.nilai <= 75.9:
      print("Huruf Mutu/Sebutan Mutu\t: B+ (Lebih dari Baik)")
    elif self.nilai >= 68 and self.nilai <= 71.9:
      print("Huruf Mutu/Sebutan Mutu\t: B (Baik)")
    elif self.nilai >= 64 and self.nilai <= 67.9:
      print("Huruf Mutu/Sebutan Mutu\t: B- (Cukup Baik)")
    elif self.nilai >= 60 and self.nilai <= 63.9:
      print("Huruf Mutu/Sebutan Mutu\t: C+ (Lebih dari Cukup)")
    elif self.nilai >= 56 and self.nilai <= 59.9:
      print("Huruf Mutu/Sebutan Mutu\t: C (Cukup)")
    elif self.nilai >= 41 and self.nilai <= 55.9:
      print("Huruf Mutu/Sebutan Mutu\t: D (Kurang)")
    elif self.nilai >= 1 and self.nilai <= 40.9:
      print("Huruf Mutu/Sebutan Mutu\t: E (Gagal)")
    else:
      print("[ERROR]: Unregistered in our system!")
    print("") # for new line

# Tugas: Mencari nilai akhir mahasiswa menggunakan konsep OOP
mhs1 = Mahasiswa("Wahyu Priambodo", 80)
mhs1.tampilkan_nama()
mhs1.kalkulasi()

mhs2 = Mahasiswa("Shaquille Ariza Hidayat", 90)
mhs2.tampilkan_nama()
mhs2.kalkulasi()

mhs3 = Mahasiswa("Muhammad Brian Azura Nixon", 71.9)
mhs3.tampilkan_nama()
mhs3.kalkulasi()