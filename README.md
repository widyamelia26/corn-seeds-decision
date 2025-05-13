# Sistem Pendukung Keputusan Untuk Pemilihan Bibit Jagung Terbaik
## Deskripsi Umum
Sistem ini merupakan aplikasi Sistem Pendukung Keputusan (SPK) berbasis Streamlit yang dikembangkan untuk membantu decision maker dalam memilih varietas bibit jagung terbaik berdasarkan sejumlah kriteria. Sistem mendukung tiga metode pengambilan keputusan, yaitu:
*  AHP (Analytic Hierarchy Process)
*  TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
*  Profile Matching
*  Integrasi AHP dan TOPSIS
*  Integrasi AHP dan Profile Matching

Sistem ini fleksibel dan dapat disesuaikan dengan kebutuhan pengguna, termasuk jumlah alternatif, kriteria, jenis dan bobot kriteria, serta metode pengambilan keputusan yang digunakan.

## Cara Menjalankan Sistem
Anda dapat menjalankan sistem ini melalui dua cara, yaitu secara lokal di komputer Anda atau langsung melalui tautan web.

### Opsi 1: Lokal dari Komputer
1. Pastikan Anda telah menginstal Python, Streamlit, dan library pendukung (NumPy, Pandas, Matplotlib) sesuai dengan requirements.txt
2. Download dan simpan file ahptopsispm_baru.py dan jagung(1).jpeg dalam folder yang sama.
3. Jalankan perintah berikut pada terminal
   `streamlit run ahptopsispm_baru.py`
5. Aplikasi akan terbuka di browser lokal secara otomatis.

### Opsi 2: 
Cukup kunjungi [sistem yang telah dideploy melalui Streamlit Cloud](https://corn-seeds-decision.streamlit.app/).
Tidak perlu instalasi apa pun. Anda bisa langsung menggunakan aplikasi secara praktis dari browser Anda.

## Langkah-Langkah Penggunaan Sistem
