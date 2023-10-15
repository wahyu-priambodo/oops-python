# TUGAS OOP 3
# Author: Wahyu Priambodo / 2207421048 / TMJ 3B
# File: mobil.py

# Class Mobil sebagai template/kerangka untuk membuat objek-objek mobil
class Mobil:
  # Constructor untuk membuat objek-objek mobil
  def __init__(self, nama_mobil, tipe_mobil, model_mobil, harga_mobil, premium_color=0, two_tone_color=0):
    self.nama_mobil = nama_mobil
    self.tipe_mobil = tipe_mobil
    self.model_mobil = model_mobil
    self.harga_mobil = harga_mobil
    self.premium_color = premium_color
    self.two_tone_color = two_tone_color

# ------ TIPE MPV ------
# Mobil veloz
veloz1 = Mobil("ALL NEW VELOZ", "MPV", "1.5 MT", 286_000_000, premium_color=1_500_000)
veloz2 = Mobil("ALL NEW VELOZ", "MPV", "1.5 Q CVT", 309_100_000, premium_color=1_500_000)
veloz3 = Mobil("ALL NEW VELOZ", "MPV", "1.5 Q CVT TSS", 331_100_000, premium_color=1_500_000)

# Mobil avanza
avanza1 = Mobil("ALL NEW AVANZA", "MPV", "1.3 MT", 233_100_000)
avanza2 = Mobil("ALL NEW AVANZA", "MPV", "1.3 CVT", 247_800_000)
avanza3 = Mobil("ALL NEW AVANZA", "MPV", "1.5 G MT", 255_100_000)
avanza4 = Mobil("ALL NEW AVANZA", "MPV", "1.5 G CVT", 269_800_000)
avanza5 = Mobil("ALL NEW AVANZA", "MPV", "1.5 G CVT TSS", 295_800_000)

# Mobil calya
calya1 = Mobil("ALL NEW CALYA", "MPV", "1.2 E MT STD", 160_900_000)
calya2 = Mobil("ALL NEW CALYA", "MPV", "1.2 E MT", 163_800_000)
calya3 = Mobil("ALL NEW CALYA", "MPV", "1.2 G MT", 169_400_000)
calya4 = Mobil("ALL NEW CALYA", "MPV", "1.2 G AT", 183_600_000)

# Mobil innova
innova1 = Mobil("ALL NEW INNOVA", "MPV", "2.0 G MT", 369_600_000)
innova2 = Mobil("ALL NEW INNOVA", "MPV", "2.4 G MT", 397_100_000)

# Mobil alphard_velfire
alphard_velfire1 = Mobil("ALL NEW ALPHARD & VELFIRE", "MPV", "2.5 G AT", 1_344_800_000, premium_color=3_100_000)
alphard_velfire2 = Mobil("ALL NEW ALPHARD & VELFIRE", "MPV", "2.5 VELFIRE", 1_359_600_000, premium_color=3_100_000)

# Mobil innova_zenix
innova_zenix1 = Mobil("ALL NEW INNOVA ZENIX", "MPV", "Zenix 2.0 G CVT", 419_000_000, premium_color=3_000_000)
innova_zenix2 = Mobil("ALL NEW INNOVA ZENIX", "MPV", "Zenix 2.0 V CVT", 467_000_000, premium_color=3_000_000)
innova_zenix3 = Mobil("ALL NEW INNOVA ZENIX", "MPV", "Zenix 2.0 G HV CVT", 458_000_000, premium_color=3_000_000)
innova_zenix4 = Mobil("ALL NEW INNOVA ZENIX", "MPV", "Zenix 2.0 V HV CVT", 532_000_000, premium_color=3_000_000)
innova_zenix5 = Mobil("ALL NEW INNOVA ZENIX", "MPV", "Zenix 2.0 Q HV CVT", 611_000_000, premium_color=3_000_000)

# ------ TIPE SUV ------
# Mobil rush
rush1 = Mobil("ALL NEW RUSH", "SUV", "1.5 G MT", 278_800_000)
rush2 = Mobil("ALL NEW RUSH", "SUV", "1.5 G AT", 289_600_000)
rush3 = Mobil("ALL NEW RUSH", "SUV", "1.5 GR MT", 291_500_000)
rush4 = Mobil("ALL NEW RUSH", "SUV", "1.5 GR AT", 302_200_000)

# Mobil raize - Two Tone Colour
raize1 = Mobil("ALL NEW RAIZE", "SUV", "1.2 G MT", 232_400_000, two_tone_color=2_700_000)
raize2 = Mobil("ALL NEW RAIZE", "SUV", "1.2 G CVT", 247_300_000, two_tone_color=2_700_000)
raize3 = Mobil("ALL NEW RAIZE", "SUV", "1.0 G MT", 251_900_000, two_tone_color=2_700_000)
raize4 = Mobil("ALL NEW RAIZE", "SUV", "1.0 G CVT", 266_900_000, two_tone_color=2_700_000)
raize5 = Mobil("ALL NEW RAIZE", "SUV", "1.0 GR CVT", 280_800_000, two_tone_color=2_700_000)
raize6 = Mobil("ALL NEW RAIZE", "SUV", "1.0 GR CVT TSS", 302_500_000, two_tone_color=2_700_000)

