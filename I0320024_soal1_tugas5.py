# Menyapa pengunjung hotel
kata_pembuka = "Selamat datang,"

# Proses input
nama = input("Masukkan nama anda : ")
jenis_kelamin = input("Apa jenis kelamin anda (L?P) : ")

# Proses pengisian data pengunjung
if jenis_kelamin.upper() == "L":
    print(kata_pembuka, "Tuan", nama,"!")
else:
    print(kata_pembuka, "Nyonya", nama,"!")
