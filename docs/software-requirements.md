# Software Requirements Specification (SRS)

## Mini Knowledge Vault

**Versi:** 1.1  
**Status:** Draft  
**Jenis Aplikasi:** Terminal / Command-Line Application  
**Bahasa Pemrograman:** Python

---

# 1. Pengantar

## 1.1 Tujuan Aplikasi

Mini Knowledge Vault adalah aplikasi berbasis terminal yang digunakan untuk menyimpan dan mengelola catatan pengetahuan pribadi yang diperoleh pengguna selama proses belajar.

Aplikasi ini dirancang sebagai tempat sederhana bagi pengguna untuk menyimpan informasi penting yang ingin dipelajari atau ditinjau kembali di kemudian hari.

Pengembangan aplikasi dilakukan secara bertahap agar setiap fitur dapat menjadi bagian dari proses pembelajaran fundamental pemrograman.

Pada versi awal, aplikasi berfokus pada fungsi dasar:

- Menambahkan catatan.
- Melihat seluruh catatan.
- Mencari catatan.
- Keluar dari aplikasi.

Fitur seperti menghapus, mengubah, dan menyimpan data secara permanen akan dikembangkan pada tahap berikutnya.

---

## 1.2 Sasaran Pengguna

Aplikasi ditujukan untuk pelajar atau individu yang ingin menyimpan dan mengelola catatan pengetahuan pribadi secara sederhana melalui terminal.

Pada tahap awal, aplikasi hanya digunakan oleh satu pengguna dan tidak memiliki sistem akun atau autentikasi.

---

## 1.3 Ruang Lingkup

Mini Knowledge Vault berfokus pada pengelolaan catatan pengetahuan pribadi melalui antarmuka terminal.

Ruang lingkup pengembangan dilakukan secara bertahap.

### Versi awal

Fitur yang menjadi fokus implementasi pertama:

- Menambahkan catatan.
- Melihat seluruh catatan.
- Mencari catatan.
- Keluar dari aplikasi.

### Pengembangan berikutnya

Fitur yang dapat ditambahkan setelah versi dasar selesai:

- Menghapus catatan.
- Mengubah catatan.
- Menyimpan data secara permanen menggunakan file JSON.
- Validasi dan error handling yang lebih baik.
- Pengembangan struktur kode.

Fitur seperti login, database, web interface, API, sinkronisasi, dan kolaborasi antar pengguna tidak termasuk dalam tujuan awal project.

---

# 2. Glosarium

| Istilah | Definisi |
|---|---|
| **Mini Knowledge Vault** | Nama aplikasi yang digunakan untuk menyimpan dan mengelola catatan pengetahuan. |
| **Catatan** | Informasi pengetahuan yang disimpan oleh pengguna. |
| **Topik** | Kategori atau bidang dari sebuah catatan, misalnya Python, Git, atau HTML. |
| **Judul** | Nama atau judul yang diberikan pada sebuah catatan. |
| **Isi Catatan** | Informasi atau penjelasan yang disimpan dalam sebuah catatan. |
| **Terminal** | Antarmuka berbasis teks yang digunakan pengguna untuk berinteraksi dengan aplikasi. |
| **CLI** | Command-Line Interface, yaitu antarmuka aplikasi yang menggunakan perintah atau input berbasis teks. |
| **SRS** | Software Requirements Specification, yaitu dokumen yang menjelaskan kebutuhan dan spesifikasi perangkat lunak. |
| **SKPL** | Spesifikasi Kebutuhan Perangkat Lunak, istilah bahasa Indonesia untuk Software Requirements Specification. |
| **Functional Requirement** | Kebutuhan yang menjelaskan fungsi atau kemampuan yang harus disediakan oleh aplikasi. |
| **Non-Functional Requirement** | Kebutuhan yang menjelaskan kualitas atau karakteristik aplikasi, seperti usability, maintainability, dan error handling. |
| **Flowchart** | Diagram visual yang menggambarkan alur proses atau algoritma aplikasi. |
| **V1** | Versi pertama aplikasi yang berfokus pada fitur fundamental. |
| **V2** | Pengembangan berikutnya yang menambahkan fitur hapus catatan. |
| **V3** | Pengembangan yang menambahkan fitur edit catatan. |
| **V4** | Pengembangan yang menambahkan penyimpanan permanen menggunakan JSON. |

---

# 3. Kebutuhan Pengguna

## 3.1 Deskripsi Umum Aplikasi

Mini Knowledge Vault merupakan aplikasi terminal sederhana untuk menyimpan dan mengelola catatan pengetahuan yang diperoleh selama proses belajar.

Pengguna dapat memilih menu yang tersedia untuk melakukan operasi terhadap catatan.

Alur interaksi dasar aplikasi adalah:

```text
Mulai
  ↓
Tampilkan Menu
  ↓
Pengguna Memilih Menu
  ↓
Jalankan Fitur
  ↓
Kembali ke Menu
  ↓
Pengguna Memilih Menu Kembali
