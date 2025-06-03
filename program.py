import random

# Kullanıcıdan sayı al
sayi = input("Bir sayı girin: ")

# Son üç haneyi al
son_uc_hane = int(sayi[-3:])

# random modülünü tohumla
random.seed(son_uc_hane)

# 10 adet rastgele sayı üret ve listeye ekle
rastgele_sayilar = []
for _ in range(10):
    rastgele_sayilar.append(random.randint(1, 100))  # 1 ile 100 arasında sayılar

# Listeyi yazdır
print("Üretilen rastgele sayılar:", rastgele_sayilar)
