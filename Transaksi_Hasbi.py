#Fungsi untuk membaca file teks
def baca_data(filename):
    
    #Membuka dan Membaca file teks .txt per baris
    file = open(filename,"r")
    teks = file.readline()
    
    #Deklarasi variabel
    list_tanggal = []
    list_bayar = []
    list_sementara = []
    list_btb = []
    dict_transaksi = {} #key adalah indeks bln/thn, value adalah total transaksi pada bln/thn tersebut
    i=0
    j=1

    
    while teks != "" :
        #Memecah file teks berdasarkan spasi dan dimasukan kedalam list_sementara
        list_sementara = teks.split()

        #Mengambil elemen list terakhir (transaksi) untuk dimasukan kedalam list_bayar
        bayar = list_sementara.pop()
        bayar = int(bayar) #String dijadikan integer
        list_bayar.append(bayar)
        
        #Mengambil elemen list terakhir (tgl/bln/thn) untuk dimasukan kedalam list_tanggal
        tanggal = list_sementara.pop()
        tanggal = tanggal.split("/")
        list_tanggal.extend(tanggal)

        #Memisahkan tanggal pada list_tanggal
        tahun = list_tanggal.pop()
        bulan = list_tanggal.pop()
        bulan_tahun = bulan + "/" + tahun
        bulan_tahun_bayar = [bulan_tahun,bayar]
        
        #Memasukan bln/thn kedalam list_bt
        list_btb.extend(bulan_tahun_bayar) #Indeks 0: bln/thn, 1: transaksi

        #Memasukan data transaksi kedalam dictionary
        if list_btb[i] in dict_transaksi: #Apabila key sudah berada dalam dict, maka value akan ditambahkan
            for k,v in dict_transaksi.items():
                v += list_btb[j] #Menjumlahkan value yg sudah ada dengan value yang baru
                dict_transaksi[list_btb[i]] = v
        else: #Apabila key belum ada, maka akan dibuat value baru
            dict_transaksi[list_btb[i]] = list_btb[j]
        i+=2    
        j+=2
        
        teks = file.readline()

    file.close()
    return dict_transaksi

#Fungsi untuk mendapatkan total transaksi terendah
def terendah():
    hasil = ("(bulan/tahun) {} dengan nilai transaksi sebesar {} rupiah".format(min(dict_transaksi, key=dict_transaksi.get), dict_transaksi[min(dict_transaksi, key=dict_transaksi.get)]))
    return hasil

#Fungsi untuk mendapatkan rata-rata nilai transaksi pada 2020 dan 2021
def report():
    r2020 =[]
    r2021 =[]
    for v,y in dict_transaksi.items():
        b1 = v.split("/")
        inte = b1[1]
        xx = int(inte)
        if inte == "2020":
            r2020.append(y)
            ex = (sum(r2020)//len(r2020))
        if inte == "2021":
            r2021.append(y)
            ex2 = (sum(r2021)//len(r2021))
    return ex,ex2
    
nama_file = "data_soal.txt"
dict_transaksi = baca_data(nama_file)
print(dict_transaksi)
print("Dictionary total transaksi per bulan/tahun :", dict_transaksi, "\n")
print("Total transaksi terendah terdapat pada", terendah(), "\n")
print("Rata-rata nilai transaksi (2020,2021) : ", report())

def print_menu():
    print("1 : Tampilkan Dictionary")
    print("2 : Tampilkan Fungsi Terendah")
    print("3 : Tampilkan Rata-rata")
    print("Exit [input any key]")

x = True
while x :
    print_menu()
    pilih = input("Masukan pilihan :")
    if pilih == "1":
        print("Dictionary total transaksi per bulan/tahun :", total_transaksi(), "\n")
    elif pilih == "2":
        print("Total transaksi terendah terdapat pada", terendah(), "\n")
    elif pilih == "3":
        print("Rata-rata nilai transaksi setiap bulan per tahun : ", rerata(), "\n")
        print("Rata-rata nilai transaksi (2020,2021) : ", report())
    else:
        x = False
