# Grading nilai

# Penginputan data
nama = input("Masukkan nama anda : ")
nilai = int(input("Berapa nilai anda : "))

#Proses konversi menjadi grading huruf
if nilai < 60 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah E")
elif nilai <= 64 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah C")
elif nilai <= 69 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah C+")
elif nilai <= 74 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah B")
elif nilai <= 79 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah B+")
elif nilai <= 84 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah A-")
elif nilai <= 100 :
    print("Halo", nama, "!", "Nilai anda setelah dikoversi adalah A")
else :
    print("Halo", nama, "!", "Nilai anda tidak valid untuk dikonversi ")

