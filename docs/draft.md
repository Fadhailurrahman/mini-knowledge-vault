# Project: Mini Knowledge Vault

## Konsep

Mini Knowledge Vault adalah program terminal sederhana untuk menyimpan,
melihat, mencari, dan mengelola catatan pengetahuan yang diperoleh selama belajar.

Program ini dibuat sebagai media praktik untuk menerapkan konsep dasar
pemrograman secara bertahap.

Program tidak menggunakan login, database, frontend, API, framework,
atau teknologi yang kompleks.

Contoh penggunaan:

=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar

Pilih menu: 1

Topik    : JavaScript
Judul    : Variabel
Catatan  : Variabel digunakan untuk menyimpan sebuah nilai.

Catatan berhasil disimpan!


==================================================
MODUL 1 — MEMAHAMI KEBUTUHAN APLIKASI
==================================================

Tujuan:
Belajar memahami masalah dan menentukan kebutuhan aplikasi sebelum
mulai membuat kode.

Pada tahap ini belum membuat program.

Yang perlu ditentukan:

- Masalah yang ingin diselesaikan
- Siapa pengguna aplikasi
- Tujuan aplikasi
- Fitur utama
- Input yang dibutuhkan
- Output yang dihasilkan
- Batasan aplikasi

Masalah:

Ketika belajar pemrograman, kita sering mendapatkan berbagai informasi
kecil yang penting. Jika informasi tersebut hanya disimpan di berbagai
tempat, akan sulit untuk mencarinya kembali.

Solusi:

Membuat program sederhana yang dapat digunakan untuk menyimpan
pengetahuan atau catatan belajar secara terstruktur.

Tujuan:

Membuat tempat sederhana untuk menyimpan pengetahuan kecil yang
didapat selama belajar sehingga catatan tersebut dapat dicari dan
digunakan kembali dengan mudah.

Target pengguna:

Pelajar atau siapa saja yang sedang mempelajari pemrograman dan ingin
menyimpan catatan pengetahuan secara sederhana.

Fitur utama:

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar dari program

Input:

- Topik
- Judul
- Isi catatan
- Pilihan menu
- Kata kunci pencarian
- Identitas catatan yang ingin dihapus

Output:

- Daftar catatan
- Hasil pencarian
- Pesan keberhasilan
- Pesan kesalahan
- Menu aplikasi

Batasan:

- Berbasis terminal
- Tidak menggunakan database
- Tidak menggunakan frontend
- Tidak menggunakan API
- Tidak menggunakan login
- Tidak menggunakan framework
- Pada tahap awal data hanya disimpan selama program berjalan


==================================================
MODUL 2 — PERENCANAAN APLIKASI
==================================================

Tujuan:
Menentukan bagaimana aplikasi akan bekerja sebelum implementasi.

Flow utama:

Mulai
  ↓
Tampilkan Menu
  ↓
Pilih Menu
  │
  ├── 1. Tambah Catatan
  │       ↓
  │     Input data
  │       ↓
  │     Simpan catatan
  │       ↓
  │     Kembali ke menu
  │
  ├── 2. Lihat Catatan
  │       ↓
  │     Tampilkan semua catatan
  │       ↓
  │     Kembali ke menu
  │
  ├── 3. Cari Catatan
  │       ↓
  │     Input kata kunci
  │       ↓
  │     Cari catatan
  │       ↓
  │     Tampilkan hasil
  │       ↓
  │     Kembali ke menu
  │
  ├── 4. Hapus Catatan
  │       ↓
  │     Pilih catatan
  │       ↓
  │     Hapus catatan
  │       ↓
  │     Kembali ke menu
  │
  └── 5. Keluar
          ↓
        Selesai


Struktur repository tahap perencanaan:

mini-knowledge-vault/
│
├── README.md
│
└── docs/
    ├── requirements.md
    └── flowchart.png


Pada tahap ini belum perlu membuat program secara lengkap.


==================================================
MODUL 3 — MENGERTI KONSEP DASAR PEMROGRAMAN
==================================================

Tujuan:
Mulai membuat program dengan menerapkan fundamental pemrograman.

Versi awal dibuat sesederhana mungkin.

Struktur:

mini-knowledge-vault/
│
├── main.py
└── README.md


Data awal:

knowledge = []


Konsep yang akan dipraktikkan:

- Variable
- Tipe data
- List
- Dictionary
- Function
- Input
- Output
- If / else
- For
- While
- Operator
- Logika pemrograman


Contoh struktur data:

knowledge = [
    {
        "topic": "JavaScript",
        "title": "Variabel",
        "note": "Variabel digunakan untuk menyimpan nilai."
    }
]


Function yang akan dibuat secara bertahap:

add_knowledge()
view_knowledge()
search_knowledge()
delete_knowledge()


Alur program:

while program masih berjalan:

    tampilkan menu

    minta pilihan pengguna

    jika pilihan = 1:
        tambah catatan

    jika pilihan = 2:
        tampilkan catatan

    jika pilihan = 3:
        cari catatan

    jika pilihan = 4:
        hapus catatan

    jika pilihan = 5:
        keluar

    selain itu:
        tampilkan pesan pilihan tidak valid


Tujuan utama modul ini bukan membuat program yang sempurna.

