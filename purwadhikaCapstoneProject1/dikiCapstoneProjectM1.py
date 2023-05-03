# CAPSTONE PROJECT MODUL 1
# by DIKI RENANDA
# MEMBUAT APLIKASI DENGAN BASIS FITUR CRUD
# DATA KARYAWAN DALAM SEBUAH PERUSAHAAN


### IMPORT LIST

import random as rd
import datetime as dt
import string as st
import os


### DATA STARTER

emplData = {
    1 : {'NIK' : '2397000010',
             'Nama' : 'Faisal Akbar',
             'DOB' : '1997-12-08',
             'Married' : False,
             'ContractType' : 1,
             'Grade' : '2A',
             'Contact' : 'faisal.akbar@karyawan.com'},
    22 : {'NIK' : '2298000221',
             'Nama' : 'Ahmad Fahri',
             'DOB' : '1998-11-07',
             'Married' : False,
             'ContractType' : 1,
             'Grade' : '1C',
             'Contact' : 'ahmad.fahri@karyawan.com'},
    333 : {'NIK' : '0478003335',
             'Nama' : 'Desta Era',
             'DOB' : '1978-05-11',
             'Married' : True,
             'ContractType' : 0,
             'Grade' : '4A',
             'Contact' : 'desta.era@karyawan.com'},
    4444 : {'NIK' : '0070044444',
             'Nama' : 'Ahmad Ali',
             'DOB' : '1970-01-09',
             'Married' : True,
             'ContractType' : 0,
             'Grade' : '4C',
             'Contact' : 'ahmad.ali@karyawan.com'},
    55555 : {'NIK' : '1994555550',
             'Nama' : 'Diki Renanda',
             'DOB' : '1994-08-12',
             'Married' : False,
             'ContractType' : 0,
             'Grade' : '3B',
             'Contact' : 'diki.renanda@karyawan.com'},
}

posData = {
    '00000001' : {'posName' : 'Head Officer Pajak',
                  'level' : 'T2',
                  'Divisi' : 'Keuangan',
                  'emplID' : 1},
    '22222200' : {'posName' : 'Officer Personalia',
                  'level' : 'T1',
                  'Divisi' : 'Personalia',
                  'emplID' : 22},
    '00333000' : {'posName' : 'Direktur Keuangan',
                  'level' : 'T4',
                  'Divisi' : 'Keuangan',
                  'emplID' : 333},
    '44445555' : {'posName' : 'Direktur Personalia',
                  'level' : 'T4',
                  'Divisi' : 'Personalia',
                  'emplID' : 4444},
    '15555522' : {'posName' : 'Kepala Kreatif 1',
                  'level' : 'T3',
                  'Divisi' : 'Kreatif',
                  'emplID' : None},
    '12323434' : {'posName' : 'Officer Kreatif',
                  'level' : 'T1',
                  'Divisi' : 'Kreatif',
                  'emplID' : None},
    '43232121' : {'posName' : 'Lead Kreatif',
                  'level' : 'T2',
                  'Divisi' : 'Kreatif',
                  'emplID' : None},
    '11199283' : {'posName' : 'Officer Sosial Media',
                  'level' : 'T1',
                  'Divisi' : 'Kreatif',
                  'emplID' : None},
}

emplGrade = ['1A','1B','1C','2A','2B','2C','3A','3B','3C','4A','4B','4C']
posLevel = ['T1','T2','T3','T4']

menuList = {
    'mainMenu' : {
        1 : 'Tampilkan daftar Karyawan',
        2 : 'Tampilkan daftar Posisi',
        3 : 'Menambahkan Karyawan',
        4 : 'Update Data Karyawan',
        5 : 'Menghapus Baris Data Karyawan',
        6 : 'Memindahkan Karyawan',
        0 : 'Exit Program'},
    'subMenu1' : {
        1 : 'Menampilkan seluruh data',
        2 : 'Melakukan pencarian data',
        0 : 'Kembali ke menu sebelumnya'}
}

