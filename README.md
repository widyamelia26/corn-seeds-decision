# Sistem Pendukung Keputusan Untuk Pemilihan Bibit Jagung Terbaik
## 1. Deskripsi Umum
Sistem ini merupakan aplikasi Sistem Pendukung Keputusan (SPK) berbasis Streamlit yang dikembangkan untuk membantu decision maker dalam memilih varietas bibit jagung terbaik berdasarkan sejumlah kriteria. Sistem mendukung tiga metode pengambilan keputusan, yaitu:
*  AHP (Analytic Hierarchy Process)
*  TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
*  Profile Matching
*  Integrasi AHP dan TOPSIS
*  Integrasi AHP dan Profile Matching

Sistem ini fleksibel dan dapat disesuaikan dengan kebutuhan pengguna, termasuk jumlah alternatif, kriteria, jenis dan bobot kriteria, serta metode pengambilan keputusan yang digunakan.

## 2. Cara Menjalankan Sistem
Anda dapat menjalankan sistem ini melalui dua cara, yaitu secara lokal di komputer Anda atau langsung melalui tautan web.

### Opsi 1: Lokal dari Komputer
1. Pastikan Anda telah menginstal Python, Streamlit, dan library pendukung (NumPy, Pandas, Matplotlib) sesuai dengan requirements.txt
2. Download dan simpan file ahptopsispm_baru.py dan jagung(1).jpeg dalam folder yang sama.
3. Jalankan perintah berikut pada terminal
   `streamlit run ahptopsispm_baru.py`
5. Aplikasi akan terbuka di browser lokal secara otomatis.

### Opsi 2: Online melalui Streamlit Cloud
Cukup kunjungi [sistem yang telah dideploy melalui Streamlit Cloud](https://corn-seeds-decision.streamlit.app/).
Tidak perlu instalasi apa pun. Anda bisa langsung menggunakan aplikasi secara praktis dari browser Anda.

## 3. Langkah-Langkah Penggunaan Sistem
### 3.1 Konfigurasi Awal
1. Masukkan jumlah alternatif (varietas jagung) dan jumlah kriteria.
2. Masukkan nama-nama alternatif dan kriteria sesuai kebutuhan.
3. Pilih salah satu metode pengambilan keputusan: AHP, TOPSIS, atau Profile Matching.
### 3.2 Metode AHP
**1. Perbandingan Berpasangan Antar Kriteria**
   * Pilih kriteria mana yang lebih penting antara dua kriteria.
   * Tentukan tingkat kepentingan pada skala 1–9 menggunakan slider.
   * Ulangi proses ini hingga semua pasangan kriteria selesai dibandingkan.
   
   _**Catatan:** Jika nilai perbandingan berpasangan tidak konsisten (nilai CR > 0.1), sistem akan memberikan peringatan. Namun, sistem tetap dapat melakukan perhitungan dan    menampilkan rekomendasi. Harap diperhatikan bahwa hasil tersebut berisiko bias atau tidak valid, sehingga disarankan untuk meninjau kembali input pengguna._

**2. Perbandingan Berpasangan Antar Alternatif (per Kriteria)**
   
   Lakukan hal yang sama seperti di poin 1 untuk membandingkan setiap varietas jagung berdasarkan masing-masing kriteria.
   
**4. Analisa**
   
   Klik tombol "Tentukan Varietas dengan AHP" untuk melihat hasil skor dan pemeringkatan alternatif.

### 3.3 Metode TOPSIS
**1. Metode Pembobotan Kriteria**

   Pilih salah satu metode pembobotan: Manual atau AHP.
   - Jika memilih manual, masukkan bobot masing-masing kriteria (jumlah total bobot harus maksimal 1). Namun, sistem akan otomatis menghitung sisa bobot pada kriteria terakhir.
   - Jika menggunakan AHP, lakukan perbandingan berpasangan antar kriteria seperti pada metode AHP.
   
   _**Catatan:** Jika perbandingan tidak konsisten (CR > 0.1), sistem tetap akan menghitung skor dan menampilkan hasil. Namun, hasil rekomendasi tersebut berisiko bias atau tidak valid._

**2. Tipe dan Nilai Kriteria**
   * Tentukan apakah setiap kriteria bersifat Benefit (semakin tinggi semakin baik) atau Cost (semakin rendah semakin baik).
   * Masukkan nilai performa alternatif untuk setiap kriteria melalui tabel matriks keputusan.

**3. Analisa**
   
   Klik tombol "Tentukan Varietas Jagung dengan TOPSIS" untuk melihat hasil perhitungan, skor TOPSIS, dan ranking alternatif.

### 3.4 Metode Profile Matching

**1. Pengaturan Kriteria**

   Tentukan jenis kriteria:
   - Core Factor (CF): Kriteria utama, sangat penting dalam pengambilan keputusan.
   - Secondary Factor (SF): Kriteria tambahan, berfungsi sebagai pelengkap.

**2. Pilih tipe data**

Ada dua tipe data yang dapat dipilih,
- Skala (1–5): Cocok untuk penilaian subjektif (misalnya, daya tahan hama: 4).
- Rentang numerik (e.g. 20–30): Cocok untuk data objektif (misalnya, kadar air: 22–25).

**3. Tentukan nilai ideal untuk setiap kriteria**

Tentukan nilai paling baik atau optimal untuk setiap kriteria, dengan contoh input sebagai berikut.
- Contoh Skala: Ideal “Daya Tumbuh” adalah 5.
- Contoh Rentang: Ideal “Kadar Air” adalah 23.

**4. Pembobotan Kriteria**

   a. Bobot dapat diatur manual atau menggunakan AHP.
      * Jika menggunakan manual, total bobot tidak boleh melebihi 1. Selain itu, total bobot Core Factor (CF) harus lebih dari 50%. Jika tidak, sistem akan memberikan peringatan namun tetap melanjutkan perhitungan.
      * Jika menggunakan AHP, sistem akan mengevaluasi konsistensi dan total bobot core factor. Total bobot Core Factor (CF) harus lebih dari 50%. Jika tidak, sistem akan memberikan peringatan namun tetap melanjutkan perhitungan.
   
   _**Catatan:** Jika perbandingan berpasangan tidak konsisten (CR > 0.1) atau bobot CF < 50%, sistem tetap akan memproses, tetapi hasilnya berpotensi tidak valid_
   
   b. Input Skor Alternatif
      * Untuk tipe Skala, masukkan skor antara 1–5.
      * Untuk tipe Rentang, masukkan nilai minimum dan maksimum.

**5. Analisa**

Klik tombol "Tentukan Varietas Jagung Terbaik dengan Profile Matching". Sistem akan menampilkan skor CF, SF, skor total, dan peringkat dari masing-masing alternatif.