Tujuannya adalah memahami bagaimana konsep fundamental pemrograman
digunakan untuk membangun sebuah program nyata.


==================================================
MODUL 4 — MODIFIKASI DAN EKSPLORASI
==================================================

Tujuan:
Mengembangkan program berdasarkan konsep baru yang dipelajari.

Pengembangan dilakukan secara bertahap.

Tidak perlu langsung membuat semua fitur.


VERSI 1

Fitur:

- Tambah catatan
- Lihat catatan
- Cari catatan


VERSI 2

Tambahkan:

- Hapus catatan


VERSI 3

Tambahkan:

- Edit catatan


VERSI 4

Mulai mempelajari file handling.

Data yang sebelumnya hanya:

knowledge = []

mulai disimpan ke:

data.json


Contoh:

{
    "knowledge": [
        {
            "topic": "JavaScript",
            "title": "Variabel",
            "note": "Variabel digunakan untuk menyimpan nilai."
        }
    ]
}


Pengembangan berikutnya dapat dilakukan berdasarkan materi yang
dipelajari.

Contoh eksplorasi:

- File handling
- JSON
- Error handling
- Validasi input
- Pencarian yang lebih baik
- Pengurutan catatan
- Filter berdasarkan topik
- Dan konsep lain yang relevan


Prinsip pengembangan:

Jangan membuat fitur hanya karena ingin program terlihat kompleks.

Fitur ditambahkan karena ada kebutuhan atau karena menjadi kesempatan
untuk mempraktikkan konsep yang sedang dipelajari.


==================================================
MODUL 5 — DOKUMENTASI DAN PUBLISH
==================================================

Tujuan:
Merapikan project dan mendokumentasikan proses pembelajaran.

Struktur akhir:

mini-knowledge-vault/
│
├── README.md
├── main.py
├── data.json
│
└── docs/
    ├── requirements.md
    └── flowchart.png


README.md dapat berisi:

# Mini Knowledge Vault

Program sederhana berbasis terminal untuk menyimpan dan mengelola
catatan pengetahuan selama proses belajar.

## Features

- Add knowledge
- View knowledge
- Search knowledge
- Edit knowledge
- Delete knowledge

## Technologies

- Python

## How to Run

```bash
python main.py
````

## What I Learned

* Menggunakan variable
* Menggunakan list dan dictionary
* Membuat function
* Menggunakan conditional statement
* Menggunakan looping
* Mengolah input pengguna
* Membaca dan menulis file JSON
* Melakukan validasi input
* Basic error handling

==================================================
RIWAYAT COMMIT
==============

Commit tidak perlu banyak.

Yang penting setiap commit merepresentasikan perubahan yang benar-benar
dilakukan.

Contoh:

Initial project
↓
Define application requirements
↓
Add application flowchart
↓
Implement basic knowledge storage
↓
Add view knowledge feature
↓
Add search feature
↓
Add delete feature
↓
Add edit knowledge feature
↓
Add JSON persistence
↓
Improve input validation
↓
Improve error handling
↓
Update documentation

==================================================
TUJUAN UTAMA PROJECT
====================

Project ini bukan dibuat untuk menghasilkan aplikasi yang kompleks.

Project ini dibuat sebagai media belajar untuk mengubah teori
pemrograman menjadi praktik.

Urutan pembelajaran:

Memahami kebutuhan
↓
Merencanakan program
↓
Memahami fundamental
↓
Menulis kode
↓
Menguji program
↓
Menemukan masalah
↓
Memodifikasi program
↓
Mempelajari konsep baru
↓
Menerapkan konsep baru
↓
Mendokumentasikan hasil

PRINSIP:

Jangan langsung mengejar aplikasi yang kompleks.

Mulai dari program sederhana.

Pahami setiap kode yang ditulis.

Jika menemukan konsep yang belum dipahami, pelajari konsep tersebut.

Kemudian kembali ke project dan coba terapkan.

Dengan begitu, project berkembang mengikuti proses belajar,
bukan proses belajar dipaksa mengikuti project.

==================================================
HUBUNGAN DENGAN PEMBELAJARAN
============================

Project Mini Knowledge Vault digunakan sebagai project praktik
untuk menerapkan konsep pemrograman secara bertahap.

Konsep yang nantinya dapat diterapkan:

Variable
↓
Tipe Data
↓
Operator
↓
Input / Output
↓
Function
↓
Conditional
↓
Looping
↓
List / Dictionary
↓
File Handling
↓
JSON
↓
Error Handling
↓
Konsep lanjutan

TARGET AKHIR:

Saya tidak hanya memiliki sebuah program yang dapat dijalankan,
tetapi juga memahami bagaimana program tersebut dibuat,
mengapa kode tersebut dibuat dengan cara tersebut, dan konsep
pemrograman apa yang saya pelajari dari proses pembuatannya.

**Catatan penting:** saya sengaja mempertahankan struktur **5 tahap/modul project** yang Anda berikan, meskipun sebelumnya Anda menyebut ada **4 modul materi pembelajaran**. Jadi keduanya tidak saya campur: **4 modul = materi yang Anda pelajari**, sedangkan **5 modul = tahapan pengerjaan Mini Knowledge Vault**.
