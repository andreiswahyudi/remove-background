Python Background Remover
Alat otomatisasi berbasis Python yang kuat untuk menghapus latar belakang foto secara massal melalui antarmuka browser lokal yang sederhana dan efisien.
Fitur
	• 🖼️ Batch Processing: Unggah dan proses hingga 100 foto sekaligus dalam satu sesi.
	• 🔒 Privasi Lokal: Semua proses dilakukan di mesin Anda. Tidak ada data atau foto yang dikirim ke server eksternal.
	• 🚀 Cepat & Otomatis: Menghapus latar belakang secara otomatis dan mengonversi hasil ke format PNG transparan.
	• 📦 Ekspor ZIP: Mengemas semua hasil pemrosesan ke dalam satu file ZIP untuk pengunduhan yang praktis.
	• 🌐 Browser Based: Menggunakan Streamlit untuk antarmuka yang ramah pengguna dan mudah diakses via browser.
Prasyarat
	• Python: Proyek ini menggunakan Python 3.10+.
	• C++ Redistributable: Diperlukan untuk mendukung pustaka pemrosesan gambar pada sistem Windows.
Instalasi
	1. Clone repositori:
Bash

git clone https://github.com/andreiswahyudi/remove-background.git cd remove-background
	2. Instal dependensi:
Bash

# Disarankan menggunakan virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instal pustaka yang diperlukan
pip install streamlit transparent-background pillow tqdm

	# Instal Dependensi: Gunakan pip untuk menginstal pustaka yang diperlukan:
	pip install -r requirements.txt
	1. Verifikasi instalasi:
Bash

streamlit --version
Disclaimer
Alat ini dibuat untuk tujuan produktivitas. Harap perhatikan penggunaan memori (RAM) perangkat Anda saat memproses file dalam jumlah banyak atau resolusi tinggi secara bersamaan.
<img width="740" height="768" alt="image" src="https://github.com/user-attachments/assets/4a53ed75-09a8-456e-9501-1c29e0843dbf" />
