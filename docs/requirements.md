# Mini Knowledge Vault — User Requirements

## 1. Latar Belakang

Dalam proses belajar, pengguna sering mendapatkan berbagai catatan pengetahuan atau hal-hal penting yang ingin disimpan untuk dipelajari kembali. Namun, pengguna dapat mengalami kesulitan untuk menyimpan dan menemukan kembali catatan tersebut secara sederhana dan terorganisir.

Oleh karena itu, dibutuhkan sebuah tempat sederhana yang dapat membantu pengguna menyimpan, melihat, mencari, dan mengelola catatan pengetahuan yang diperoleh selama proses belajar.

Mini Knowledge Vault dibuat sebagai aplikasi sederhana yang berfokus pada kebutuhan tersebut tanpa menambahkan kompleksitas yang belum diperlukan.

---

## 2. Pengguna

Aplikasi ditujukan untuk **pelajar atau siapa pun yang ingin menyimpan catatan pengetahuan pribadi** yang diperoleh dari proses belajar.

Pada tahap awal, aplikasi digunakan oleh satu pengguna untuk mengelola catatan pengetahuannya sendiri.

---

## 3. Tujuan Aplikasi

Mini Knowledge Vault bertujuan untuk membantu pengguna:

* Menyimpan catatan pengetahuan secara terorganisir.
* Melihat kembali catatan yang telah disimpan.
* Menemukan catatan tertentu dengan lebih mudah.
* Menghapus catatan yang sudah tidak diperlukan.
* Mengembangkan dan memperbarui catatan pada tahap pengembangan berikutnya.

Tujuan utama aplikasi adalah menyediakan tempat sederhana untuk menyimpan dan mengelola pengetahuan yang diperoleh selama proses belajar.

---

## 4. Kebutuhan Pengguna

Sebagai pengguna, saya ingin:

1. Menambahkan catatan pengetahuan baru agar pengetahuan yang saya dapatkan dapat disimpan.
2. Melihat seluruh catatan yang telah disimpan agar saya dapat meninjau kembali pengetahuan yang pernah dipelajari.
3. Mencari catatan berdasarkan informasi tertentu agar saya dapat menemukan catatan yang dibutuhkan dengan lebih mudah.
4. Menghapus catatan yang sudah tidak diperlukan.
5. Mengubah catatan yang sudah ada apabila terdapat informasi yang perlu diperbaiki atau diperbarui.

Kebutuhan untuk mengubah catatan tetap menjadi bagian dari kebutuhan aplikasi, tetapi fitur tersebut tidak menjadi bagian dari implementasi versi awal.

---

## 5. Informasi yang Disimpan

Setiap catatan pengetahuan setidaknya memiliki tiga informasi utama:

* **Topik**
* **Judul**
* **Isi catatan**

Contoh:

| Topik  | Judul              | Isi Catatan                                          |
| ------ | ------------------ | ---------------------------------------------------- |
| Python | List Comprehension | Cara membuat list dengan sintaks yang lebih ringkas. |

Contoh lain:

```text
Topik   : Git
Judul   : Git Commit
Catatan : Digunakan untuk menyimpan perubahan pada repository.
```

---

## 6. Fitur Utama

### 6.1 Fitur Versi Awal

Versi awal aplikasi menyediakan kemampuan untuk:

* Menambah catatan.
* Melihat seluruh catatan.
* Mencari catatan.
* Menghapus catatan.
* Keluar dari aplikasi.

