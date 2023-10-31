#1 
list=["B 3224 FAL","CBR150R","150 cc","Hitam"]
print(list)

#2
list.append(35_000_000)
list.append("4 roda")
print(list)

list.insert(2,"Honda")
list.insert(3,"Motor")
print(list)

#3
luas_bangun_datar = input("Pilih jenis bangun datar untuk menghitung luas: ").lower()
match luas_bangun_datar:

    case "persegi":
        sisi_persegi = float(input('Input panjang sisi persegi: '))
        luas_persegi = sisi_persegi * sisi_persegi
        print('Luas persegi = ', round(luas_persegi,2))

    case "lingkaran":
        phi = 3.14
        r = float(input('Masukkan jari-jari lingkaran: ') )
        luas_lingkaran = phi * r * r
        print("luas lingkaran= ", round(luas_lingkaran,2))

    case "segitiga":
        alas_segitiga = float(input('Masukkan Alas Segitiga: '))
        tinggi_segitiga = float(input('Masukkan Tinggi Segitiga: '))
        luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
        print("luas Segitiga", round(luas_segitiga,2))
        
    case _:
        print("Salah memasukkan pilihan")

