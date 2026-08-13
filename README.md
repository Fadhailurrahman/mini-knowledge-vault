# Mini Knowledge Vault

Mini Knowledge Vault adalah program sederhana berbasis terminal untuk menyimpan, melihat, dan mencari catatan pengetahuan yang diperoleh selama proses belajar.

Project ini dibuat sebagai media latihan untuk memahami fundamental pemrograman menggunakan Python.

---

## Project Status

**Version:** Day 3 — Basic Version  
**Status:** In Development  
**Language:** Python  
**Interface:** Command-Line Interface (CLI)

Pada tahap ini, data masih disimpan di dalam memory selama program berjalan.

Data belum disimpan secara permanen ke file.

---

## Features

Versi saat ini memiliki beberapa fitur dasar:

- Add knowledge
- View all knowledge
- Search knowledge
- Exit application

Fitur berikut belum tersedia pada versi ini:

- Delete knowledge
- Edit knowledge
- Persistent storage
- JSON
- Database

Fitur tersebut akan dikembangkan secara bertahap pada tahap pembelajaran berikutnya.

---

## Project Structure

```text
mini-knowledge-vault/
│
├── main.py
└── README.md
```

---

## How the Application Works

Ketika program dijalankan, pengguna akan melihat menu utama:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Keluar

Pilih menu:
```

Pengguna dapat memilih menu sesuai kebutuhan.

### 1. Tambah Catatan

Pengguna dapat memasukkan:

- Topik
- Judul
- Isi catatan

Contoh:

```text
=== TAMBAH CATATAN ===

Topik    : Python
Judul    : List Comprehension
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.

Catatan berhasil disimpan!
```

---

### 2. Lihat Semua Catatan

Program akan menampilkan seluruh catatan yang telah ditambahkan selama program berjalan.

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

---

### 3. Cari Catatan

Pengguna dapat memasukkan kata kunci untuk mencari catatan.

Pencarian dilakukan berdasarkan:

- Topik
- Judul
- Isi catatan

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

---

### 4. Keluar

Pengguna dapat memilih menu keluar untuk menghentikan program.

```text
Terima kasih telah menggunakan Mini Knowledge Vault.
Program selesai.
```

---

## Concepts Learned

Project ini digunakan untuk mempraktikkan beberapa fundamental Python.

### Variables

Digunakan untuk menyimpan nilai.

Contoh:

```python
topic = input("Topik    : ")
title = input("Judul    : ")
content = input("Catatan  : ")
```

### List

Digunakan untuk menyimpan kumpulan catatan.

```python
knowledge = []
```

### Dictionary

Digunakan untuk merepresentasikan sebuah catatan.

```python
note = {
    "topic": topic,
    "title": title,
    "content": content
}
```

### Function

Digunakan untuk memisahkan program menjadi beberapa tugas.

Contoh:

```python
def add_knowledge():
    ...
```

```python
def view_knowledge():
    ...
```

```python
def search_knowledge():
    ...
```

### Conditional

Digunakan untuk mengambil keputusan berdasarkan kondisi.

```python
if choice == "1":
    add_knowledge()
elif choice == "2":
    view_knowledge()
elif choice == "3":
    search_knowledge()
else:
    ...
```

### Loop

Program menggunakan `while` untuk menjaga menu tetap berjalan.

```python
while True:
    ...
```

Program juga menggunakan `for` untuk melakukan iterasi terhadap kumpulan catatan.

```python
for note in knowledge:
    ...
```

### User Input

Program menerima input langsung dari pengguna melalui terminal.

```python
input("Pilih menu: ")
```

---

## Data Storage

Pada versi Day 3, data hanya disimpan di memory.

```python
knowledge = []
```

Artinya, ketika program dihentikan, seluruh catatan akan hilang.

Contoh:

```text
Program berjalan
      ↓
knowledge = []
      ↓
Tambah catatan
      ↓
knowledge berisi data
      ↓
Program ditutup
      ↓
Data hilang
```

Penyimpanan permanen menggunakan JSON akan dipelajari pada tahap pengembangan berikutnya.

---

## How to Run

Pastikan Python sudah terinstall.

Jalankan program melalui terminal:

```bash
python main.py
```

Jika sistem menggunakan `python3`:

```bash
python3 main.py
```

---

## Learning Progress

Project ini dikembangkan secara bertahap mengikuti proses belajar.

```text
Day 1
↓
Memahami kebutuhan aplikasi
↓
Day 2
↓
Membuat spesifikasi dan perencanaan
↓
Day 3
↓
Implementasi fundamental Python
↓
Next
↓
Menambahkan fitur Delete
↓
Next
↓
Menambahkan fitur Edit
↓
Next
↓
File Handling & JSON
```

---

## What I Learned

Pada tahap ini saya belajar dan mempraktikkan:

- Membuat variable.
- Menggunakan list.
- Menggunakan dictionary.
- Membuat dan memanggil function.
- Menerima input dari pengguna.
- Menampilkan output.
- Menggunakan `if`, `elif`, dan `else`.
- Menggunakan `while`.
- Menggunakan `for`.
- Menggunakan operator perbandingan.
- Menggunakan operator logika.
- Mengelola data sederhana di dalam memory.
- Memecah program menjadi beberapa function berdasarkan tugasnya.

---

## Development Principle

Project ini tidak dibuat dengan tujuan memasukkan sebanyak mungkin fitur sejak awal.

Pengembangan dilakukan secara bertahap:

```text
Belajar
   ↓
Praktik
   ↓
Membuat fitur sederhana
   ↓
Evaluasi
   ↓
Menemukan kebutuhan baru
   ↓
Mempelajari konsep baru
   ↓
Memodifikasi aplikasi
```

Dengan pendekatan tersebut, setiap perubahan pada aplikasi menjadi bagian dari proses belajar pemrograman.

---

## Future Development

Pengembangan berikutnya direncanakan secara bertahap:

### Version 2

Menambahkan:

- Delete knowledge
- Validasi pilihan catatan

### Version 3

Menambahkan:

- Edit knowledge

### Version 4

Menambahkan:

- File handling
- JSON
- Persistent storage

### Version 5

Kemungkinan pengembangan:

- Validasi input yang lebih baik
- Error handling
- Pencarian yang lebih fleksibel
- Pengelompokan berdasarkan topik
- Perbaikan struktur kode
- Peningkatan tampilan terminal

Fitur dapat berubah sesuai dengan kebutuhan dan hasil eksplorasi selama proses belajar.

---

## Documentation

Dokumentasi project:

```text
docs/
├── requirements.md
└── software-requirements.md
```

Dokumen tersebut berisi kebutuhan dan spesifikasi aplikasi sebelum proses implementasi.

---

## Author

**Fadhailurrahman**

Mini Knowledge Vault dibuat sebagai project pembelajaran untuk memahami fundamental pemrograman dan menerapkan konsep yang dipelajari ke dalam project nyata.
