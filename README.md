remove-background
Alat otomatisasi berbasis Python dan Streamlit yang dirancang untuk menghapus latar belakang hingga 100 foto secara sekaligus dengan cepat, mudah, dan aman.

Fitur Utama
📦 Pemrosesan Batch: Mampu menangani hingga 100 foto dalam satu kali proses unggah.

🔒 Privasi Terjamin: Proses penghapusan latar belakang dilakukan sepenuhnya secara lokal di komputer Anda. Tidak ada data yang diunggah ke server eksternal.

⚡ Efisien & Praktis: Cukup unggah foto melalui browser dan unduh hasilnya langsung dalam satu paket file ZIP.

🛠️ Didukung AI: Menggunakan teknologi segmentasi gambar canggih untuk hasil potongan yang rapi.

Prasyarat
Sebelum menjalankan aplikasi, pastikan perangkat Anda telah terinstal:

Python 3.10 atau versi lebih baru.

Microsoft Visual C++ Redistributable (Khusus pengguna Windows, untuk mendukung modul pemrosesan gambar).

Instalasi
Clone Repositori:

Bash
git clone https://github.com/andreiswahyudi/remove-background.git
cd remove-background
Instal Dependensi: Gunakan pip untuk menginstal pustaka yang diperlukan:

Bash
pip install -r requirements.txt
Penggunaan
Untuk menjalankan aplikasi ini di browser lokal Anda, ikuti langkah berikut:

Jalankan perintah Streamlit:

Bash
streamlit run removebg.py
Buka URL yang muncul di terminal (biasanya http://localhost:8501).

Unggah foto-foto yang ingin diproses (maksimal 100 file).

Klik tombol proses dan tunggu hingga selesai.

Unduh hasil akhirnya dalam format ZIP.

Daftar Dependensi
Aplikasi ini menggunakan beberapa pustaka utama:

streamlit: Untuk antarmuka web.

transparent-background: Mesin utama penghapus latar belakang.

Pillow: Untuk manipulasi gambar.

Disclaimer
Aplikasi ini ditujukan untuk mempermudah alur kerja produktivitas. Pastikan perangkat Anda memiliki memori (RAM) yang cukup saat memproses foto dalam jumlah besar sekaligus.
