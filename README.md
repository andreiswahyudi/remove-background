## Background Remover

Alat otomatisasi berbasis Python yang kuat untuk menghapus latar belakang foto secara massal melalui antarmuka browser lokal yang sederhana dan efisien.

## Fitur

* **🖼️ Batch Processing**: Unggah dan proses hingga 100 foto sekaligus dalam satu sesi.
* **🔒 Privasi Lokal**: Semua proses dilakukan di mesin Anda. Tidak ada data atau foto yang dikirim ke server eksternal.
* **🚀 Cepat & Otomatis**: Menghapus latar belakang secara otomatis dan mengonversi hasil ke format PNG transparan.
* **📦 Ekspor ZIP**: Mengemas semua hasil pemrosesan ke dalam satu file ZIP untuk pengunduhan yang praktis.
* **🌐 Browser Based**: Menggunakan Streamlit untuk antarmuka yang ramah pengguna dan mudah diakses via browser.

## Prasyarat

* **Python**: Proyek ini menggunakan [Python 3.10+](https://python.org).
* **C++ Redistributable**: Diperlukan untuk mendukung pustaka pemrosesan gambar pada sistem Windows.

## Instalasi

1. Clone repositori:
```bash
git clone https://github.com/andreiswahyudi/remove-background.git
cd remove-background

```


2. Instal dependensi:
```bash
pip install -r requirements.txt

```


3. Verifikasi instalasi:
```bash
streamlit --version

```



## Penggunaan

Anda dapat menjalankan alat ini melalui antarmuka web lokal.

### 1. Jalankan Aplikasi

```bash
streamlit run removebg.py

```

### 2. Unggah Foto

Unggah hingga 100 foto yang ingin diproses.

### 3. Mulai Proses

Klik tombol **PROCESS**. Sistem akan menampilkan progress bar untuk setiap foto yang sedang dikerjakan.

### 4. Unduh Hasil

Setelah selesai, klik tombol **Unduh Semua Hasil (ZIP)** untuk menyimpan foto yang telah bersih dari latar belakang.

## Disclaimer

Alat ini dibuat untuk **tujuan produktivitas**. Harap perhatikan penggunaan memori (RAM) perangkat Anda saat memproses file dalam jumlah banyak atau resolusi tinggi secara bersamaan.

---

**Apakah ada bagian lain yang ingin Anda sesuaikan sebelum diunggah ke GitHub?**
