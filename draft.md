# Project: Mini Knowledge Vault

## Konsep

Mini Knowledge Vault adalah program berbasis terminal untuk menyimpan, melihat, mencari, dan mengelola catatan pengetahuan yang diperoleh selama proses belajar.

Contoh penggunaan:

```text
=== MINI KNOWLEDGE VAULT ===

1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar

Pilih menu: 1

Topik    : Python
Judul    : List Comprehension
Catatan  : Cara membuat list dengan sintaks yang lebih ringkas.

Catatan berhasil disimpan!
```

Aplikasi dirancang sesederhana mungkin agar dapat digunakan sebagai media belajar fundamental pemrograman.

Pada tahap awal, aplikasi tidak membutuhkan:

* Login atau autentikasi.
* Database.
* Frontend atau antarmuka web.
* API.
* Koneksi internet.
* Framework.
* Sinkronisasi antarperangkat.
* Fitur kolaborasi.

---

# Pembagian Project Berdasarkan 5 Modul

Project Mini Knowledge Vault dikerjakan secara bertahap mengikuti proses belajar:

```text
Modul 1 → Memahami Kebutuhan Aplikasi
    ↓
Modul 2 → Perencanaan Aplikasi
    ↓
Modul 3 → Mengerti Konsep Dasar Pemrograman
    ↓
Modul 4 → Eksplorasi & Modifikasi Aplikasi
    ↓
Modul 5 → Dokumentasi & Publish
```

Setiap tahap memiliki tujuan dan hasil yang berbeda.

---

# 1. Memahami Kebutuhan Aplikasi

## Tujuan

Belajar memahami dan mendefinisikan masalah sebelum mulai coding.

Pada tahap ini belum membuat program.

Fokus utama adalah menjawab:

* Masalah apa yang ingin diselesaikan?
* Siapa pengguna aplikasi?
* Apa tujuan aplikasi?
* Fitur apa yang dibutuhkan?
* Input apa yang diberikan pengguna?
* Output apa yang dihasilkan aplikasi?
* Apa saja batasan aplikasi?

## Output Modul

```text
mini-knowledge-vault/
└── docs/
    └── requirements.md
```

Dokumen `requirements.md` berisi kebutuhan pengguna dan ruang lingkup awal aplikasi.

Contoh permasalahan:

> Saya membutuhkan tempat sederhana untuk menyimpan pengetahuan kecil yang saya dapat ketika belajar, sehingga saya tidak perlu mencari kembali catatan tersebut.

Pada tahap ini fokusnya adalah **memahami apa yang harus dibuat**, bukan bagaimana cara membuatnya.

---

# 2. Perencanaan Aplikasi

Setelah kebutuhan aplikasi dipahami, tahap berikutnya adalah merencanakan bagaimana aplikasi akan bekerja.

Pada tahap ini belum membuat implementasi program secara lengkap.

Kita mulai menerjemahkan requirement menjadi alur proses.

Contoh alur utama:

```text
Mulai
  ↓
Tampilkan Menu
  ↓
Pilih Menu
  ├── Tambah → Masukkan Data → Simpan
  ├── Lihat → Tampilkan Catatan
  ├── Cari → Masukkan Kata Kunci → Tampilkan Hasil
  ├── Hapus → Pilih Catatan → Hapus
  └── Keluar → Selesai
  ↓
Kembali ke Menu
```

Aplikasi akan terus kembali ke menu utama sampai pengguna memilih menu keluar.

## Output Modul

Repository mulai memiliki dokumentasi perencanaan:

```text
mini-knowledge-vault/
├── docs/
│   ├── requirements.md
│   └── flowchart.png
└── README.md
```

Flowchart digunakan untuk menggambarkan alur aplikasi sebelum diterjemahkan menjadi kode.

Pada tahap ini fokusnya adalah:

> **Memahami bagaimana program akan berjalan sebelum menulis kode.**

---

# 3. Mengerti Konsep Dasar Pemrograman

Pada tahap ini kita mulai masuk ke implementasi program.

Tujuan utamanya bukan membuat aplikasi yang kompleks, tetapi menggunakan project sebagai media untuk memahami fundamental pemrograman.

