data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

print("No.1")
for z, q in data_panen.items():
        print(f"Lokasi: {q['nama_lokasi']}")
print("hasil panen:")
for tanaman, jumlah in q['hasil_panen'].items():
        print(f"  - {tanaman}: {jumlah}")          
print("\n")

print("No.2")
jagung = (data_panen['lokasi2']['hasil_panen']['jagung'])
print(f"Jumlah Hasil Panen Jagung di Lokasi 2 adalah: {jagung}")
print("\n")

print("No.3")
lok3 = (data_panen['lokasi3']['nama_lokasi'])
print(f"Nama lokasi3 adalah: {lok3}")
print("\n")

print("No.4")
for z, q in data_panen.items():
    p_padi = q['hasil_panen']['padi']
    p_kedelai = q['hasil_panen']['kedelai']
    
    print(z)
    print(f"jumlah hasil panen padi: {p_padi}")
    print(f"jumlah hasil panen kedelai: {p_kedelai} \n")
print("\n")

print("No.5")
padi_a = (data_panen['lokasi1']['hasil_panen']['padi'])
kedelai_a = (data_panen['lokasi1']['hasil_panen']['kedelai'])
padi_b = (data_panen['lokasi2']['hasil_panen']['padi'])
kedelai_b = (data_panen['lokasi2']['hasil_panen']['kedelai'])
padi_c = (data_panen['lokasi3']['hasil_panen']['padi'])
kedelai_c = (data_panen['lokasi3']['hasil_panen']['kedelai'])
padi_d = (data_panen['lokasi4']['hasil_panen']['padi'])
kedelai_d = (data_panen['lokasi4']['hasil_panen']['kedelai'])
padi_e = (data_panen['lokasi5']['hasil_panen']['padi'])
kedelai_e = (data_panen['lokasi5']['hasil_panen']['kedelai'])

print(f"jumlah hasil panen padi lokasi 1 : {padi_a}")
print(f"jumlah hasil panen kedelai lokasi 1 : {kedelai_a} \n")
print(f"jumlah hasil panen padi lokasi 2 : {padi_b}")
print(f"jumlah hasil panen kedelai lokasi 2 : {kedelai_b} \n")
print(f"jumlah hasil panen padi lokasi 3 : {padi_c}")
print(f"jumlah hasil panen kedelai lokasi 3 : {kedelai_c}\n")
print(f"jumlah hasil panen padi lokasi 4 : {padi_d}")
print(f"jumlah hasil panen kedelai lokasi 4 : {kedelai_d} \n")
print(f"jumlah hasil panen padi lokasi 5 : {padi_e}")
print(f"jumlah hasil panen kedelai lokasi 5 : {kedelai_e}")
print("\n")

print("No.6")
for z, q in data_panen.items():
    p_padi = q['hasil_panen']['padi']
    p_jagung = q['hasil_panen']['jagung']
    
    if p_jagung > 1300 or p_jagung > 800:
        print(f"{z} Memerlukan Perhatian Khusus")
    else :
        print(f"{z} Kondisi Baik")
print("\n")
       
       
print("ini adalah baris baru")
