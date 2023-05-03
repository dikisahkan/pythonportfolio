# TEBAK KATA EDISI ULANG TAHUN

# Import List
import os

# STARTING DATA
# kataKunci = input('Masukan kata kunci :')
jawabanJalan = []
posisiTepat = []
posisiBeda = []
qwertyUiop = {
    'Line1' : ['Q','W','E','R','T','Y','U','I','O','P'],
    'Line2' : ['A','S','D','F','G','H','J','K','L'],
    'Line3' : ['Z','X','C','V','B','N','M']
}

# Function List
def clearScreen() :
    if os.name == 'posix' : # for macos / linux
        os.system('clear')
    if os.name == 'nt' : # for windows
        os.system('cls')

def showMessage(nomor) : # fungsi menampilkan message
    if nomor == 0 :
        print(f'\nSelamat tebakan anda Benar!\nJawabannya : {kataKunci}\n')
    elif nomor == 1 :
        print(f'\nOops! Harus {jmlHuruf} huruf ya!\n')
    elif nomor == 2 :
        print('\nIni permainan kata :) Masukan hanya kata ya!\n')
    elif nomor == 3 :
        print('\nMasukan jumlah dalam angka yah..\n')
    elif nomor == 9 :
        print(f'\nAnda gagal menebak :(\nJawabannya : {kataKunci}\n')

def validasi(apa,cekapa) : # fungsi validasi
    if cekapa == 1 : # validasi jumlah karakter
        if len(apa) != jmlHuruf :
            showMessage(1)
            return False
        else :
            return True
    elif cekapa == 2 : # validasi apakah ini kata atau bukan
        if apa.isalpha() :
            return True
        else :
            showMessage(2)
            return False

def pencocokan(inputan) : # untuk komparasi hasil tebakan dengan jawaban
    kataKunciList = list(kataKunci.upper()) # dibuat huruf besar agar tidak ngaruh
    inputanList = list(inputan.upper()) # dibuat hurud besar agar tidak ngaruh
    for i,k in zip(range(len(inputanList)), inputanList) : # loop antara berapa index (diambil dari range len) dan putaran value nya (untuk di store)
        if k in kataKunciList : # di cek apakah tebakan ada dalam jawaban
            if inputanList[i] == kataKunciList[i] : # di cek dulu apakah lokasinya sama
               posisiTepat[i] = k # jika hasil tepat sasaran
               if posisiTepat.count(k) == kataKunciList.count(k) : # cek apakah semua huruf duplicate sudah kena semua baik hanya 1 atau lebih
                    for m in qwertyUiop : # m adalah line di keyboard nya karena pakai dict
                        if k.upper() in qwertyUiop[m] : # kalau ada di baris itu...
                            urutan = qwertyUiop[m].index(k.upper())
                            qwertyUiop[m][urutan] = ' ' # di delete jika sudah masuk tepat posisi
            else :
                if kataKunciList.count(k) != posisiTepat.count(k) :
                    posisiBeda[i] = k # jika hasil benar tapi salah posisi
        elif k not in kataKunciList :
             for m in qwertyUiop : # m adalah line di keyboard nya karena pakai dict
                if k.upper() in qwertyUiop[m] : # kalau ada di baris itu...
                    urutan = qwertyUiop[m].index(k.upper())
                    qwertyUiop[m][urutan] = ' ' # di delete jika sudah masuk tepat posisi
    for i,k in zip(range(len(inputanList)), inputanList) : # di loop untuk menghapus selisih yang berlebihan di posisiBeda
        if posisiBeda.count(k) + posisiTepat.count(k) > kataKunciList.count(k) : # cek dulu apakah berlebih
            for m in range((posisiBeda.count(k) + posisiTepat.count(k)) - kataKunciList.count(k)) : # akan ngeloop sesuai selisih yang tak perlu
                urutan = posisiBeda.index(k) # cari index nya yang berlebih
                posisiBeda[urutan] = '' # hapus yang berlebihnya
    return inputanList , posisiTepat , posisiBeda , qwertyUiop


# APPS START
while True :
    kataKunci = input('\nMasukan kata kunci rahasia : ')
    if validasi(kataKunci, 2) :
        break

jmlHuruf = len(kataKunci)
while True :
    try :
        tryChance = int(input('Masukan jumlah percobaan : '))
        break
    except :
        showMessage(3)
clearScreen()

print(f'Selamat datang di Tebak Kata!\nJumlah percobaan : {tryChance}\nSelamat menebak!\n')
for i in range(jmlHuruf) : # di create berdasarkan jumlah kata nya.
    jawabanJalan.append('')
    posisiTepat.append('')
    posisiBeda.append('')

for i in range(tryChance) :
    while True :
        tebakanInput = input(f'Masukan {jmlHuruf} huruf (Percobaan {i+1}):')
        if validasi (tebakanInput, 2) and validasi(tebakanInput, 1) :
            break
    tempKata = pencocokan(tebakanInput)
    cetakHasil = ''
    for i in range(3) :
        for k in range(jmlHuruf) :
            cetakHasil += '| {:<3} '.format(tempKata[i][k])
        if i == 0 :
            cetakHasil += '| <<< Jawaban kamu\n'
        elif i == 1 :
            cetakHasil += '| <<< Tepat posisi\n'
        elif i == 2 :
            cetakHasil += '| <<< Beda posisi\n'
    print(cetakHasil)
    posisiTepat = [] # di reset lagi
    posisiBeda = [] # di reset lagi
    for i in range(jmlHuruf) : # untuk di create ulang lagi kosongan
        posisiTepat.append('')
        posisiBeda.append('')
    for i in qwertyUiop :
        print(f'{"  ".join(qwertyUiop[i])}') # loop untuk print keyboard list nya
    if tempKata[0] == tempKata[1] : # kalau berhasil, artinya sudah sama persis tebakan dan jawaban
        showMessage(0)
        break
else:
    showMessage(9) # kalau gagal tebak, artinya loop sesuai jumlah kesempatan / tryChance nya habis