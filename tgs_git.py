data_panen ={
    'lokasi1':{
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    },
}

#No. 1
print (data_panen)

#No. 2
print (f"Jumlah hasil panen jagung dari lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

#No. 3
print (data_panen['lokasi3']['nama_lokasi'])

#No. 4 dan 5
jumlah_padi = {}
jumlah_kedelai = {}
for i,j in data_panen.items():
    jumlah_padi[i] = j['hasil_panen']['padi']
    jumlah_kedelai[i] = j['hasil_panen']['kedelai']
print(f"Jumlah Hasil Panen Padi: {jumlah_padi}")
print(f"Jumlah Hasil Panen Kedelai: {jumlah_kedelai}")

#No. 6
jumlah_jagung = {}
for i,j in data_panen.items():
    jumlah_padi[i] = j['hasil_panen']['jagung']

for key, value in data_panen.items():
    nama_lokasi = value['nama_lokasi']
    padi = value['hasil_panen']['padi']
    jagung = value['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"{nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"{nama_lokasi} dalam kondisi baik.")
    
    #ubahbaruasdasdsad

    #ubahmain
    #blabalbalbala