# Mobil fortuner
fortuner1 = Mobil("ALL NEW FORTUNER", "SUV", "2.4 VRZ (4x2)", 606_200_000)
fortuner2 = Mobil("ALL NEW FORTUNER", "SUV", "2.4 VRZ GR (4x2)", 624_950_000)
fortuner3 = Mobil("ALL NEW FORTUNER", "SUV", "2.4 VRZ GR (4x4)", 715_350_000)

# Mobil corolla cross
corolla_cross1 = Mobil("ALL NEW COROLLA CROSS", "SUV", "1.8 HYBRID AT", 540_900_000, premium_color=3_800_000)

# ------ TIPE HATCHBACK ------
# Mobil agya
agya1 = Mobil("ALL NEW AGYA", "HATCHBACK", "1.2 G MT STD", 159_700_000)
agya2 = Mobil("ALL NEW AGYA", "HATCHBACK", "1.2 G AT STD", 173_300_000)
agya3 = Mobil("ALL NEW AGYA", "HATCHBACK", "1.2 GR MT", 165_500_000)
agya4 = Mobil("ALL NEW AGYA", "HATCHBACK", "1.2 GR AT", 181_500_000)

# Mobil yaris
yaris1 = Mobil("ALL NEW YARIS", "HATCHBACK", "1.2 G CVT 3 AB", 295_800_000)
yaris2 = Mobil("ALL NEW YARIS", "HATCHBACK", "1.5 S MT GR 3 AB", 308_100_000)
yaris3 = Mobil("ALL NEW YARIS", "HATCHBACK", "1.5 S CVT GR 3AB", 320_300_000)
yaris4 = Mobil("ALL NEW YARIS", "HATCHBACK", "1.5 S CVT GR 7AB", 325_700_000)

# ------ TIPE SEDAN ------
# Mobil corolla_altis
corolla_altis1 = Mobil("ALL NEW COROLLA ALTIS", "SEDAN", "1.8 V AT", 514_200_000, premium_color=3_000_000)
corolla_altis2 = Mobil("ALL NEW COROLLA ALTIS", "SEDAN", "1.8 HYBIRD AT", 565_600_000, premium_color=3_000_000)

# Mobil camry
camry1 = Mobil("ALL NEW CAMRY", "SEDAN", "2.5 V AT", 741_700_000, premium_color=3_000_000)
camry2 = Mobil("ALL NEW CAMRY", "SEDAN", "1.5 L AT", 874_600_000, premium_color=3_000_000)

# Mobil vios
vios1 = Mobil("ALL NEW VIOS", "SEDAN", "1.5 E MT", 314_900_000, premium_color=1_500_000)
vios2 = Mobil("ALL NEW VIOS", "SEDAN", "1.5 G CVT", 355_200_000, premium_color=1_500_000)
vios3 = Mobil("ALL NEW VIOS", "SEDAN", "1.5 G CVT TSS", 368_400_000, premium_color=1_500_000)

# ------ TIPE SPORT ------
# Mobil gr86
gr86_1 = Mobil("ALL NEW GR 86", "SPORT", "GR 86 2.4L M/T", 922_000_000)
gr86_2 = Mobil("ALL NEW GR 86", "SPORT", "GR 86 2.4L A/T", 938_500_000)

# Mobil supra
supra1 = Mobil("ALL NEW SUPRA", "SPORT", "SUPRA 3.0L A/T", 2_051_000_000)

# ------ TIPE COMMERCIAL ------
# Mobil hiace
hiace1 = Mobil("ALL NEW HIACE", "COMMERCIAL", "COMUTTER MT", 545_000_000)
hiace2 = Mobil("ALL NEW HIACE", "COMMERCIAL", "PREMIO MT", 630_000_000)

# Mobil hilux
hilux1 = Mobil("ALL NEW HILUX", "COMMERCIAL", "SC 2.0 MT BSN", 269_900_000)
hilux2 = Mobil("ALL NEW HILUX", "COMMERCIAL", "SC 2.4 MT DSL", 290_900_000)
hilux3 = Mobil("ALL NEW HILUX", "COMMERCIAL", "SC 2.4 MT 4X4 DSL", 393_800_000)
hilux4 = Mobil("ALL NEW HILUX", "COMMERCIAL", "DC E MT 4X4 DSL", 431_000_000)
hilux5 = Mobil("ALL NEW HILUX", "COMMERCIAL", "DC G MT 4X4 DSL", 464_000_000)
hilux6 = Mobil("ALL NEW HILUX", "COMMERCIAL", "DC V AT 4X4 DSL", 513_600_000)

# List semua mobil yang tersedia
list_semua_mobil = [
  veloz1, veloz2, veloz3,
  avanza1, avanza2, avanza3, avanza4, avanza5,
  calya1, calya2, calya3, calya4,
  innova1, innova2,
  alphard_velfire1, alphard_velfire2,
  innova_zenix1, innova_zenix2, innova_zenix3, innova_zenix4, innova_zenix5,
  rush1, rush2, rush3, rush4,
  raize1, raize2, raize3, raize4, raize5, raize6,
  fortuner1, fortuner2, fortuner3,
  corolla_cross1,
  agya1, agya2, agya3, agya4,
  yaris1, yaris2, yaris3, yaris4,
  corolla_altis1, corolla_altis2,
  camry1, camry2,
  vios1, vios2, vios3,
  gr86_1, gr86_2, supra1,
  hiace1, hiace2,
  hilux1, hilux2, hilux3, hilux4, hilux5, hilux6
]