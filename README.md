# Mini Knowledge Vault

Mini Knowledge Vault adalah aplikasi sederhana berbasis terminal (CLI) untuk menyimpan dan mengelola catatan pengetahuan yang diperoleh selama proses belajar.

Aplikasi ini dibuat menggunakan Python dengan tujuan menyediakan tempat sederhana untuk menambahkan, melihat, mencari, menghapus, dan mengedit catatan pengetahuan.

Project ini dikembangkan sebagai project pembelajaran setelah mempelajari dan menyelesaikan kelas **Memulai Dasar Pemrograman untuk Menjadi Pengembang Software** dari Dicoding.

---

## Features

Mini Knowledge Vault menyediakan fitur:

- Menambahkan catatan.
- Melihat seluruh catatan.
- Mencari catatan.
- Menghapus catatan.
- Mengedit catatan.
- Keluar dari aplikasi.

Setiap catatan memiliki:

- Topik.
- Judul.
- Isi catatan.

---

## Preview

Ketika aplikasi dijalankan, pengguna akan melihat menu utama:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Edit catatan
6. Keluar

Pilih menu:
````

---

## How It Works

### 1. Tambah Catatan

Pengguna dapat menambahkan catatan baru dengan memasukkan topik, judul, dan isi catatan.

Contoh:

```text
=== TAMBAH CATATAN ===

Topik    : Python
Judul    : List Comprehension
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.

Catatan berhasil disimpan!
```

Catatan kemudian disimpan ke dalam list selama aplikasi sedang berjalan.

---

### 2. Lihat Semua Catatan

Pengguna dapat melihat seluruh catatan yang telah ditambahkan.

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

Jika belum terdapat catatan:

```text
Belum ada catatan.
```

---

### 3. Cari Catatan

Pengguna dapat mencari catatan menggunakan kata kunci.

Pencarian dilakukan pada:

* Topik.
* Judul.
* Isi catatan.

Pencarian tidak membedakan huruf besar dan huruf kecil.

Contoh:

```text
=== CARI CATATAN ===

Masukkan kata kunci: Python

=== HASIL PENCARIAN ===

[1]
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.
```

Jika tidak ditemukan:

```text
Catatan tidak ditemukan.
```

---

### 4. Hapus Catatan

Pengguna dapat menghapus catatan berdasarkan nomor yang ditampilkan pada daftar.

Contoh:

```text
=== HAPUS CATATAN ===

[1]
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.

Pilih nomor catatan yang ingin dihapus: 1

Catatan berhasil dihapus!
Judul: List Comprehension
```

Program melakukan validasi sederhana untuk memastikan nomor catatan yang dimasukkan tersedia.

---

### 5. Edit Catatan

Pengguna dapat memilih catatan yang ingin diperbarui.

Program akan menampilkan data yang sedang tersimpan sebelum meminta data baru.

Contoh:

```text
=== EDIT CATATAN ===

[1]
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.

Pilih nomor catatan yang ingin diedit: 1

=== DATA CATATAN SAAT INI ===
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.

=== MASUKKAN DATA BARU ===
Topik    : Python
Judul    : List Comprehension Dasar
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.

Catatan berhasil diperbarui!
```

---

### 6. Keluar

Pengguna dapat memilih menu keluar untuk menghentikan aplikasi.

```text
Terima kasih telah menggunakan Mini Knowledge Vault.
Program selesai.
```

---

## Data Storage

Pada versi saat ini, catatan disimpan sementara di dalam memory menggunakan list Python:

```python
knowledge = []
```

Setiap catatan direpresentasikan menggunakan dictionary:

```python
note = {
    "topic": topic,
    "title": title,
    "content": content
}
```

Karena data masih disimpan di memory, seluruh catatan akan hilang ketika program ditutup.

Persistent storage menggunakan file belum menjadi bagian dari versi saat ini.

---

## Technologies

* Python
* Command-Line Interface (CLI)

Project tidak menggunakan:

* Framework.
* Database.
* API.
* Internet connection.
* Web interface.
* Authentication.

---

## Project Structure

```text
mini-knowledge-vault/
│
├── main.py
├── README.md
│
└── docs/
    ├── requirements.md
    └── software-requirements.md
```

---

## How to Run

Pastikan Python telah terinstall pada komputer.

Jalankan aplikasi menggunakan terminal:

```bash
python main.py
```

Pada beberapa sistem, Python dapat dijalankan menggunakan:

```bash
python3 main.py
```

---

## Concepts

Project ini menggunakan beberapa konsep dasar Python, antara lain:

* Variables.
* Strings.
* Lists.
* Dictionaries.
* Functions.
* Conditional statements.
* `if`, `elif`, dan `else`.
* `for` loop.
* `while` loop.
* User input.
* String methods.
* Type conversion.
* List indexing.
* Menambah dan menghapus data dari list.
* Memperbarui data pada dictionary.
* Validasi input sederhana.

---

## Project Purpose

Mini Knowledge Vault dibuat sebagai aplikasi sederhana untuk menerapkan konsep dasar pemrograman ke dalam sebuah project yang dapat digunakan secara nyata.

Fokus project bukan pada jumlah fitur atau kompleksitas aplikasi, tetapi pada pembuatan solusi yang sederhana, mudah dipahami, dan dapat dikembangkan secara bertahap.

---

## Current Limitations

Versi saat ini memiliki beberapa batasan:

* Data belum disimpan secara permanen.
* Data akan hilang ketika program ditutup.
* Aplikasi hanya berjalan melalui terminal.
* Belum memiliki database.
* Belum memiliki sistem akun atau autentikasi.
* Validasi input masih sederhana.

Batasan tersebut dapat dikembangkan pada versi berikutnya apabila diperlukan.

---

## Future Development

Pengembangan berikutnya dapat mencakup:

* Persistent storage.
* File handling.
* JSON.
* Validasi input yang lebih baik.
* Error handling.
* Pencarian yang lebih fleksibel.
* Pengelompokan catatan berdasarkan topik.
* Perbaikan struktur kode.
* Peningkatan tampilan terminal.

Pengembangan akan dilakukan berdasarkan kebutuhan project dan konsep yang ingin dipelajari.

---

## Documentation

Dokumentasi kebutuhan dan spesifikasi aplikasi tersedia di:

```text
docs/
├── requirements.md
└── software-requirements.md
```

---

## Author

**Moh. Fadhailurrahman**

Mini Knowledge Vault merupakan project pembelajaran untuk memahami dan menerapkan fundamental pemrograman menggunakan Python.
