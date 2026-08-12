# Software Requirements Specification (SRS)

## Mini Knowledge Vault

**Versi:** 1.0
**Status:** Draft
**Jenis Aplikasi:** Terminal / Command-Line Application
**Bahasa Pemrograman:** Python

---

## 1. Pengantar

### 1.1 Tujuan Aplikasi

Mini Knowledge Vault adalah aplikasi berbasis terminal yang digunakan untuk menyimpan dan mengelola catatan pengetahuan pribadi yang diperoleh pengguna selama proses belajar.

Aplikasi ini dirancang sebagai tempat sederhana bagi pengguna untuk menyimpan informasi penting yang ingin dipelajari atau ditinjau kembali di kemudian hari.

Pada versi awal, aplikasi menyediakan beberapa fungsi utama, yaitu menambahkan, melihat, mencari, dan menghapus catatan pengetahuan.

### 1.2 Sasaran Pengguna

Aplikasi ditujukan untuk pelajar atau individu yang ingin menyimpan dan mengelola catatan pengetahuan pribadi secara sederhana melalui terminal.

Pada tahap awal, aplikasi hanya digunakan oleh satu pengguna dan tidak memiliki sistem akun atau autentikasi.

### 1.3 Ruang Lingkup

Mini Knowledge Vault berfokus pada pengelolaan catatan pengetahuan sederhana.

Fitur yang menjadi ruang lingkup versi awal:

* Menambahkan catatan.
* Melihat seluruh catatan.
* Mencari catatan.
* Menghapus catatan.
* Keluar dari aplikasi.

Fitur seperti login, database, web interface, API, sinkronisasi, dan kolaborasi antar pengguna tidak termasuk dalam versi awal.

---

## 2. Glosarium

| Istilah                        | Definisi                                                                                                             |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Mini Knowledge Vault**       | Nama aplikasi yang digunakan untuk menyimpan dan mengelola catatan pengetahuan.                                      |
| **Catatan**                    | Informasi pengetahuan yang disimpan oleh pengguna.                                                                   |
| **Topik**                      | Kategori atau bidang dari sebuah catatan, misalnya Python, Git, atau HTML.                                           |
| **Judul**                      | Nama atau judul yang diberikan pada sebuah catatan.                                                                  |
| **Isi Catatan**                | Informasi atau penjelasan yang disimpan dalam sebuah catatan.                                                        |
| **Terminal**                   | Antarmuka berbasis teks yang digunakan pengguna untuk berinteraksi dengan aplikasi.                                  |
| **SRS**                        | Software Requirements Specification, yaitu dokumen yang menjelaskan kebutuhan dan spesifikasi perangkat lunak.       |
| **SKPL**                       | Spesifikasi Kebutuhan Perangkat Lunak, istilah bahasa Indonesia untuk Software Requirements Specification.           |
| **Functional Requirement**     | Kebutuhan yang menjelaskan fungsi atau kemampuan yang harus disediakan oleh aplikasi.                                |
| **Non-Functional Requirement** | Kebutuhan yang menjelaskan kualitas atau karakteristik aplikasi, seperti usability, performance, dan error handling. |
| **Flowchart**                  | Diagram visual yang menggambarkan alur proses atau algoritma aplikasi.                                               |

---

# 3. Kebutuhan Pengguna

## 3.1 Deskripsi Umum Aplikasi

Mini Knowledge Vault merupakan aplikasi terminal sederhana untuk menyimpan dan mengelola catatan pengetahuan yang diperoleh selama belajar.

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
```

Aplikasi akan terus berjalan selama pengguna belum memilih menu keluar.

## 3.2 Informasi Sebuah Catatan

Setiap catatan pengetahuan memiliki informasi sebagai berikut:

* **Topik**
* **Judul**
* **Isi Catatan**

Contoh:

```text
Topik : Python
Judul : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.
```

## 3.3 Kegunaan Aplikasi

Mini Knowledge Vault memberikan beberapa kegunaan bagi pengguna:

1. Pengguna dapat menyimpan pengetahuan yang diperoleh selama belajar.
2. Pengguna dapat melihat kembali seluruh catatan yang telah dibuat.
3. Pengguna dapat mencari catatan tertentu.
4. Pengguna dapat menghapus catatan yang sudah tidak diperlukan.
5. Pengguna dapat mengelola catatan melalui antarmuka terminal yang sederhana.

---

# 4. Sistem Arsitektur

## 4.1 Gambaran Umum

Pada versi awal, Mini Knowledge Vault menggunakan arsitektur aplikasi sederhana yang berjalan secara lokal pada komputer pengguna.

Komponen utama aplikasi terdiri dari:

```text
Pengguna
   ↓
