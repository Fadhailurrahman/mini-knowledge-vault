# Mini Knowledge Vault

Mini Knowledge Vault adalah program sederhana berbasis terminal untuk menyimpan, melihat, mencari, menghapus, dan mengedit catatan pengetahuan yang diperoleh selama proses belajar.

Project ini dibuat sebagai media latihan untuk memahami fundamental pemrograman menggunakan Python.

Pengembangan dilakukan secara bertahap berdasarkan materi pembelajaran dan kebutuhan aplikasi.

---

## Project Status

**Version:** Module 4 — Exploration & Modification
**Status:** In Development
**Language:** Python
**Interface:** Command-Line Interface (CLI)

Pada tahap ini, aplikasi sudah memiliki fitur dasar untuk mengelola catatan.

Data masih disimpan di dalam memory selama program berjalan.

Data belum disimpan secara permanen ke file.

---

## Features

Versi saat ini memiliki fitur:

* Add knowledge
* View all knowledge
* Search knowledge
* Delete knowledge
* Edit knowledge
* Exit application

Fitur yang belum tersedia:

* Persistent storage
* File handling
* JSON
* Database
* Advanced error handling

Fitur tersebut akan dikembangkan secara bertahap pada tahap pembelajaran berikutnya.

---

## Project Structure

```text
mini-knowledge-vault/
│
├── main.py
├── README.md
└── docs/
    ├── requirements.md
    └── software-requirements.md
```

---

## How the Application Works

Ketika program dijalankan, pengguna akan melihat menu utama:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Edit catatan
6. Keluar

Pilih menu:
```

Pengguna dapat memilih menu sesuai kebutuhan.

---

### 1. Tambah Catatan

Pengguna dapat memasukkan:

* Topik
* Judul
* Isi catatan

Contoh:

```text
=== TAMBAH CATATAN ===

Topik    : Python
Judul    : List Comprehension
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.

Catatan berhasil disimpan!
```

Catatan disimpan ke dalam list `knowledge` sebagai sebuah dictionary.

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

Jika belum ada catatan:

```text
Belum ada catatan.
```

---

### 3. Cari Catatan

Pengguna dapat memasukkan kata kunci untuk mencari catatan.

Pencarian dilakukan berdasarkan:

* Topik
* Judul
* Isi catatan

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

Pengguna dapat memilih nomor catatan yang ingin dihapus.

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

Program melakukan validasi sederhana terhadap pilihan pengguna.

Jika pengguna memasukkan pilihan yang tidak valid:

```text
Pilihan tidak valid.
Masukkan nomor catatan.
```

Jika nomor tidak tersedia:

```text
Nomor catatan tidak ditemukan.
```

Fitur ini menggunakan method `.pop()` untuk menghapus data dari list.

---

### 5. Edit Catatan

Pengguna dapat memilih catatan yang ingin diubah.

Program akan menampilkan data lama terlebih dahulu.

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
Catatan  : Cara membuat list menggunakan sintaks yang lebih ringkas.

Catatan berhasil diperbarui!
```

Data dictionary kemudian diperbarui menggunakan value baru.

---

### 6. Keluar

Pengguna dapat memilih menu keluar untuk menghentikan aplikasi.

```text
Terima kasih telah menggunakan Mini Knowledge Vault.
Program selesai.
```

---

## Concepts Learned

Project ini digunakan untuk mempraktikkan fundamental Python.

### Variables

Digunakan untuk menyimpan nilai.

Contoh:

```python
topic = input("Topik    : ")
title = input("Judul    : ")
content = input("Catatan  : ")
```

---

### List

Digunakan untuk menyimpan kumpulan catatan.

```python
knowledge = []
```

Catatan baru ditambahkan menggunakan:

```python
knowledge.append(note)
```

---

### Dictionary

Digunakan untuk merepresentasikan sebuah catatan.

```python
note = {
    "topic": topic,
    "title": title,
    "content": content
}
```

---

### Function

Function digunakan untuk memisahkan program menjadi beberapa tugas.

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

```python
def delete_knowledge():
    ...
```

```python
def edit_knowledge():
    ...
```

Setiap function memiliki tanggung jawab tertentu.

---

### Conditional

Digunakan untuk mengambil keputusan berdasarkan kondisi.

Contoh:

```python
if choice == "1":
    add_knowledge()

elif choice == "2":
    view_knowledge()

elif choice == "3":
    search_knowledge()

elif choice == "4":
    delete_knowledge()

elif choice == "5":
    edit_knowledge()

elif choice == "6":
    break
```

---

### Loop

Program menggunakan `while` untuk menjaga menu tetap berjalan.

```python
while True:
    show_menu()
```

Program juga menggunakan `for` untuk melakukan iterasi terhadap kumpulan catatan.

```python
for note in knowledge:
    ...
```

---

### User Input

Program menerima input langsung dari pengguna melalui terminal.

```python
choice = input("Pilih menu: ")
```

---

### String Method

Program menggunakan `.lower()` untuk membuat pencarian tidak membedakan huruf besar dan kecil.

```python
keyword.lower()
```

Program juga menggunakan `.isdigit()` untuk memeriksa apakah input berisi angka.

```python
choice.isdigit()
```

---

### Number Conversion

Input dari `input()` selalu berupa string.

Untuk mengubah input menjadi integer:

```python
index = int(choice)
```

---

### List Index

Program menggunakan index untuk mengakses catatan tertentu.

Contoh:

```python
note = knowledge[index - 1]
```

`index - 1` digunakan karena nomor yang ditampilkan kepada pengguna dimulai dari `1`, sedangkan index list Python dimulai dari `0`.

---

### Delete Data

