# 📊 Analisis Data E-commerce & Dashboard Interaktif

Proyek ini terdiri dari dua komponen utama:
1. **Analisis Data** (Jupyter Notebook) untuk eksplorasi dataset e-commerce.
2. **Dashboard Interaktif** (Streamlit) untuk visualisasi data dan eksplorasi dinamis.

---

## 🗂 Struktur Repositori
submission
├───dashboard

│ ├── customers_dataset.csv

│ ├── geolocation_dataset.csv

│ └── products_dataset.csv

| └───dashboard.py

├───data

│ ├── customers_dataset.csv

│ ├── geolocation_dataset.csv

│ └── products_dataset.csv

├── Copy_of_Proyek_Analisis_Data.ipynb

├───README.md

└───requirements.txt

└───url.txt

---

## 📋 Prasyarat
- Python 3.8+
- Library Python:
  ```bash
  pip install pandas matplotlib seaborn streamlit jupyter
🚀 Cara Menjalankan
1. Analisis Data (Jupyter Notebook)
Buka terminal dan jalankan:

bash
Copy
jupyter notebook
Buka file Copy_of_Proyek_Analisis_Data.ipynb.

Eksekusi sel-sel untuk melihat:

Pembersihan data

Analisis distribusi pelanggan

Analisis karakteristik produk

Visualisasi EDA

2. Dashboard Interaktif (Streamlit)
Pastikan dataset berada di folder data/.

Jalankan di terminal:

bash
Copy
streamlit run dashboard.py
Dashboard akan terbuka di browser dengan dua tab:

📊 Visualisasi: Pilih analisis (Distribusi Pelanggan/Karakteristik Produk) di sidebar.

📈 Data Mentah: Tampilkan data mentah sesuai analisis yang dipilih.

🛠 Fitur Dashboard
Analisis Distribusi Pelanggan:

- Top 10 kota dengan pelanggan terbanyak (Bar Chart)

- Peta geografis pelanggan (Sample 1.000 data)

- Analisis Karakteristik Produk:

- Distribusi berat produk (Histogram + KDE)

- Distribusi dimensi produk (Panjang, Tinggi, Lebar)

##📁 Dataset
Dataset diambil dari Brazilian E-Commerce Public Dataset di Kaggle, mencakup:

- customers_dataset.csv: Data pelanggan

- geolocation_dataset.csv: Lokasi geografis

- products_dataset.csv: Karakteristik produk

💡 Kontribusi
Fork repositori

- Buat branch fitur (git checkout -b fitur/namafitur)

- Commit perubahan (git commit -m 'Tambahkan fitur X')

- Push ke branch (git push origin fitur/namafitur)

- Buat Pull Request
