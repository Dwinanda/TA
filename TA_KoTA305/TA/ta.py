from array import array
from codecs import ignore_errors
from csv import writer
import string
import pandas as pd
import math

#=======Data Training========
kurs = pd.read_excel(r'D:\Kuliah\Semester8\TA\TA_KoTA305\TA\DataHistoris.xlsx', sheet_name='Kurs Jual Sebelum Covid')
data = pd.DataFrame(kurs, columns = ['No', 'Kurs'])
# print(kurs_array)
# pd.set_option("display.max_rows", None)

print(data)
row_count = pd.DataFrame(kurs, columns = ['No']).count()
# print(row_count[0])


#Tahapan menentukan Nilai Minimum dna Maksimum
minimal=pd.DataFrame(kurs, columns = ['Kurs']).min().astype(int)
maksimal=pd.DataFrame(kurs, columns = ['Kurs']).max().astype(int)

# print('Nilai Minimal dari data historis yaitu: ', minimal[0])
# print('Nilai Maksimal dari data historis yaitu: ', maksimal[0])

#Tahapan menentukan Banyak Kelas, Rentang Kelas, dan Interval Kelas
banyak_kelas = 1+(3.3*math.log10(row_count))
banyak_kelas = int(banyak_kelas)
# print('Banyak Kelas adalah:', banyak_kelas)

rentang_kelas = maksimal[0] - minimal[0] 

# print('Rentang Kelas dari data historis yaitu:', rentang_kelas)

interval_kelas = rentang_kelas/12
interval_kelas = int(interval_kelas)
# print('Interval Kelas dari data historis yaitu:', interval_kelas)


#Pembentukan Interval Kelas data historis
kumpulan_kelas = []
kumpulan_fuzzyfikasi = []
nilai_tengah = []
for i in range(banyak_kelas):
    k = 1
    i = minimal[0]
for j in range(banyak_kelas):
    kelas = []
    j = i + interval_kelas
    kelas.append(i)
    kelas.append(j)
    kelas.append(f"A{k}")
    kumpulan_fuzzyfikasi.append(f"A{k}")
    kumpulan_kelas.append(kelas)
    print(kelas)
    nilai = (i + j)/2
    nilai_tengah.append(nilai)
    print(f"Interval Kelas ke - {k}: ", i, ' - ', j, " = " f"A{k}", " = ", nilai)
    j = j + 1
    i = j
    k = k + 1

# print(kumpulan_kelas)
print(kumpulan_fuzzyfikasi)

kumpulan_kurs = []
kurs_array = []
data1 = pd.DataFrame(kurs, columns = ['Kurs'])
print(data1)
# print(data1.values[0][0])

# Loop Penentuan Fuzzyfikasi
fuzzyfikasi = []
for kurs_b4_covid in kurs.values:
    kurs_checked = kurs_b4_covid[2]
    for kelas in kumpulan_kelas:
        if kurs_checked <= kelas[1]:
            data_historis = []
            data_historis.append(kurs_b4_covid[0])
            data_historis.append(kurs_b4_covid[1])
            data_historis.append(kurs_b4_covid[2])
            data_historis.append(kelas[2])
            fuzzyfikasi.append(data_historis)
            # print(str(kurs_checked) + " masuk ke kelas " + kelas[2])            
            break
# Fuzzyfikasi = pd.DataFrame(fuzzyfikasi, columns=['No', 'Tanggal', 'Kurs', 'Fuzzyfikasi'])
# with pd.ExcelWriter('D:\Kuliah\Semester8\TA\TA_KoTA305\TA\DataHistoris.xlsx', mode='a') as writer:
#     FLR.to_excel(writer, sheet_name='Fuzzyfikasi Kurs Jual', index=False)
kurs_array.append(data1)
kumpulan_kurs.append(kurs_array)

# Penentuan FLR
FLR = pd.read_excel(r'D:\Kuliah\Semester8\TA\TA_KoTA305\TA\DataHistoris.xlsx', sheet_name='Fuzzyfikasi Kurs Jual')
FLRData = pd.DataFrame(FLR, columns=['Fuzzyfikasi'])
FLRData_kumpulan = []
for i in range(0, FLRData.size - 1):
    if i+1 <= FLRData.size - 1:
        FLRData_values_kumpulan = []
        if FLRData.values[1][0] == FLRData.values[1][0]:
            # FLRData_values_kumpulan.append(FLRData.values[i][0]), " - ", FLRData.values[i+1][0])
            FLRData_values_kumpulan.append(FLRData.values[i][0])
            FLRData_values_kumpulan.append(FLRData.values[i+1][0])
            FLRData_kumpulan.append(FLRData_values_kumpulan)
# print(kumpulan_fuzzyfikasi[0])

# Penentuan FLRG
perpus = []
for fuzzyfikasi in kumpulan_fuzzyfikasi:
    FLRG = []
    FLRG.append(fuzzyfikasi)
    relasiFLRG = []
    for i in FLRData_kumpulan:
        if fuzzyfikasi == i[0]: 
             relasiFLRG.append(i[1])
    # print(list(dict.fromkeys(relasiFLRG)))
    relasiFLRG = list(dict.fromkeys(relasiFLRG))
    FLRG.append(relasiFLRG)
    perpus.append(FLRG)
print(perpus)

# Menghitung Nilai FLRG
for nilai_fuzzyfikasi in kumpulan_fuzzyfikasi:
    nilai_FLRG = []

# for fuzzyfikasi_b4_covid in FLRData.values:
#     print(fuzzyfikasi_b4_covid)
    # print(fuzzyfikasi_b4_covid[0])
    # print(fuzzyfikasi_checked)
# Fuzzyfikasi = pd.DataFrame(kumpulan_kelas, columns=['Minimal', 'Maksimal', 'Fuzzyfikasi'])

# # Fuzzyfikasi.to_excel(sheet_name= 'Lembar1')
# with pd.ExcelWriter('D:\Kuliah\Semester8\TA\TA_KoTA305\TA\DataHistoris.xlsx', mode='a') as writer:
#     Fuzzyfikasi.to_excel(writer, sheet_name='apaaja')

# print(Fuzzyfikasi)

# print(data)