Implementasi awal menggunakan Python.

Struktur paling sederhana:

```text
mini-knowledge-vault/
├── main.py
└── README.md
```

Pada versi awal, data belum perlu disimpan secara permanen ke file.

Secara konseptual, data dapat disimpan sementara di dalam program:

```python
knowledge = []
```

Kemudian program mulai dikembangkan menggunakan konsep fundamental seperti:

* Variable.
* String.
* Number.
* Boolean.
* List.
* Dictionary.
* Function.
* Conditional statement.
* `if`.
* `elif`.
* `else`.
* `for`.
* `while`.
* Input.
* Output.
* Operator perbandingan.
* Operator logika.

Contoh pembagian fungsi:

```text
add_knowledge()
view_knowledge()
search_knowledge()
delete_knowledge()
```

Setiap fungsi memiliki tanggung jawab tertentu sehingga kode dapat dipahami dan dikembangkan secara bertahap.

## Fokus Modul

Pada tahap ini fokus utama adalah:

> **Memahami konsep fundamental melalui masalah nyata yang ada di dalam project.**

Kita tidak langsung menggunakan framework atau teknologi tambahan.

---

# 4. Eksplorasi & Modifikasi Aplikasi

Setelah versi dasar selesai, kita mulai mengevaluasi aplikasi dan bertanya:

> "Apa yang bisa saya eksplorasi atau tingkatkan dari program ini?"

Fitur tambahan tidak harus ditentukan seluruhnya sejak awal.

Pengembangan dilakukan berdasarkan:

* kebutuhan aplikasi,
* konsep yang sedang dipelajari,
* masalah yang ditemukan,
* dan hal-hal yang ingin dieksplorasi.

## Versi 1 — Basic Knowledge Vault

Fitur:

```text
1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Keluar
```

Fokus utama:

* Variable.
* List.
* Dictionary.
* Function.
* Conditional.
* Loop.
* Input dan output.

---

## Versi 2 — Edit Feature

Setelah versi dasar stabil, kita dapat menambahkan kemampuan untuk mengubah catatan yang sudah ada.

Fitur menjadi:

```text
1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Edit catatan
6. Keluar
```

Fokus pembelajaran:

* Mencari data tertentu.
* Mengubah data.
* Mengelola data yang sudah ada.
* Memahami alur perubahan data.

Fitur edit tidak menjadi bagian dari implementasi awal karena sengaja ditunda sebagai bahan eksplorasi berikutnya.

---

## Versi 3 — Persistent Storage

Setelah memahami penyimpanan data di dalam memory, kita dapat mengeksplorasi bagaimana membuat data tetap tersedia setelah program ditutup.

Program yang sebelumnya menggunakan:

```python
knowledge = []
```

dikembangkan agar dapat menyimpan data ke file:

```text
data.json
```

Struktur project menjadi:

```text
mini-knowledge-vault/
├── main.py
├── data.json
└── README.md
```

Fokus pembelajaran:

* File handling.
* Membaca file.
* Menulis file.
* JSON.
* Mengubah data Python menjadi JSON.
* Membaca kembali data JSON ke dalam program.

---

## Versi Berikutnya — Improvement

Setelah fitur dasar selesai, pengembangan berikutnya dapat dilakukan berdasarkan kebutuhan dan hasil eksplorasi.

Contohnya:

* Validasi input yang lebih baik.
* Error handling yang lebih baik.
* Pencarian yang lebih fleksibel.
* Pengelompokan catatan berdasarkan topik.
* Perbaikan struktur kode.
* Peningkatan tampilan terminal.
* Fitur tambahan lain yang muncul selama proses belajar.

Tidak semua fitur harus dibuat.

Prinsip utama project adalah:

> **Fitur ditambahkan karena ada kebutuhan atau karena menjadi bagian dari proses eksplorasi belajar, bukan karena ingin membuat aplikasi terlihat kompleks.**

---

# 5. Dokumentasi & Publish

Setelah aplikasi selesai dikembangkan dan cukup stabil, repository dirapikan agar dapat digunakan sebagai dokumentasi perjalanan belajar.

Struktur akhir yang direncanakan:

