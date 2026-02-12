Python Background Remover
Alat otomatisasi berbasis Python yang kuat untuk menghapus latar belakang foto secara massal melalui antarmuka browser lokal yang sederhana dan efisien.

Fitur
🖼️ Batch Processing: Unggah dan proses hingga 100 foto sekaligus dalam satu sesi.

🔒 Privasi Lokal: Semua proses dilakukan di mesin Anda. Tidak ada data atau foto yang dikirim ke server eksternal.

🚀 Cepat & Otomatis: Menghapus latar belakang secara otomatis dan mengonversi hasil ke format PNG transparan.

📦 Ekspor ZIP: Mengemas semua hasil pemrosesan ke dalam satu file ZIP untuk pengunduhan yang praktis.

🌐 Browser Based: Menggunakan Streamlit untuk antarmuka yang ramah pengguna dan mudah diakses via browser.

Prasyarat
Python: Proyek ini menggunakan Python 3.10+.

C++ Redistributable: Diperlukan untuk mendukung pustaka pemrosesan gambar pada sistem Windows.

Instalasi
Clone repositori:

Bash
git clone https://github.com/username/python-bg-remover.git
cd python-bg-remover
Instal dependensi:

Bash
# Disarankan menggunakan virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instal pustaka yang diperlukan
pip install streamlit transparent-background pillow tqdm
Verifikasi instalasi:

Bash
streamlit --version
Penggunaan
Anda dapat menjalankan alat ini melalui antarmuka web lokal.

1. Jalankan Aplikasi
Bash
streamlit run webapp.py
2. Unggah Foto
Buka alamat yang muncul di terminal (biasanya http://localhost:8501), lalu unggah hingga 100 foto yang ingin diproses.

3. Mulai Proses
Klik tombol Mulai Proses Otomasi. Sistem akan menampilkan progress bar untuk setiap foto yang sedang dikerjakan.

4. Unduh Hasil
Setelah selesai, klik tombol Unduh Semua Hasil (ZIP) untuk menyimpan foto yang telah bersih dari latar belakang.

Konfigurasi
Batas maksimal file dapat diubah secara manual pada file webapp.py:

Python
# Ubah angka 100 sesuai kebutuhan sistem Anda
if file_count > 100:
    st.error("Batas maksimal terlampaui")
Disclaimer
Alat ini dibuat untuk tujuan produktivitas. Harap perhatikan penggunaan memori (RAM) perangkat Anda saat memproses file dalam jumlah banyak atau resolusi tinggi secara bersamaan.
