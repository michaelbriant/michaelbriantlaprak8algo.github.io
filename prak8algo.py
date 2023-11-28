# elkom1
def karakter_ganjil(input_kata):
    print("Karakter Index Ganjil:")
    for i in range(len(input_kata)):
        if i % 2 != 0:
            print(input_kata[i], end="")

# input kata
inputan = input("Masukkan sebuah kata: ")
karakter_ganjil(inputan)
print()


# elkom2
print()
print('PROGRAM MENGHITUNG JUMLAH RANGE')
def hitung_jumlah_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

# Input rentang dari pengguna
start_num = int(input("masukan angka pertama: "))
end_num = int(input("masukan angka kedua: "))

# Hitung jumlah rentang dan cetak hasilnya
hasil = hitung_jumlah_range(start_num, end_num)
print(f'Jumlah range adalah: {hasil}')