Terminal / Command Line
   ↓
Program Python
   ↓
Data Catatan di Memori
```

Pengguna memberikan input melalui terminal. Program Python memproses input tersebut dan menghasilkan output kembali melalui terminal.

Pada versi awal, data catatan disimpan sementara di dalam memori selama program berjalan.

## 4.2 Komponen Sistem

Sistem awal terdiri dari beberapa bagian utama:

### User Interface

Antarmuka berbasis terminal yang digunakan pengguna untuk memilih menu dan memasukkan data.

### Application Logic

Bagian program yang menangani logika seperti:

* Menampilkan menu.
* Memproses pilihan pengguna.
* Menambahkan catatan.
* Menampilkan catatan.
* Mencari catatan.
* Menghapus catatan.

### Data Storage

Pada versi awal, data disimpan sementara di dalam memori program.

Penyimpanan permanen seperti file JSON akan dipertimbangkan pada tahap pengembangan berikutnya.

---

# 5. Spesifikasi Kebutuhan Sistem

## 5.1 Kebutuhan Fungsional

### FR-01 — Menampilkan Menu Utama

Sistem harus menampilkan menu utama ketika aplikasi dijalankan.

Menu utama terdiri dari:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar
```

Pengguna dapat memilih salah satu menu yang tersedia.

---

### FR-02 — Menambahkan Catatan

Sistem harus memungkinkan pengguna menambahkan catatan pengetahuan baru.

Pengguna harus dapat memasukkan:

* Topik.
* Judul.
* Isi catatan.

Contoh:

```text
Topik    : Python
Judul    : List Comprehension
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.
```

Setelah data berhasil diproses, sistem menampilkan informasi bahwa catatan berhasil disimpan.

Contoh:

```text
Catatan berhasil disimpan!
```

---

### FR-03 — Melihat Semua Catatan

Sistem harus memungkinkan pengguna melihat seluruh catatan yang telah ditambahkan selama aplikasi berjalan.

Apabila terdapat beberapa catatan, sistem menampilkan catatan tersebut secara terstruktur agar mudah dibaca.

Contoh:

```text
=== DAFTAR CATATAN ===

[1]
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.

[2]
Topik   : Git
Judul   : Git Commit
Catatan : Digunakan untuk menyimpan perubahan pada repository.
```

Apabila belum terdapat catatan, sistem memberikan informasi bahwa belum ada catatan yang tersedia.

---

### FR-04 — Mencari Catatan

Sistem harus memungkinkan pengguna mencari catatan berdasarkan informasi tertentu.

Pengguna dapat memasukkan kata kunci pencarian.

Sistem kemudian memproses kata kunci tersebut dan menampilkan catatan yang sesuai.

Contoh:

```text
Masukkan kata kunci: Python

Hasil pencarian:

Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.
```

Apabila tidak ditemukan catatan yang sesuai, sistem menampilkan informasi bahwa catatan tidak ditemukan.

---

### FR-05 — Menghapus Catatan

Sistem harus memungkinkan pengguna menghapus catatan yang tersedia.

Pengguna memilih catatan yang ingin dihapus, kemudian sistem menghapus catatan tersebut dari data yang sedang digunakan aplikasi.

Setelah berhasil, sistem memberikan informasi kepada pengguna.

Contoh:

```text
Catatan berhasil dihapus!
```

---

### FR-06 — Keluar dari Aplikasi

Sistem harus memungkinkan pengguna keluar dari aplikasi dengan memilih menu keluar.

Ketika pengguna memilih menu tersebut, aplikasi menghentikan proses dan menampilkan pesan penutup.

Contoh:

```text
Terima kasih telah menggunakan Mini Knowledge Vault.

Program selesai.
```

---

### FR-07 — Menangani Pilihan Menu Tidak Valid

Sistem harus menangani input menu yang tidak tersedia.

Contoh ketika pengguna memasukkan:

```text
Pilih menu: 9
```

Sistem memberikan informasi bahwa pilihan tidak valid dan meminta pengguna memilih menu kembali.

Contoh:

```text
Pilihan tidak valid.
Silakan pilih menu yang tersedia.
```

---

## 5.2 Kebutuhan Non-Fungsional

### NFR-01 — Usability

Aplikasi harus memiliki antarmuka terminal yang sederhana dan mudah dipahami oleh pengguna.

Instruksi yang diberikan kepada pengguna harus jelas sehingga pengguna dapat mengetahui tindakan yang harus dilakukan.

### NFR-02 — Error Handling