dateFormat = '%Y-%m-%d'
todayIs = dt.date.today()


### FUNCTION LIST


## FUNCTION FOR SYSTEM

def clearScreenView() :
    if os.name == 'posix' : # for macos / linux
        os.system('clear')
    if os.name == 'nt' : # for windows
        os.system('cls')


## FUNCTION FOR TRANSLATING

def dobTahun(dob) :
    if dob != '' :
        dobList = [int(i) for i in dob.split('-')]
        if int(dobList[1]) > todayIs.month :
            dobYear = str((todayIs.year - dobList[0]) -  1) + ' Thn'
        elif int(dobList[1]) == todayIs.month :
            if int(dobList[2]) > todayIs.day :
                dobYear = str((todayIs.year - dobList[0]) -  1) + ' Thn'
            else :
                dobYear = str(todayIs.year - dobList[0]) + ' Thn'
        else :
            dobYear = str(todayIs.year - dobList[0]) + ' Thn'
    else :
        dobYear = ''
    return dobYear

def maritalStatus(value) :
    if value == '' :
        status = ''
    else :
        if value :
            status = 'Menikah'
        else :
            status = 'Belum Menikah'
    return status

def contractStatus(value) :
    if value == 0 :
        status = 'Tetap'
    elif value == 1 :
        status = 'Kontrak'
    elif value == '' :
        status = ''
    return status

def nikToEmplID(nik) :
    for i in emplData :
        if emplData[i]['NIK'] == nik :
            return i

def generateKey(howmany,kemana) :
    while True :
        berapaDigit = int('9' * howmany)
        keyRandom = rd.randint(1,berapaDigit)
        if keyRandom not in kemana :
            break
    return keyRandom

def generateNIK(dob,key) :
    if dob == '' :
        randomNIK = str(todayIs.year)[-2:] + '00' + str(key).zfill(5) + str(rd.randint(1,9))
    else :
        randomNIK = str(todayIs.year)[-2:] + dob[2:4] + str(key).zfill(5) + str(rd.randint(1,9))
    return randomNIK

def generateEmail(name) :
    cleanName = ''.join(i for i in name if i not in st.punctuation)
    nameList = cleanName.lower().split()
    eMail = '.'.join(nameList[:2]) + '@karyawan.com'
    return eMail


## FUNCTION FOR MATCHING

def emplPos(source,emplKey) :
    for i in source :
        if emplKey == source[i]['emplID'] :
            return source[i]['posName']
    else :
        return '-Unassigned-'

def posEmpl(source,posKey) :
    if source[posKey]['emplID'] != None :
        emplReturn = emplData[source[posKey]['emplID']]['NIK'] + ' - ' + emplData[source[posKey]['emplID']]['Nama']
    else :
        emplReturn = '-Vacant Position-'
    return emplReturn


##  VALIDATION

# FUNCTION FOR MESSAGES

def showMessages(tipe) :
    if tipe == 0 :
        print('\nBerhasil!\n')
    elif tipe == 1 :
        print('\nMasukan hanya angka\n')
    elif tipe == 2 :
        print('\nMasukan sesuai pilihan yang tersedia\n')
    elif tipe == 3 :
        print('\nMasukan hanya Y atau N\n')
    elif tipe == 4 :
        print('\nData sudah ada sebelumnya\n')
    elif tipe == 5 :
        print('\nMasukan hanya huruf saja\n')
    elif tipe == 6 :
        print('\nMasukan antara 3 - 40 Karakter\n')
    elif tipe == 7 :
        print('\nMasukan sesuai format tanggal YYYY-MM-DD\n')
    elif tipe == 8 :
        print('\nMasukan sesuai format dan rentang grade\n')
    elif tipe == 9 :
        print('\nNIK harus 10 digit!\n')
    elif tipe == 10 :
        print('\nNIK belum ada!\n')
    elif tipe == 11 :
        print('\nFormat email harus berisi username (hanya dengan pemisah titik)\ndan berdomain "@karyawan.com"\ncontoh: "abc.de@karyawan.com"\n')
    elif tipe == 12 :
        print('\nAnda telah membatalkan penghapusan pegawai\n')
    elif tipe == 13 :
        print('\nPosisi ID harus 8 digit!\n')
    elif tipe == 14 :
        print('\nPosisi ID belum ada!\n')
    elif tipe == 15 :
        print('\nData tidak bisa kosong!\n')
    elif tipe == 16 :
        print('\nNIK sudah ada!\n')
    elif tipe == 17 :
        print(f'\n{"Data tidak ditemukan":^80}\n')
    elif tipe == 18 :
        print('\nMasukan hanya antara 1 dan 0\n')
    elif tipe == 19 :
        print('\nProgram telah tertutup. Terimakasih\n')

