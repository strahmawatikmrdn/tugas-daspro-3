hari_kerja = 4
hari_kerja_perbulan = 16
gaji = 1000000000
gaji_lembur_perhari = 20000000

total_gaji = (hari_kerja/hari_kerja_perbulan)*gaji+gaji_lembur_perhari
total_gaji = int(total_gaji)
formt = f"{total_gaji:,}"
print ("Rp", formt)