Aplikasi harus dapat menangani input pengguna yang tidak sesuai dengan pilihan yang tersedia tanpa langsung menghentikan program.

Sistem harus memberikan pesan kesalahan yang mudah dipahami dan memungkinkan pengguna kembali ke menu utama.

### NFR-03 — Maintainability

Program harus memiliki struktur yang sederhana dan mudah dikembangkan.

Fungsi-fungsi aplikasi sebaiknya dipisahkan berdasarkan tanggung jawabnya agar penambahan atau perubahan fitur pada tahap berikutnya dapat dilakukan dengan lebih mudah.

### NFR-04 — Performance

Aplikasi harus dapat menjalankan operasi dasar seperti menambah, melihat, mencari, dan menghapus catatan tanpa proses yang tidak diperlukan.

Karena aplikasi ditujukan untuk penggunaan lokal dengan jumlah catatan yang relatif sederhana pada tahap awal, kebutuhan performa tidak mencakup pemrosesan data dalam skala besar.

### NFR-05 — Offline

Aplikasi versi awal harus dapat digunakan tanpa koneksi internet.

Seluruh proses utama dilakukan secara lokal pada komputer pengguna.

### NFR-06 — Simplicity

Aplikasi harus mempertahankan konsep sederhana dan tidak menggunakan komponen eksternal yang belum diperlukan untuk kebutuhan versi awal.

---

# 6. Antarmuka Pengguna

## 6.1 Jenis Antarmuka

Mini Knowledge Vault menggunakan **Command-Line Interface (CLI)** atau antarmuka berbasis terminal.

Pengguna berinteraksi dengan aplikasi melalui teks dan input dari keyboard.

## 6.2 Menu Utama

Antarmuka utama dirancang dengan bentuk sederhana:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar

Pilih menu:
```

## 6.3 Form Tambah Catatan

Ketika pengguna memilih menu tambah catatan, sistem meminta:

```text
Topik    :
Judul    :
Catatan  :
```

Setelah seluruh data dimasukkan, sistem memproses dan menyimpan catatan.

## 6.4 Output Sistem

Sistem harus memberikan feedback kepada pengguna setelah sebuah operasi dilakukan.

Contohnya:

```text
Catatan berhasil disimpan!
```

atau:

```text
Catatan tidak ditemukan.
```

---

# 7. Antarmuka Perangkat Keras

Aplikasi dapat digunakan pada komputer yang memiliki:

* Keyboard untuk memasukkan data.
* Monitor atau layar untuk menampilkan output terminal.
* Media penyimpanan untuk menyimpan source code aplikasi.

Aplikasi tidak membutuhkan perangkat keras khusus.

---

# 8. Antarmuka Perangkat Lunak

Pada versi awal, aplikasi membutuhkan:

* Sistem operasi yang mendukung Python.
* Python sebagai bahasa pemrograman.
* Terminal atau command-line interface untuk menjalankan aplikasi.

Aplikasi tidak membutuhkan:

* Web browser.
* Database server.
* API eksternal.
* Web server.
* Sistem autentikasi.

---

# 9. Model Data

Pada versi awal, sebuah catatan dapat dimodelkan sebagai objek data sederhana yang memiliki tiga informasi utama:

```text
Catatan
│
├── Topik
├── Judul
└── Isi Catatan
```

Secara konseptual, data dapat direpresentasikan sebagai:

```text
Knowledge
├── topic
├── title
└── content
```

Kumpulan catatan kemudian dapat direpresentasikan sebagai:

```text
Knowledge Vault
│
├── Knowledge 1
├── Knowledge 2
├── Knowledge 3
└── ...
```

Implementasi struktur data akan ditentukan pada tahap pengembangan program.

---

# 10. Alur Utama Sistem

Alur utama aplikasi adalah sebagai berikut:

```text
Mulai
  ↓
Tampilkan Menu
  ↓
Pengguna Memilih Menu
  ↓
┌───────────────────────────────┐
│                               │
├── 1. Tambah Catatan            │
│       ↓                       │
│   Simpan Catatan              │
│       ↓                       │
├── 2. Lihat Catatan             │
│       ↓                       │
│   Tampilkan Catatan           │
│       ↓                       │
├── 3. Cari Catatan              │
│       ↓                       │
│   Tampilkan Hasil Pencarian   │
│       ↓                       │
├── 4. Hapus Catatan             │
│       ↓                       │
│   Hapus Catatan               │
│       ↓                       │
├── 5. Keluar                    │
│       ↓                       │
│     Selesai                   │
│                               │
└───────────────────────────────┘