# FUNCTION FOR VALIDATING

def validasi(cekapa,inputnya,rangemin = None,rangemax = None) :
    if cekapa == 1 : # CEK SESUAI RANGE
        if inputnya < rangemin or inputnya > rangemax :
            showMessages(2)
            return False
        else :
            return True
    elif cekapa == 2 : # CEK INPUT Y / N / 0
        if inputnya == '0' :
            return inputnya
        elif inputnya not in ('Y','N') :
            showMessages(3)
            return False
        else :
            return True
    elif cekapa == 3 : # CEK INPUT NIK SUDAH BENAR DAN ADA ATAU BELUM
        if len(inputnya) == 10 :
            for i in emplData :
                if emplData[i]['NIK'] == inputnya :
                    return True
            else :
                return False
        else :
            showMessages(9)
            return False
    elif cekapa == 4 : # CEK APAKAH STRING HANYA HURUF / UNTUK NAMA
        if all(i.isalpha() or i.isspace() or i == "'" for i in inputnya) : # all itu juga semua iterasi true maka dia true. intinya all untuk cek iterasi, tapi di combine dengan or, tetap salah satu.
            return True
        else :
            showMessages(5)
            return False
    elif cekapa == 5 : # CEK APAKAH PANJANG STRING LEBIH DARI 40
        if len(inputnya) <= 40 and len(inputnya) >= 3 :
            return True
        else :
            showMessages(6)
            return False
    elif cekapa == 6 : # CEK DATE FORMAT
        try :
            dt.datetime.strptime(inputnya,dateFormat) # cek pakai striptime (strptime) bandingkan dengan dateFormat = '%Y-%m-%d' module datetime.datetime class
            return True
        except ValueError:
            showMessages(7)
            return False
    elif cekapa == 7 : # CEK GRADE EXIST IN LIST
        if inputnya in emplGrade :
            return True
        else :
            showMessages(8)
            return False
    elif cekapa == 8 : # CEK FORMAT EMAIL
        if inputnya[-13:] == '@karyawan.com' and len(inputnya) > 13 and all(i.isalpha() or i == '.' for i in inputnya[0:-13]) :
            return True
        else :
            showMessages(11)
            return False
    elif cekapa == 9 : # CEK INPUT POSISI ID
        if len(inputnya) == 8 and inputnya.isdigit() :
            for i in posData :
                if inputnya == i :
                    return True
            else :
                showMessages(14)
                return False
        else :
            showMessages(13)
            return False
    elif cekapa == 0 : # CEK KHUSUS ADD / UPDATE DENGAN VALUE KOSONG
        print('Anda yakin memasukan data kosong?\nJika add, value anda akan kosong.\nJika update, value anda akan terhapus.')
        while True :
            confirmZero = input('(Y/N) :').upper()
            if confirmZero in ('Y','N') :
                if confirmZero == 'Y' :
                    return True
                else :
                    showMessages(12)
                    return False
            else :
                showMessages(3)


## FUNCTION FOR CRUD

# FUNCTION FOR PRINTING