```text
mini-knowledge-vault/
│
├── README.md
├── main.py
├── data.json
│
└── docs/
    ├── requirements.md
    └── flowchart.png
```

Tidak semua file harus langsung tersedia sejak awal.

`data.json`, misalnya, baru muncul setelah aplikasi memiliki fitur persistent storage.

## README

README menjelaskan secara singkat:

```text
# Mini Knowledge Vault

Program sederhana berbasis terminal untuk menyimpan
dan mengelola catatan pengetahuan.

## Features

- Add knowledge
- View knowledge
- Search knowledge
- Delete knowledge
- Edit knowledge

## Technologies

- Python

## How to Run

python main.py
```

Setelah proses belajar selesai, README juga dapat memiliki bagian:

```text
## What I Learned

- Working with lists and dictionaries
- Creating reusable functions
- Handling user input
- Using conditional statements
- Working with loops
- Reading and writing JSON files
- Basic error handling
```

Bagian ini penting karena repository tidak hanya menunjukkan hasil akhir aplikasi, tetapi juga menunjukkan **apa yang dipelajari selama proses pengembangan**.

---

# Struktur Project Secara Bertahap

## Tahap Modul 1

```text
mini-knowledge-vault/
└── docs/
    └── requirements.md
```

## Tahap Modul 2

```text
mini-knowledge-vault/
├── docs/
│   ├── requirements.md
│   └── flowchart.png
└── README.md
```

## Tahap Modul 3

```text
mini-knowledge-vault/
├── main.py
├── README.md
└── docs/
    ├── requirements.md
    └── flowchart.png
```

## Tahap Persistent Storage

```text
mini-knowledge-vault/
├── main.py
├── data.json
├── README.md
└── docs/
    ├── requirements.md
    └── flowchart.png
```

---

# Perjalanan Commit

Commit tidak perlu dibuat sebanyak mungkin.

Yang penting setiap commit merepresentasikan perubahan yang benar-benar dilakukan.

Contoh perjalanan:

```text
Initial project
↓
Define application requirements
↓
Add software requirements
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
Add edit feature
↓
Add JSON persistence
↓
Improve error handling
↓
Add documentation
```

Tidak semua commit tersebut harus dibuat.

Jika dalam prosesnya beberapa perubahan memang dilakukan sekaligus, satu commit dapat mewakili beberapa perubahan yang saling berkaitan.

Prinsipnya:

> **Commit harus menggambarkan perjalanan pengembangan yang nyata, bukan mengejar jumlah commit.**

---

# Prinsip Utama Project

Mini Knowledge Vault bukan hanya project untuk menghasilkan aplikasi terminal.

Project ini digunakan sebagai **media belajar pemrograman**.

Alur belajar yang digunakan:

```text
Belajar konsep
    ↓
Pahami konsep
    ↓
Praktik kecil
    ↓
Hubungkan dengan project
    ↓
Implementasikan
    ↓
Temukan masalah
    ↓
Eksplorasi solusi
    ↓
Modifikasi project
    ↓
Review
    ↓
Dokumentasikan
```

Karena itu, aplikasi tidak perlu langsung memiliki banyak fitur.

Kita mulai dari masalah sederhana, membuat solusi sederhana, kemudian mengembangkan aplikasi seiring bertambahnya pemahaman.

---

# Roadmap Keseluruhan

```text
MODUL 1
Memahami Kebutuhan
        ↓
requirements.md
        ↓
MODUL 2
Perencanaan Aplikasi
        ↓
Flowchart + Algorithm
        ↓
MODUL 3
Konsep Dasar Pemrograman
        ↓
Python Fundamental
        ↓
Mini Knowledge Vault V1
        ↓
MODUL 4
Eksplorasi & Modifikasi
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
        ↓
README
        ↓
Review Project
        ↓
GitHub Repository
```

## Prinsip Belajar

> **Jangan langsung coding.**

Kita mengikuti urutan:

**Requirement → Planning → Algorithm → Flowchart → Coding → Eksplorasi → Dokumentasi**

Dengan demikian, setiap tahap memiliki tujuan yang jelas dan setiap perubahan pada aplikasi dapat dikaitkan dengan proses belajar yang sedang dilakukan.
