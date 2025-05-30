### 📄 **Deskripsi Singkat (untuk GitHub Repository)**

> Proyek ini adalah program Python sederhana untuk mengelola dan menganalisis data hasil panen dari beberapa kebun. Program ini mencetak hasil panen setiap lokasi, menampilkan informasi spesifik, menghitung total hasil panen padi dan kedelai per lokasi, serta memberikan peringatan jika suatu kebun melebihi ambang batas hasil tertentu yang dapat menandakan perlunya perhatian khusus.

---

# 📊 Analisis Data Hasil Panen

Proyek Python ini digunakan untuk menyimpan, menampilkan, dan menganalisis data hasil panen dari lima lokasi kebun. Data yang dianalisis meliputi tiga jenis tanaman: padi, jagung, dan kedelai.
````markdown
## 🔧 Fitur

- Menampilkan hasil panen dari tiap lokasi.
- Mengakses data spesifik seperti jumlah jagung di lokasi 2 dan nama lokasi ke-3.
- Menghitung total hasil panen padi dan kedelai dari setiap lokasi.
- Memberikan peringatan untuk lokasi yang hasil padinya > 1300 atau jagungnya > 800.

## 📁 Struktur Data

Data disimpan dalam dictionary Python bersarang, dengan struktur sebagai berikut:

```python
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    ...
}
````

## ▶️ Cara Menjalankan

1. Pastikan Anda sudah menginstal Python (versi 3.x).
2. Simpan kode pada file Python, misalnya `panen.py`.
3. Jalankan dengan perintah:

```bash
python panen.py
```

## 💡 Contoh Output

```
Lokasi: Kebun A
Hasil Panen:
  Padi: 1200
  Jagung: 800
  Kedelai: 500
------------------------------
...
Jumlah hasil panen jagung dari lokasi 2:  900
Nama lokasi dari lokasi3:  Kebun C
Lokasi : Kebun A dalam kondisi baik.
Lokasi : Kebun B memerlukan perhatian khusus.
...
```



---
