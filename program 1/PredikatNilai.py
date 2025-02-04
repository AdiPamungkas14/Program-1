# Input nilai UTS dan UAS
uts = float(input("MASUKAN NILAI UTS: "))
uas = float(input("MASUKAN NILAI UAS: "))

# Menghitung Hasil Akhir
hasil_akhir = (70 / 100 * uts) + (30 / 100 * uas)

# Mencetak hasil nilai
print("=" * 60)
print("NILAI UTS:", uts)
print("NILAI UAS:", uas)
print("Hasil Akhir:", hasil_akhir)
print("=" * 60)

# Menentukan predikat nilai 
if hasil_akhir >= 86 and hasil_akhir <= 100:
    print("Predikat: Sangat Baik")
elif hasil_akhir >= 66 and hasil_akhir <= 85:
    print("Predikat: Baik")
elif hasil_akhir >= 51 and hasil_akhir <= 65:
    print("Predikat: Cukup")
elif hasil_akhir >= 31 and hasil_akhir <= 50:
    print("Predikat: Kurang")
elif hasil_akhir >= 0 and hasil_akhir <= 30:
    print("Predikat: Buruk")
else:
    print("SALAH INPUT")