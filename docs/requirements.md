# Mini Knowledge Vault — User Requirements

## 1. Overview

Mini Knowledge Vault adalah aplikasi berbasis terminal yang digunakan untuk menyimpan dan mengelola catatan pengetahuan pribadi.

Aplikasi ditujukan untuk pengguna yang membutuhkan tempat sederhana untuk mencatat informasi yang diperoleh selama proses belajar dan melihatnya kembali ketika diperlukan.

---

## 2. Purpose

Tujuan utama aplikasi adalah menyediakan cara sederhana bagi pengguna untuk:

- Menyimpan catatan pengetahuan.
- Melihat catatan yang telah dibuat.
- Mencari catatan tertentu.
- Menghapus catatan yang tidak diperlukan.
- Mengubah catatan yang perlu diperbarui.

Aplikasi dibuat dengan pendekatan sederhana tanpa bergantung pada database, server, atau layanan eksternal.

---

## 3. Target User

Aplikasi ditujukan untuk:

- Pelajar.
- Pemula yang sedang belajar pemrograman.
- Individu yang ingin menyimpan catatan pengetahuan pribadi.

Pada versi saat ini, aplikasi digunakan oleh satu pengguna.

---

## 4. User Requirements

Sebagai pengguna, saya ingin:

1. Menambahkan catatan pengetahuan baru agar informasi yang saya pelajari dapat disimpan.
2. Melihat seluruh catatan agar saya dapat meninjau kembali informasi yang pernah disimpan.
3. Mencari catatan berdasarkan kata kunci agar informasi tertentu dapat ditemukan dengan lebih mudah.
4. Menghapus catatan yang sudah tidak diperlukan.
5. Mengedit catatan apabila terdapat informasi yang perlu diperbaiki atau diperbarui.
6. Keluar dari aplikasi ketika sudah selesai menggunakannya.

---

## 5. Information Stored

Setiap catatan memiliki tiga informasi utama:

| Field | Description |
|---|---|
| Topik | Kategori atau bidang dari catatan |
| Judul | Judul catatan |
| Isi Catatan | Informasi atau penjelasan yang disimpan |

Contoh:

```text
Topik   : Python
Judul   : List Comprehension
Catatan : Cara membuat list dengan sintaks yang lebih ringkas.
````

---

## 6. Functional Requirements

### FR-01 — Add Knowledge

Aplikasi harus memungkinkan pengguna menambahkan catatan baru.

Data yang dimasukkan:

* Topik.
* Judul.
* Isi catatan.

Catatan baru harus disimpan selama aplikasi sedang berjalan.

---

### FR-02 — View Knowledge

Aplikasi harus memungkinkan pengguna melihat seluruh catatan yang tersedia.

Setiap catatan harus ditampilkan dengan informasi:

* Nomor catatan.
* Topik.
* Judul.
* Isi catatan.

Jika belum ada catatan, aplikasi harus memberikan informasi kepada pengguna.

---

### FR-03 — Search Knowledge

Aplikasi harus memungkinkan pengguna mencari catatan menggunakan kata kunci.

Pencarian dilakukan terhadap:

* Topik.
* Judul.
* Isi catatan.

Pencarian tidak membedakan huruf besar dan huruf kecil.

Jika tidak terdapat hasil yang sesuai, aplikasi harus memberikan informasi bahwa catatan tidak ditemukan.

---

### FR-04 — Delete Knowledge

Aplikasi harus memungkinkan pengguna menghapus catatan berdasarkan nomor catatan.

Aplikasi harus memeriksa input pengguna sebelum melakukan penghapusan.

Jika nomor tidak valid atau tidak tersedia, data tidak boleh dihapus.

---

### FR-05 — Edit Knowledge

Aplikasi harus memungkinkan pengguna mengubah catatan yang telah tersedia.

Pengguna memilih catatan berdasarkan nomor, kemudian memasukkan data baru untuk:

* Topik.
* Judul.
* Isi catatan.

---

### FR-06 — Exit Application

Aplikasi harus menyediakan pilihan untuk keluar dari program.

Ketika pengguna memilih menu keluar, aplikasi harus menghentikan proses program dengan memberikan pesan kepada pengguna.

---

## 7. Input Requirements

Aplikasi menerima input berupa:

* Pilihan menu.
* Topik catatan.
* Judul catatan.
* Isi catatan.
* Kata kunci pencarian.
* Nomor catatan untuk operasi edit dan delete.

---

## 8. Output Requirements

Aplikasi memberikan output berupa:

* Menu utama.
* Daftar catatan.
* Hasil pencarian.
* Pesan keberhasilan operasi.
* Pesan ketika data tidak ditemukan.
* Pesan ketika input tidak valid.
* Pesan ketika aplikasi dihentikan.

---

## 9. Data Storage

Pada versi saat ini, data disimpan sementara di dalam memory aplikasi.

Data tidak disimpan secara permanen.

Akibatnya, seluruh catatan akan hilang ketika program dihentikan.

Persistent storage tidak termasuk dalam kebutuhan versi saat ini.

---

## 10. Scope

### Included

Versi saat ini mencakup:

* Add knowledge.
* View knowledge.
* Search knowledge.
* Delete knowledge.
* Edit knowledge.
* Exit application.

### Not Included

Versi saat ini tidak mencakup:

* Login.
* Authentication.
* Multiple users.
* Database.
* API.
* Web interface.
* Mobile interface.
* Cloud storage.
* Synchronization.
* Collaboration.
* Persistent storage.

Fitur di luar cakupan dapat dipertimbangkan pada pengembangan berikutnya.

---

## 11. Constraints

Aplikasi memiliki batasan:

* Berjalan melalui terminal.
* Menggunakan Python.
* Data hanya disimpan selama program berjalan.
* Tidak membutuhkan koneksi internet.
* Tidak menggunakan database.
* Tidak membutuhkan layanan eksternal.

---

## 12. Success Criteria

Project dianggap memenuhi kebutuhan apabila pengguna dapat:

1. Menjalankan aplikasi melalui terminal.
2. Menambahkan catatan.
3. Melihat catatan.
4. Mencari catatan.
5. Menghapus catatan.
6. Mengedit catatan.
7. Mendapatkan informasi ketika input tidak valid.
8. Keluar dari aplikasi melalui menu yang tersedia.

---

## 13. Project Context

Mini Knowledge Vault dikembangkan sebagai project pembelajaran setelah mempelajari dan menyelesaikan kelas:

**Memulai Dasar Pemrograman untuk Menjadi Pengembang Software**

dari Dicoding.

Konsep yang dipelajari kemudian diterapkan ke dalam sebuah aplikasi sederhana agar dapat dipraktikkan melalui project nyata.