Program menggunakan `.pop()` untuk menghapus catatan berdasarkan index.

```python
deleted_note = knowledge.pop(index - 1)
```

Method tersebut menghapus data dari list dan mengembalikan data yang dihapus.

---

### Update Dictionary

Program dapat mengubah value dari dictionary.

Contoh:

```python
note["topic"] = topic
note["title"] = title
note["content"] = content
```

Konsep ini digunakan pada fitur Edit Knowledge.

---

## Data Storage

Pada versi saat ini, data masih disimpan di memory.

```python
knowledge = []
```

Artinya, data hanya tersedia selama program sedang berjalan.

Contohnya:

```text
Program berjalan
      ↓
knowledge = []
      ↓
Tambah catatan
      ↓
knowledge berisi data
      ↓
Edit / Delete / Search
      ↓
Program ditutup
      ↓
Data hilang
```

Pada tahap berikutnya, project akan mempelajari cara menyimpan data secara permanen menggunakan file dan JSON.

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
Modul 1
↓
Memahami kebutuhan aplikasi
↓
Modul 2
↓
Perencanaan aplikasi
↓
Modul 3
↓
Konsep dasar pemrograman
↓
Implementasi Add / View / Search / Exit
↓
Modul 4
↓
Eksplorasi & Modifikasi Aplikasi
↓
Delete Knowledge
↓
Edit Knowledge
↓
Next
↓
File Handling & JSON Persistence
↓
Next
↓
Improvement
↓
Modul 5
↓
Dokumentasi & Publish
```

---

## What I Learned

Pada tahap ini saya belajar dan mempraktikkan:

* Membuat variable.
* Menggunakan list.
* Menggunakan dictionary.
* Membuat dan memanggil function.
* Menerima input dari pengguna.
* Menampilkan output.
* Menggunakan `if`, `elif`, dan `else`.
* Menggunakan `while`.
* Menggunakan `for`.
* Menggunakan operator perbandingan.
* Menggunakan operator logika.
* Menggunakan string method.
* Menggunakan `.lower()`.
* Menggunakan `.isdigit()`.
* Mengubah string menjadi integer menggunakan `int()`.
* Mengakses data berdasarkan index.
* Menghapus data menggunakan `.pop()`.
* Mengubah value pada dictionary.
* Melakukan validasi input sederhana.
* Mengelola data sederhana di dalam memory.
* Memodifikasi aplikasi yang sudah dibuat sebelumnya.
* Memecah program menjadi beberapa function berdasarkan tugasnya.

---

## Module 4 — Exploration & Modification

Modul 4 berfokus pada kemampuan untuk mengevaluasi aplikasi yang sudah ada dan melakukan modifikasi berdasarkan kebutuhan.

Pada tahap ini aplikasi dikembangkan dengan menambahkan:

* Delete Knowledge.
* Edit Knowledge.
* Validasi pilihan catatan.
* Pengelolaan data yang sudah ada.

Proses pengembangan mengikuti pola:

```text
Aplikasi yang sudah ada
        ↓
Evaluasi
        ↓
Menemukan kebutuhan
        ↓
Menentukan perubahan
        ↓
Implementasi
        ↓
Pengujian
        ↓
Review
```

Tujuan utama tahap ini bukan membuat aplikasi menjadi kompleks, tetapi memahami bagaimana sebuah program dapat dikembangkan secara bertahap.

---

## Development Principle

Project ini tidak dibuat dengan tujuan memasukkan sebanyak mungkin fitur sejak awal.

Pengembangan dilakukan secara bertahap:

```text
Belajar
   ↓
Memahami konsep
   ↓
Praktik
   ↓
Menghubungkan konsep dengan project
   ↓
Membuat fitur
   ↓
Evaluasi
   ↓
Menemukan kebutuhan baru
   ↓
Memodifikasi aplikasi
   ↓
Menguji
   ↓
Review
   ↓
Dokumentasi
```

Dengan pendekatan tersebut, setiap perubahan pada aplikasi menjadi bagian dari proses belajar pemrograman.

Prinsip utama project:

> **Fitur ditambahkan karena ada kebutuhan atau karena menjadi bagian dari proses eksplorasi belajar, bukan karena ingin membuat aplikasi terlihat kompleks.**

---

## Future Development

Pengembangan berikutnya direncanakan secara bertahap.

### Version 3 — Persistent Storage

Menambahkan:

* File handling.
* JSON.
* Persistent storage.
* Membaca data dari file.
* Menulis data ke file.

Target penyimpanan:

```text
data.json
```

---

### Version 4 — Improvement

Kemungkinan pengembangan:

* Validasi input yang lebih baik.
* Error handling.
* Pencarian yang lebih fleksibel.
* Pengelompokan berdasarkan topik.
* Perbaikan struktur kode.
* Peningkatan tampilan terminal.
* Fitur tambahan berdasarkan kebutuhan project.

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

## Roadmap

```text
MODUL 1
Memahami Kebutuhan
        ↓
requirements.md
        ↓
MODUL 2
Perencanaan Aplikasi
        ↓
SRS / Planning
        ↓
MODUL 3
Konsep Dasar Pemrograman
        ↓
Python Fundamental
        ↓
Basic Knowledge Vault
        ↓
MODUL 4
Eksplorasi & Modifikasi
        ↓
Delete
        ↓
Edit
        ↓
File Handling
        ↓
JSON Persistence
        ↓
Improvement
        ↓
MODUL 5
Dokumentasi & Publish
```

---

## Author

**Fadhailurrahman**

Mini Knowledge Vault dibuat sebagai project pembelajaran untuk memahami fundamental pemrograman dan menerapkan konsep yang dipelajari ke dalam project nyata.
