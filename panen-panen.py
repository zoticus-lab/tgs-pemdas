data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"  {hasil.capitalize()}: {jumlah}")
    print("-" * 30)
data
print("Jumlah hasil panen jagung dari lokasi 2:", data_panen['lokasi2']['hasil_panen']['jagung'])
print("-" * 30)
print("Nama lokasi dari lokasi3:", data_panen['lokasi3']['nama_lokasi'])
print("-" * 30)

padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

total_padi = {
    'lokasi1': data_panen['lokasi1']['hasil_panen']['padi'],
    'lokasi2': data_panen['lokasi2']['hasil_panen']['padi'],
    'lokasi3': data_panen['lokasi3']['hasil_panen']['padi'],
    'lokasi4': data_panen['lokasi4']['hasil_panen']['padi'],
    'lokasi5': data_panen['lokasi5']['hasil_panen']['padi']
}

total_kedelai = {
    'lokasi1': data_panen['lokasi1']['hasil_panen']['kedelai'],
    'lokasi2': data_panen['lokasi2']['hasil_panen']['kedelai'],
    'lokasi3': data_panen['lokasi3']['hasil_panen']['kedelai'],
    'lokasi4': data_panen['lokasi4']['hasil_panen']['kedelai'],
    'lokasi5': data_panen['lokasi5']['hasil_panen']['kedelai']
}

for lokasi, data in data_panen.items():
    jumlah_padi = data['hasil_panen']['padi']
    jumlah_jagung = data['hasil_panen']['jagung']

    if jumlah_padi > 1300 or jumlah_jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi : {data['nama_lokasi']} dalam kondisi baik.")