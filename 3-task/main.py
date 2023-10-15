# TUGAS OOP 3
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# File: main.py

from menu import AppMenu # import class AppMenu dari file menu.py
import os # library untuk clear screen terminal/cmd

# definisi file utama (main program)
if __name__ == "__main__":
  while True:
    os.system("clear") if os.name == "posix" else os.system("cls") # untuk clear screen terminal/cmd
    AppMenu.tampilkan_menu() # di awal, tampilkan menu terlebih dahulu
    pilihan_menu = int(input("Pilih menu (1-8): ")) # pilih menu
    
    # menjalankan menu sesuai pilihan user
    if pilihan_menu == 1:
      AppMenu.menu1()
    elif pilihan_menu == 2:
      AppMenu.menu2()
    elif pilihan_menu == 3:
      AppMenu.menu3()
    elif pilihan_menu == 4:
      AppMenu.menu4()
    elif pilihan_menu == 5:
      AppMenu.menu5()
    elif pilihan_menu == 6:
      AppMenu.menu6()
    elif pilihan_menu == 7:
      AppMenu.menu7()
    elif pilihan_menu == 8:
      AppMenu.keluar()
    else:
      # jika opsi yang dipilih tidak ada, maka tampilkan pesan error
      print("Maaf, inputnya tidak sesuai!")
    
    # setelah menjalankan menu, user dapat kembali ke menu awal
    kembali = input("Kembali ke menu awal? (yes/no): ")
    if kembali == "yes": continue # kembali ke menu awal
    else: AppMenu.keluar() # keluar dari program