Menu utama versi awal:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar
```

### 6.2 Fitur Pengembangan Berikutnya

Setelah versi awal selesai dan dipahami, aplikasi dapat dikembangkan dengan fitur tambahan seperti:

* Mengubah atau mengedit catatan.
* Penyimpanan data secara permanen.
* Validasi input yang lebih baik.
* Pencarian yang lebih fleksibel.
* Pengelompokan catatan berdasarkan topik.

Fitur tambahan akan dikembangkan secara bertahap berdasarkan kebutuhan dan proses pembelajaran.

---

## 7. Input

Pengguna dapat memberikan informasi berupa:

### Saat Menambahkan Catatan

* Topik catatan.
* Judul catatan.
* Isi catatan.

### Saat Mencari Catatan

* Kata kunci atau informasi pencarian.

### Saat Menghapus Catatan

* Pilihan atau identitas catatan yang ingin dihapus.

### Saat Memilih Menu

* Pilihan menu yang tersedia pada aplikasi.

Pada pengembangan berikutnya, input tambahan dapat digunakan untuk mengubah catatan.

---

## 8. Output

Aplikasi memberikan informasi kepada pengguna berupa:

* Daftar catatan yang tersimpan.
* Hasil pencarian catatan.
* Informasi bahwa catatan berhasil ditambahkan.
* Informasi bahwa catatan berhasil dihapus.
* Informasi apabila catatan yang dicari tidak ditemukan.
* Informasi apabila suatu tindakan tidak dapat dilakukan.
* Informasi apabila pilihan menu tidak valid.
* Pesan ketika pengguna keluar dari aplikasi.

Pada pengembangan berikutnya, aplikasi juga dapat memberikan informasi bahwa sebuah catatan berhasil diperbarui.

---

## 9. Batasan Aplikasi

Pada tahap awal, aplikasi memiliki batasan sebagai berikut:

* Digunakan untuk kebutuhan pribadi.
* Digunakan oleh satu pengguna.
* Tidak membutuhkan sistem login atau autentikasi.
* Tidak membutuhkan koneksi internet.
* Tidak membutuhkan fitur berbagi catatan.
* Tidak mencakup sinkronisasi antarperangkat.
* Fokus pada pengelolaan catatan pengetahuan sederhana.
* Menggunakan antarmuka berbasis terminal.
* Tidak menggunakan database pada versi awal.
* Penyimpanan permanen belum menjadi bagian dari implementasi awal.

Batasan tersebut dapat berubah apabila kebutuhan aplikasi berkembang pada tahap berikutnya.

---

## 10. Di Luar Cakupan Versi Awal

Fitur berikut tidak menjadi bagian dari versi awal aplikasi:

* Akun pengguna.
* Login dan autentikasi.
* Berbagi catatan.
* Kolaborasi antar pengguna.
* Notifikasi.
* Integrasi dengan layanan eksternal.
* Sinkronisasi antarperangkat.
* Antarmuka berbasis web.
* Antarmuka berbasis mobile.
* Database.
* API.
* Penyimpanan permanen.
* Fitur edit catatan.

Fitur edit dan penyimpanan permanen dapat dipertimbangkan sebagai bagian dari pengembangan setelah versi awal selesai.

---

## 11. Kriteria Keberhasilan

Aplikasi versi awal dianggap memenuhi kebutuhan apabila pengguna dapat:

1. Menjalankan aplikasi melalui terminal.
2. Melihat menu utama.
3. Menambahkan sebuah catatan pengetahuan.
4. Melihat catatan yang telah ditambahkan.
5. Mencari catatan berdasarkan informasi tertentu.
6. Menghapus catatan yang telah tersedia.
7. Kembali ke menu utama setelah melakukan operasi.
8. Mendapatkan informasi ketika memasukkan pilihan yang tidak valid.
9. Keluar dari aplikasi melalui menu yang tersedia.

Kebutuhan untuk mengubah catatan akan menjadi bagian dari kriteria keberhasilan pada tahap pengembangan berikutnya setelah fitur edit diterapkan.

---

## 12. Prinsip Pengembangan

Mini Knowledge Vault dikembangkan secara bertahap sebagai media pembelajaran pemrograman.

Pengembangan tidak dilakukan dengan memasukkan seluruh fitur sejak awal. Fitur akan ditambahkan berdasarkan kebutuhan aplikasi dan konsep pemrograman yang sedang dipelajari.

Alur pengembangan:

```text
Memahami kebutuhan
        ↓
Merancang solusi
        ↓
Membuat versi sederhana
        ↓
Menguji aplikasi
        ↓
Menemukan kebutuhan baru
        ↓
Mempelajari konsep baru
        ↓
Memodifikasi aplikasi
        ↓
Mendokumentasikan hasil
```

Dengan pendekatan tersebut, setiap perubahan pada aplikasi diharapkan memiliki alasan dan menjadi bagian dari proses pembelajaran.

---

**Versi dokumen:** 1.1
**Status:** Draft Requirement
**Project:** Mini Knowledge Vault