def printLimit(value,limit) :
    if len(value) > limit :
        return value[:limit] + '..'
    else :
        return value
    
def printEmplList(source,count,key) :
    print('{:<2} | {:<10} | {:<12} | {:<17} | {:<6} | {:<11} | {:<7} | {:<5} | {}'.format(count, source[key]['NIK'], printLimit(source[key]['Nama'],10), printLimit(emplPos(posData,key),15), dobTahun(source[key]['DOB']), printLimit(maritalStatus(source[key]['Married']),9), contractStatus(source[key]['ContractType']), source[key]['Grade'], source[key]['Contact']))

def printEmpl(source,search = None) :
    print('{}\n\n{:<2} | {:<10} | {:<12} | {:<17} | {:<6} | {:<11} | {:<7} | {:<5} | {}'.format('Daftar Karyawan :', 'No', 'NIK', 'Nama', 'Posisi', 'Umur', 'Status', 'Kontrak', 'Grade', 'Email'))
    print('-' * 125)
    k = 0
    for i in source :
        if search == None :
            k += 1
            printEmplList(source,k,i)
        else :
            if search in source[i]['Nama'].lower() :
                k += 1
                printEmplList(source,k,i)
    if k == 0 :
        showMessages(17)

def printPosList(source,count,key) :
    print('{:<2} | {:<9} | {:<20} | {:<5} | {:<11} | {}'.format(count, key, printLimit(source[key]['posName'],18), source[key]['level'], source[key]['Divisi'], posEmpl(posData,key)))

def printPos(source,search = None) :
    print('{}\n\n{:<2} | {:<9} | {:<20} | {:<5} | {:<11} | {}'.format('Daftar Posisi :', 'No', 'id Posisi', 'Nama Posisi', 'Level', 'Divisi', 'Pegawai'))
    print('-' * 80)
    k = 0
    for i in source :
        if search == None :
            k += 1
            printPosList(source,k,i)
        else :
            if search in source[i]['posName'].lower() :
                k += 1
                printPosList(source,k,i)
    if k == 0 :
        showMessages(17)

# FUNCTION FOR VIEWING / READING

def viewEmpl() :
    print('Anda dapat melihat data Employee dengan cara :')
    for i in menuList['subMenu1'] :
        print(f"{i}. {menuList['subMenu1'][i]}")
    subMenuInput = int(input('Masukan cara yang diinginkan :'))
    if subMenuInput == 1 :
        printEmpl(emplData)
    elif subMenuInput == 2 :
        namaSearchInput = input('Masukan nama pegawai yang hendak dicari :').lower()
        printEmpl(emplData,namaSearchInput)
    return subMenuInput

def viewPos() :
    print('Anda dapat melihat data Posisi dengan cara :')
    for i in menuList['subMenu1'] :
        print(f"{i}. {menuList['subMenu1'][i]}")
    subMenuInput = int(input('Masukan cara yang diinginkan :'))
    if subMenuInput == 1 :
        printPos(posData)
    elif subMenuInput == 2 :
        namaSearchInput = input('Masukan nama posisi yang hendak dicari :').lower()
        printPos(posData,namaSearchInput)
    return subMenuInput

def promptToSee(what) :
    if what == 'empl' :
        while True :
            subMenuInput = input('Apakah anda mau melihat daftar karyawan terlebih dahulu?\n(Y/N) atau 0 untuk kembali ke menu sebelumnya :').upper()
            if validasi(2,subMenuInput) :
                break
        if subMenuInput == 'Y' :
            while True :
                try :
                    subMenuInput = viewEmpl()
                    if validasi(1,subMenuInput,0,len(menuList['subMenu1']) - 1) :
                        break
                except ValueError :
                    showMessages(1)
    elif what == 'pos' :
        while True :
            subMenuInput = input('Apakah anda mau melihat daftar posisi terlebih dahulu?\n(Y/N) atau 0 untuk kembali ke menu sebelumnya :').upper()
            if validasi(2,subMenuInput) :
                break
        if subMenuInput == 'Y' :
            while True :
                try :
                    subMenuInput = viewPos()
                    if validasi(1,subMenuInput,0,len(menuList['subMenu1']) - 1) :
                        break
                except ValueError :
                    showMessages(1)
    if subMenuInput == '0' :
        return int(subMenuInput)
    else :
        return subMenuInput