Selain pilihan 5:
        ↓
Kembali ke Menu Utama
```

---

# 11. Batasan Sistem

Versi awal Mini Knowledge Vault memiliki batasan sebagai berikut:

1. Aplikasi hanya digunakan secara lokal.
2. Aplikasi tidak memiliki sistem login atau autentikasi.
3. Aplikasi hanya ditujukan untuk satu pengguna.
4. Aplikasi tidak menyediakan fitur berbagi catatan.
5. Aplikasi tidak menyediakan kolaborasi antar pengguna.
6. Aplikasi tidak membutuhkan koneksi internet.
7. Aplikasi tidak menggunakan database pada versi awal.
8. Data pada versi awal belum disimpan secara permanen setelah program ditutup.
9. Aplikasi hanya menyediakan antarmuka berbasis terminal.
10. Fitur edit catatan belum menjadi bagian dari implementasi awal.

---

# 12. Rencana Pengembangan Sistem

Mini Knowledge Vault dirancang untuk dapat dikembangkan secara bertahap sesuai dengan proses pembelajaran.

## Versi 1 — Basic Knowledge Vault

Fitur:

* Tambah catatan.
* Lihat catatan.
* Cari catatan.
* Keluar.

Fokus pembelajaran:

* Variable.
* List.
* Dictionary.
* Function.
* Input dan output.
* Conditional statement.
* Loop.

## Versi 2 — Delete Feature

Menambahkan kemampuan untuk menghapus catatan.

Fokus pembelajaran:

* Manipulasi data.
* Validasi input.
* Penggunaan struktur data.

## Versi 3 — Edit Feature

Menambahkan kemampuan untuk mengubah catatan yang sudah tersedia.

Fokus pembelajaran:

* Mencari data tertentu.
* Mengubah data.
* Mengelola state/data aplikasi.

## Versi 4 — Persistent Storage

Menambahkan penyimpanan data secara permanen menggunakan file JSON.

Contoh:

```text
mini-knowledge-vault/
├── main.py
└── data.json
```

Fokus pembelajaran:

* File handling.
* JSON.
* Membaca data dari file.
* Menulis data ke file.

## Versi 5 — Improvement

Pengembangan berikutnya dapat mencakup:

* Validasi input yang lebih baik.
* Penanganan error yang lebih lengkap.
* Peningkatan struktur kode.
* Peningkatan tampilan terminal.
* Fitur pengelompokan berdasarkan topik.
* Fitur pencarian yang lebih fleksibel.

Pengembangan fitur dilakukan secara bertahap berdasarkan kebutuhan dan hasil evaluasi aplikasi, bukan dengan memasukkan seluruh fitur sejak awal.

---

# 13. Kriteria Keberhasilan

Versi awal Mini Knowledge Vault dianggap berhasil apabila pengguna dapat:

1. Menjalankan aplikasi melalui terminal.
2. Melihat menu utama.
3. Menambahkan sebuah catatan.
4. Melihat catatan yang telah ditambahkan.
5. Mencari catatan berdasarkan kata kunci.
6. Menghapus catatan.
7. Kembali ke menu utama setelah melakukan operasi.
8. Keluar dari aplikasi melalui menu yang tersedia.
9. Mendapatkan pesan yang sesuai ketika memasukkan pilihan yang tidak valid.

---

# 14. Ringkasan Kebutuhan

Secara keseluruhan, Mini Knowledge Vault merupakan aplikasi sederhana yang berfokus pada pengelolaan pengetahuan pribadi melalui terminal.

Ruang lingkup utama versi awal adalah:

```text
┌──────────────────────────────┐
│    MINI KNOWLEDGE VAULT      │
├──────────────────────────────┤
│ 1. Tambah Catatan            │
│ 2. Lihat Semua Catatan       │
│ 3. Cari Catatan              │
│ 4. Hapus Catatan             │
│ 5. Keluar                    │
└──────────────────────────────┘
```

Aplikasi dirancang dengan prinsip pengembangan bertahap. Versi awal dibuat sesederhana mungkin agar dapat digunakan sebagai media pembelajaran fundamental pemrograman. Fitur tambahan seperti edit dan penyimpanan permanen menggunakan JSON akan dikembangkan pada tahap berikutnya setelah versi dasar selesai.

Dokumen ini menjadi acuan untuk tahap selanjutnya, yaitu **perancangan algoritma dan flowchart aplikasi** sebelum masuk ke tahap implementasi program.

---

**Dokumen:** `docs/software-requirements.md`
**Project:** Mini Knowledge Vault
**Versi:** 1.0
:::
