# INFORMASI DATA BARANG DI GUDANG
listGudang = [
    {
        'nomorID':'0',
        'jenis':'celana',
        'nama': 'jeans',
        'stock': 20,
        'harga': 95000
    },
    {
        'nomorID':'1',
        'jenis':'celana',
        'nama': 'chino',
        'stock': 15,
        'harga': 90000
    },
    {
        'nomorID':'2',
        'jenis':'celana',
        'nama': 'jogger',
        'stock': 25,
        'harga': 85000
    }
]

# MENU READ DATA
def menampilkanGudang() :
    while True :
        pilihan1 = input('''
                +++++ Menampilkan Barang Gudang +++++

                1.Menampilkan Semua Barang
                2.Menampilkan Barang Dengan Nomor ID Tertentu
                3.Kembali ke Menu Utama
                Silahkan pilih Sub Menu Menambah Barang [1-3] : ''')
        if pilihan1 !='1' and pilihan1 !='2' and pilihan1 !='3':
            print('Pilihan yang anda masukkan salah, pilih [1-3]\n')
            menampilkanGudang()
        elif pilihan1 == '1' :
            print('\t\t+++++ Stock Gudang +++++\n')
            print('nomorID | Jenis\t| Nama  \t| Stock\t| Harga')
            if len(listGudang) > 0 :
                for i in range(len(listGudang)) :
                    print('{}\t|{}\t| {}  \t| {}\t| {}'.format(listGudang[i]['nomorID'],listGudang[i]['jenis'],listGudang[i]['nama'],listGudang[i]['stock'],listGudang[i]['harga']))
            elif len(listGudang) == 0 :
                print ('Tidak Tersedia Barang\n')
                menampilkanGudang()
        elif pilihan1 == '2' :
            nomorIDtampil = input("Masukkan nomor ID Barang: ")
            match = False
            for i in range(len(listGudang)) :
                if listGudang[i]['nomorID'] == nomorIDtampil :
                    print('+++++ Stock Gudang +++++\n')
                    print('nomorID | Jenis\t| Nama  \t| Stock\t| Harga')       
                    print('{}\t|{}\t| {}  \t| {}\t| {}'.format(listGudang[i]['nomorID'],listGudang[i]['jenis'],listGudang[i]['nama'],listGudang[i]['stock'],listGudang[i]['harga']))
                    match -= match
                else :
                    match+=1
            if match >= len(listGudang) :
                print ('\nBarang dengan Nomor ID yang dimaksud tidak tersedia')
        elif pilihan1 == '3' :
            gudang()

# MENU CREATE DATA
def menambahGudang() :
    while True :
        pilihan2 = input('''
                +++++ Menambah Data Barang Gudang +++++

                1.Menambah Data Barang
                2.Kembali ke Menu Utama
                Silahkan pilih Sub Menu Menambah Barang [1-2] : ''')
        if pilihan2 !='1' and pilihan2 !='2' :
            print('Pilihan yang anda masukkan salah, pilih [1-2]\n')
            menambahGudang()
        elif pilihan2 == '1' :
            nomorIDtambah = input('\nMasukkan Nomor ID Barang : ')
            match = 0
            for i in range(len(listGudang)):
                if listGudang[i]['nomorID'] == nomorIDtambah:
                    print('\nData barang sudah ada')
                    match-=match
                    menambahGudang()
                else:
                    match+=1
            if match >= len(listGudang) :
                    jenisBarang = input('Masukkan Jenis Barang : ')
                    namaBarang = input('Masukkan Nama Barang : ')
                    stockBarang = int(input('Masukkan Stock Barang : '))
                    hargaBarang = int(input('Masukkan Harga Barang : '))
                    while True:
                        confirm = input('\nApakah anda ingin melanjutkan proses penambahan data barang? (Y/N)')
                        if confirm == 'Y' :
                            listGudang.append({
                            'nomorID': nomorIDtambah,
                            'jenis' : jenisBarang,
                            'nama': namaBarang,
                            'stock': stockBarang,
                            'harga': hargaBarang
                                                })
                            print('\nData barang telah tersimpan')
                            menambahGudang()
                        elif confirm == 'N' :
                            menambahGudang()
                        elif confirm != 'Y' and confirm != 'N' :
                            print('\nPilihan Salah. Pilih (Y/N)')
        elif pilihan2 == '2' :
            gudang()