def getDetail(source,key) :
    dataDetail = source[key].values()
    return dataDetail

def backConfirm() :
    while True :
        confirmInput = input('\nAnda ingin kembali ke menu utama? (Y/N) ').upper() # input konfirmasi back
        if validasi(2,confirmInput) :
            if confirmInput == '0' :
                showMessages(3)
                continue
            else :
                break
    return confirmInput

# FUNCTION FOR CREATING or UPDATING

def updateDataEmpl(tipe,emplid,nik,nama,dob,married,contract,grade,contact) :
    updateValues = [nik,nama,dob,married,contract,grade,contact]
    if tipe == 1 :
        emplData[emplid] = {}
    for i,k in zip(next(iter(emplData.values())), updateValues) :
        emplData[emplid][i] = k

def assignEmplPos(posID,posName,level,Divisi,emplID) :
    updateValues = [posName,level,Divisi,emplID]
    for i in posData :
        if posData[i]['emplID'] == emplID :
            posData[i]['emplID'] = None
    posData[posID] = {}
    for i,k in zip(next(iter(posData.values())), updateValues) :
        posData[posID][i] = k



### APPS START



clearScreenView() # agar clean tidak ada command pembuka

while True :
    print('\nSelamat Datang di Employee Management System!\n')
    for i in menuList['mainMenu'] :
        print(f"{i}. {menuList['mainMenu'][i]}")
    while True :
        try :
            menuInput = int(input('\nMasukan menu yang diinginkan :')) # Input master menu
            if validasi(1,menuInput,0,len(menuList['mainMenu']) - 1) :
                break
        except ValueError :
            showMessages(1)

    if menuInput == 1 : # Menampilkan data Karyawan
        while True :
            while True :
                try :
                    subMenuInput = viewEmpl() # Input sub menu pilihan
                    if validasi(1,subMenuInput,0,len(menuList['subMenu1']) - 1) :
                        break
                except ValueError :
                    showMessages(1)
            if subMenuInput == 0 :
                clearScreenView()
                break
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 2 : # Menampilkan data Posisi
        while True :
            while True :
                try :
                    subMenuInput = viewPos() # input sub menu pilihan
                    if validasi(1,subMenuInput,0,len(menuList['subMenu1']) - 1) :
                        break
                except ValueError :
                    showMessages(1)
            if subMenuInput == 0 :
                clearScreenView()
                break
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 3 : # Menambahkan data karyawan
        while True :
            print('Anda akan menambah data Karyawan :')
            subMenuInput = promptToSee('empl') # input prompt untuk cek lihat empl
            if subMenuInput == 0 :
                clearScreenView()
                break
            print('Anda dapat mengosongkan value sementara jika belum ada dengan cara langsung Enter.')
            while True :
                newNameInput = input('Masukan Nama untuk karyawan baru :').title() # input nama baru
                if newNameInput == '' :
                    if validasi(0,newNameInput) :
                        break
                else :
                    if validasi(4,newNameInput) and validasi(5,newNameInput) :
                        break
            while True :
                newDOBinput = input('Masukan Tanggal Lahir untuk karyawan baru (yyyy-mm-dd) :') # input dob baru
                if newDOBinput == '' :
                    if validasi(0,newDOBinput) :
                        break
                else :
                    if validasi(6,newDOBinput) :
                        break
            while True :
                newMarriedInput = input('Masukan status pernikahan untuk karyawan baru (1 = Menikah / 0 = Belum Menikah):') # input status baru
                if newMarriedInput == '' :
                    if validasi(0,newMarriedInput) :
                        break
                else :
                    try :
                        if validasi(1,int(newMarriedInput),0,1) :
                            newMarriedInput = bool(int(newMarriedInput))
                            break
                    except ValueError :
                        showMessages(1)
            while True :
                newContractInput = input('Masukan Tipe Kontrak untuk karyawan baru (1 = Kontrak / 0 = Tetap) :') # input status kontrak
                if newContractInput == '' :
                    if validasi(0,newContractInput) :
                        break
                else :
                    try :
                        if validasi(1,int(newContractInput),0,1) :
                            newContractInput = int(newContractInput)
                            break
                    except ValueError :
                        showMessages(1)
            while True :
                newGradeInput = input('Masukan Grade untuk karyawan baru :').upper() # input grade baru
                if newGradeInput == '' :
                    if validasi(0,newGradeInput) :
                        break
                else :
                    if validasi(7,newGradeInput) :
                        break
            newKeyEmpl = generateKey(5,emplData) # genrate employee Key
            newNIKempl = generateNIK(newDOBinput,newKeyEmpl) # genereate employee NIK based on Key DOB EntryYear
            if newNameInput == '' :
                newEmail = '' # tidak generate email jika nama kosong
            else :
                newEmail = generateEmail(newNameInput) # generate email based on name
            updateDataEmpl(1,newKeyEmpl,newNIKempl,newNameInput,newDOBinput,newMarriedInput,newContractInput,newGradeInput,newEmail) # proses add
            printEmpl(emplData)
            showMessages(0)
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 4 : # Mengupdate data karyawan
        while True :
            print('Anda akan mengupdate data karyawan')
            subMenuInput = promptToSee('empl') # prompt untuk lihat empl
            if subMenuInput == 0 :
                clearScreenView()
                break
            while True :
                nikToUpdateInput = input('Masukan NIK pegawai yang hendak di update :') # input NIK yang mau di Update
                if validasi(3,nikToUpdateInput) :
                    break
                else :
                    showMessages(10)
            while True :
                try :
                    whatToUpdateInput = int(input('Masukan nama kolom yang hendak di update\n1 = Nama\n2 = Tanggal Lahir\n3 = Status Pernikahan\n4 = Kontrak\n5 = Grade\n6 = Email\n:')) # input apa yang mau di update
                    if validasi(1,whatToUpdateInput,1,7) :
                        break
                except ValueError :
                    showMessages(1)
            while True :
                updateValueInput = input('Masukan value data untuk update\nLangsung enter jika hendak menghapus value :') # input value nya yang di update
                if updateValueInput == '' :
                    if validasi(0,updateValueInput) :
                        pass
                    else :
                        break
                else :
                    if whatToUpdateInput == 1 : # JIKA NAMA
                        if validasi(4,updateValueInput) and validasi(5,updateValueInput) :
                            updateValueInput = updateValueInput.title()
                        else :
                            continue
                    elif whatToUpdateInput == 2 : # JIKA DOB
                        if validasi(6,updateValueInput) :
                            pass
                        else :
                            continue
                    elif whatToUpdateInput == 3 : # JIKA STATUS
                        try :
                            if validasi(1,int(updateValueInput),0,1) :
                                updateValueInput = bool(int(updateValueInput))
                            else :
                                showMessages(18)
                                continue
                        except ValueError :
                            showMessages(1)
                            continue
                    elif whatToUpdateInput == 4 : # JIKA KONTRAK
                        try :
                            if validasi(1,int(updateValueInput),0,1) :
                                updateValueInput = int(updateValueInput)
                            else :
                                showMessages(18)
                                continue
                        except ValueError :
                            showMessages(1)
                            continue
                    elif whatToUpdateInput == 5 : # JIKA GRADE
                        updateValueInput = updateValueInput.upper()
                        if validasi(7,updateValueInput) :
                            pass
                        else :
                            continue
                    elif whatToUpdateInput == 6 : # JIKA EMAIL
                        if validasi(8,updateValueInput) :
                            pass
                        else :
                            continue
                emplDetail = list(getDetail(emplData, nikToEmplID(nikToUpdateInput))) # proses update start
                emplDetail[whatToUpdateInput] = updateValueInput
                updateDataEmpl(0,nikToEmplID(nikToUpdateInput), emplDetail[0], emplDetail[1], emplDetail[2], emplDetail[3], emplDetail[4], emplDetail[5], emplDetail[6])
                printEmpl(emplData)
                showMessages(0)
                break
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 5 : # Menghapus data karyawan
        while True :
            print('Anda akan menghapus data baris Karyawan')
            subMenuInput = promptToSee('empl') # Input cek karyawan lihat
            if subMenuInput == 0 :
                clearScreenView()
                break
            while True :
                delKeyInput = input('Masukan NIK pegawai yang hendak dihapus\n(0 jika batal dan hendak kembali):') # NIK yang mau di delete
                if delKeyInput != '0' :
                    if validasi(3,delKeyInput) :
                        break
                    else :
                        showMessages(10)
                else :
                    break
            if delKeyInput != '0' :
                while True :
                    promptToDelete = input(f'Apakah anda yakin untuk menghapus pegawai dengan NIK {delKeyInput} ?\nPerubahan tidak dapat dikembalikan.\n(Y/N) :').upper() # confirm delete
                    if validasi(2,promptToDelete) :
                        if promptToDelete == '0' :
                            showMessages(3)
                            continue
                        else :
                            break
                if promptToDelete == 'Y' : # jika ya, delete
                    for i in posData :
                        if posData[i]['emplID'] == nikToEmplID(delKeyInput) :
                            posData[i]['emplID'] = None # unassign pegawai dulu dari posisinya
                    del emplData[nikToEmplID(delKeyInput)] # baru di delete agar tidak missing reference
                    printEmpl(emplData)
                    showMessages(0)
                else :
                    showMessages(12)
            else :
                clearScreenView()
                break
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 6 : # Memindahkan posisi karyawan
        while True :
            print('Anda akan melakukan perpindahan karyawan terhadap posisinya :')
            subMenuInput = promptToSee('empl') # input mau lihat daftar employee dulu atau tidak
            if subMenuInput == 0 :
                clearScreenView()
                break
            subMenuInput = promptToSee('pos') # input mau lihat daftar posisi dulu atau tidak
            if subMenuInput == 0 :
                clearScreenView()
                break
            while True :
                targetEmplInput = input('Masukan NIK pegawai yang hendak dipindahkan :') # Input NIK yang mau dipindah
                if validasi(3,targetEmplInput) :
                    break
                else :
                    showMessages(10)
            print('Perhatian: Jika anda memindahkan pegawai ke posisi yang berisi incumbent, maka incumbent akan menjadi -Unassigned-')
            while True :
                targetPosInput = input('Masukan posisi id tujuan untuk diisi pegawai tersebut :') # Input pos ID tujuan
                if validasi(9,targetPosInput) :
                    break
            posDetail =  list(getDetail(posData, targetPosInput)) # proses assign start
            posDetail[3] = nikToEmplID(targetEmplInput)
            assignEmplPos(targetPosInput,posDetail[0],posDetail[1],posDetail[2],posDetail[3])
            showMessages(0)
            confirmInput = backConfirm() # input konfirmasi back
            if confirmInput == 'Y' :
                clearScreenView()
                break

    elif menuInput == 0 : # Exit Program
        while True :
            confirmInput = input('Anda yakin untuk menutup aplikasi? (Y/N) ').upper() # input konfirmasi exit
            if validasi(2,confirmInput) :
                if confirmInput == '0' :
                    showMessages(3)
                    continue
                break
        if confirmInput == 'Y' :
            clearScreenView()
            showMessages(19)
            break # end of program
        else :
            clearScreenView() # back to menu
