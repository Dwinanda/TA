import pandas as pd
import math

#=======Data Training========
kurs = pd.read_excel(r'D:\Kuliah\Semester8\TA\TA_KoTA305\TA\DataHistoris.xlsx', sheet_name='Kurs Jual Sebelum Covid')
data = pd.DataFrame(kurs, columns = ['Kurs'])

print(data)
row_count = pd.DataFrame(kurs, columns = ['No']).count()
# print(row_count[0])


#Tahapan menentukan Nilai Minimum dna Maksimum
minimal=pd.DataFrame(kurs, columns = ['Kurs']).min().astype(int)
maksimal=pd.DataFrame(kurs, columns = ['Kurs']).max().astype(int)

print('Nilai Minimal dari data historis yaitu: ', minimal[0])
print('Nilai Maksimal dari data historis yaitu: ', maksimal[0])

#Tahapan menentukan Banyak Kelas, Rentang Kelas, dan Interval Kelas
banyak_kelas = 1+(3.3*math.log10(row_count))
banyak_kelas = int(banyak_kelas)
print('Banyak Kelas adalah:', banyak_kelas)

rentang_kelas = maksimal[0] - minimal[0] 

print('Rentang Kelas dari data historis yaitu:', rentang_kelas)

interval_kelas = rentang_kelas/12
interval_kelas = int(interval_kelas)
print('Interval Kelas dari data historis yaitu:', interval_kelas)


#Pembentukan Interval Kelas data historis
for i in range(banyak_kelas):
    k = 1
    i = minimal[0]
for j in range(banyak_kelas):
    j = i + interval_kelas
# while (j < maksimal[0]):
    print(f"Range ke - {k}:", i, ' - ', j)
    j = j + 1
    i = j
    k = k + 1
    
# print(data)