# MENU UPDATE DATA
def mengubahGudang() :
    while True :
        pilihan3 = input('''
                +++++ Mengubah Barang Gudang +++++

                1.Mengubah Barang
                2.Kembali ke Menu Utama
                Silahkan pilih Sub Menu Mengubah Barang [1-2] : ''')
        if pilihan3 !='1' and pilihan3 !='2' :
            print('Pilihan yang anda masukkan salah, pilih [1-2]\n')
            mengubahGudang()
        elif pilihan3 == '1' :
            id_item_update=input('nomor ID barang yang ingin dirubah = ')
            for i in listGudang :
                if id_item_update == i['nomorID']:
                    print('+++++ Barang yang ingin Diubah +++++\n')
                    print('nomorID | Jenis\t| Nama  \t| Stock\t| Harga')
                    print('{}\t|{}\t| {}  \t| {}\t| {}'.format(i['nomorID'],i['jenis'],i['nama'],i['stock'],i['harga']))
                    while True:
                        confirm = input('\nApakah anda ingin lanjut merubah data barang? (Y/N)')
                        if confirm == 'Y' :
                            key_update=input('\nSilahkan pilih dari nama kolom berikut (jenis, nama, stock, harga) untuk data barang yang ingin diubah = ')
                            value_update=input('\nMasukkan data baru = ')
                            for i in listGudang:
                                if i['nomorID'] == id_item_update:
                                    i[key_update]=value_update
                                    while True:
                                        reconfirm = input('\nApakah anda ingin melanjutkan proses perubahan data barang? (Y/N)')
                                        if reconfirm == 'Y' :
                                            print('\nData barang telah berubah')
                                            mengubahGudang()
                                        elif reconfirm == 'N' :
                                            mengubahGudang()
                                        elif reconfirm != 'Y' and reconfirm != 'N' :
                                            print('\nPilihan Salah. Pilih (Y/N)')

                        elif confirm == 'N' :
                            mengubahGudang()
                        elif confirm != 'Y' and confirm != 'N' :
                            print('\nPilihan Salah. Pilih (Y/N)')
            else:
                print ('\nBarang dengan Nomor ID yang dimaksud tidak tersedia')
                mengubahGudang()
        
                    
        elif pilihan3 == '2' :
            gudang()

# MENU DELETE DATA
def menghapusGudang() :
    while True :
        pilihan4 = input('''
                +++++ Menghapus Barang Gudang +++++

                1.Menghapus Barang
                2.Kembali ke Menu Utama
                Silahkan pilih Sub Menu Menghapus Barang [1-2] : ''')
        if pilihan4 !='1' and pilihan4 !='2' :
            print('Pilihan yang anda masukkan salah, pilih [1-2]\n')
        elif pilihan4 == '1' :
            id_item_erase = input('\nMasukkan nomorID barang yang ingin dihapus : ')
            match = 0
            for i in range(len(listGudang)):
                if listGudang[i]['nomorID'] == id_item_erase:
                    print('+++++ Barang yang ingin Dihapus +++++\n')
                    print('nomorID | Jenis\t| Nama  \t| Stock\t| Harga')
                    print('{}\t|{}\t| {}  \t| {}\t| {}'.format(listGudang[i]['nomorID'],listGudang[i]['jenis'],listGudang[i]['nama'],listGudang[i]['stock'],listGudang[i]['harga']))
                    while True :
                        confirm = input('\nApakah anda ingin lanjut menghapus data barang? (Y/N)')
                        if confirm == 'Y' :
                            listGudang.pop(i)
                            match -= match
                            break
                        elif confirm == 'N' :
                        
                            menghapusGudang()
                        else:
                            match += 1
                    if match >= len(listGudang):
                        print('\nBarang yang anda cari tidak ada')
                        menghapusGudang()
                    elif match < len(listGudang):
                        print('\nData barang telah dihapus')
                        menghapusGudang()
        elif pilihan4 == '2' :
            print ('\nBarang dengan Nomor ID yang dimaksud tidak tersedia')
            gudang()

# MENU EXIT PROGRAM
def keluarGudang() :
    pilihan5 = input('Apakah anda yakin (Y/N)? ')
    while True :
        if pilihan5 !='Y' and pilihan5 !='N' :
                print('Pilihan yang anda masukkan salah, pilih (Y/N)\n')
                pilihan55 = input('Apakah anda yakin (Y/N)? ')
                if pilihan55 == 'N':
                    print('\nAnda kembali ke menu utama\n')
                    gudang()
                elif pilihan55 == 'Y':
                        print('==================================   HAVE A GREAT DAY!   ==================================\n')
                        quit()
        if pilihan5 == 'N':
            print('\nAnda kembali ke menu utama\n')
            gudang()
        elif pilihan5 == 'Y':
            print('==================================   HAVE A GREAT DAY!   ==================================\n')
            quit()

# MENU UTAMA
def gudang():
    while True :
        pilihanMenu = input('''
==========   Gudang Konveksi Cabang Serpong   ==========

            Pilihan Menu :
            1. Menampilkan Stock Gudang
            2. Menambah Barang
            3. Mengubah Barang
            4. Menghapus Barang
            5. Exit Program
            Masukkan angka Menu yang ingin dijalankan : ''')

        if(pilihanMenu == '1') :
            menampilkanGudang()
        elif(pilihanMenu == '2') :
            menambahGudang()
        elif(pilihanMenu == '3') :
            mengubahGudang() 
        elif(pilihanMenu == '4') :
            menghapusGudang()
        elif(pilihanMenu == '5') :
            keluarGudang()
        else:
            print('Pilihan yang anda masukkan salah. Pilih [1-5]')
gudang()