def judul(): #tanpa parameter yang didalem () tidak ada isi
    print('--------------------------------------')
    print("\t\nLatihan Pertemuan 3\t\nFungsi dan Operator")
    print('------------------------------------\n')
    
def hitungbmi(berat,tinggi): #parameter diisi yang didalam ()
    print("Maka BMI anda adalah ", berat/(tinggi*tinggi))

judul()
nim=input("Masukkan Nim = ")
nama=input("Masukkan Nama = ")
b=int(input("Masukkan berat anda = "))
t=float(input("Masukkan tinggi anda = "))
judul()
hitungbmi(b,t)