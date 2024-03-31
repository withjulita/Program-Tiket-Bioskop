nma=input("Masukkan Nama Anda : ")
usia=int(input("Masukkan Usia Anda : "))

if usia >= 17 :
    print("Anda sudah cukup umur untuk menonton film")
    print("Daftar Genre :")
    print("1.Romantis")
    print("2. Komedi ")
    gnre=input("Ketik Genre film : ")
    if gnre =="romantis":
        print("Daftar film genre romantis :")
        print("1. Ayat Ayat Cinta")
        print("2 Habibie dan Ainun")
        film=input("Pilih Film : ")
        if film =="ayat ayat cinta":
            print("Ayat Ayat Cinta")
        else:
            film="Habibie dan Ainun"
    else:
        gnre="Komedi"
        print("Daftar film genre Komedi :")
        print("1. Warkop DKI")
        print("2. Cek Toko Sebelah")
        film=int(input("Pilih Film : "))
        if film =="film":
            print("Warkop DKI")
        else:
            film="Cek Toko Sebelah"

else:
    print("Anda belum cukup umur untuk menonton film")

print("1.Senin - Jumat = Rp. 40.000")
print("2. Sabtu = Rp. 45.000")  
print("3. Minggu = Rp. 50.000") 
hrga=int(input("Pilih Hari : "))
if hrga ==1:
    print("Pilih hari : \nSenin\nSelasa\nRabu\nKamis\nJumat")
    hri=input("Ketik hari : ")
    hrga=40000
elif hrga ==2:
    hri="Sabtu"
    hrga=45000
else:
    hri="Minggu"
    hrga=50000

print("Pilih waktu nonton :")
print("1. 14.10")
print("2. 20.00")
wktu=input("Pilih waktu nonton Anda : ")
if wktu ==1:
    print("Jam 14.10")
    waktu='14.10'
else:
    print("Jam 20.00")
    waktu='20.00'

print("===========================================")
print("Atas nama : ",nma)
print("Usia : ",usia)
print("Genre yang dipilih : ",gnre)
print("Film yang ditonton : ", film)
print("Total : ",hrga)
print("Pada hari : ",hri)
print("Jam nonton : ",waktu)
print("===========================================")




