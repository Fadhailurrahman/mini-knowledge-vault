
# Mini Knowledge Vault — Software Requirements Specification

## 1. Overview

Mini Knowledge Vault adalah aplikasi terminal berbasis Python yang digunakan untuk menyimpan dan mengelola catatan pengetahuan pribadi.

Aplikasi menyediakan operasi dasar untuk:

- Menambahkan catatan.
- Melihat catatan.
- Mencari catatan.
- Menghapus catatan.
- Mengedit catatan.

---

## 2. Purpose

Dokumen ini menjelaskan kebutuhan teknis dan perilaku utama yang harus dipenuhi oleh aplikasi Mini Knowledge Vault.

Dokumen digunakan sebagai referensi untuk memahami fungsi aplikasi dan batasan implementasinya.

---

## 3. Application Type

| Property | Value |
|---|---|
| Application | Mini Knowledge Vault |
| Type | Command-Line Application |
| Language | Python |
| Interface | Terminal / CLI |
| Storage | In-memory |
| Database | Tidak digunakan |
| Internet | Tidak diperlukan |
| Authentication | Tidak tersedia |

---

## 4. Application Flow

Alur utama aplikasi:

```text
Start
  ↓
Display Main Menu
  ↓
User Selects Menu
  ↓
Execute Selected Operation
  ↓
Return to Main Menu
  ↓
User Selects Menu Again
  ↓
Exit
````

Aplikasi akan terus menampilkan menu sampai pengguna memilih opsi keluar.

---

## 5. Data Model

Data utama aplikasi disimpan dalam sebuah list:

```python
knowledge = []
```

Setiap catatan direpresentasikan sebagai dictionary:

```python
note = {
    "topic": topic,
    "title": title,
    "content": content
}
```

### Data Fields

| Field     | Type   | Description   |
| --------- | ------ | ------------- |
| `topic`   | String | Topik catatan |
| `title`   | String | Judul catatan |
| `content` | String | Isi catatan   |

---

## 6. Functional Specification

### 6.1 Show Menu

Function:

```python
show_menu()
```

Tanggung jawab:

* Menampilkan menu utama.
* Menampilkan seluruh pilihan operasi yang tersedia.

Menu:

```text
1. Tambah catatan
2. Lihat semua catatan
3. Cari catatan
4. Hapus catatan
5. Edit catatan
6. Keluar
```

---

### 6.2 Add Knowledge

Function:

```python
add_knowledge()
```

Proses:

```text
User memilih Add
       ↓
Input topic
       ↓
Input title
       ↓
Input content
       ↓
Create dictionary
       ↓
Append ke knowledge
       ↓
Tampilkan pesan berhasil
```

Data ditambahkan menggunakan:

```python
knowledge.append(note)
```

---

### 6.3 View Knowledge

Function:

```python
view_knowledge()
```

Proses:

1. Memeriksa apakah terdapat catatan.
2. Jika tidak ada, tampilkan pesan.
3. Jika ada, lakukan iterasi terhadap list.
4. Tampilkan setiap catatan dengan nomor.

Iterasi menggunakan:

```python
for index, note in enumerate(knowledge, start=1):
```

Nomor ditampilkan mulai dari `1` agar lebih mudah dipilih oleh pengguna.

---

### 6.4 Search Knowledge

Function:

```python
search_knowledge()
```

Pencarian dilakukan terhadap:

```text
topic
title
content
```

Pencarian menggunakan:

```python
keyword.lower()
```

dan:

```python
note["topic"].lower()
note["title"].lower()
note["content"].lower()
```

Dengan demikian, pencarian tidak membedakan huruf besar dan huruf kecil.

Alur:

```text
Input keyword
      ↓
Iterasi setiap catatan
      ↓
Periksa topic
      ↓
Periksa title
      ↓
Periksa content
      ↓
Simpan hasil yang sesuai
      ↓
Tampilkan hasil
```

---

### 6.5 Delete Knowledge

Function:

```python
delete_knowledge()
```

Proses:

1. Memastikan terdapat catatan.
2. Menampilkan daftar catatan.
3. Meminta nomor catatan.
4. Memeriksa apakah input berupa angka.
5. Mengubah input menjadi integer.
6. Memeriksa apakah nomor berada dalam range yang tersedia.
7. Menghapus catatan menggunakan `.pop()`.

Contoh:

```python
deleted_note = knowledge.pop(index - 1)
```

`index - 1` digunakan karena nomor yang ditampilkan kepada pengguna dimulai dari `1`, sedangkan index list Python dimulai dari `0`.

---

### 6.6 Edit Knowledge

Function:

```python
edit_knowledge()
```

Proses:

1. Memastikan terdapat catatan.
2. Menampilkan daftar catatan.
3. Meminta nomor catatan.
4. Memvalidasi input.
5. Mengakses catatan berdasarkan index.
6. Menampilkan data saat ini.
7. Meminta data baru.
8. Memperbarui dictionary.

Data diperbarui menggunakan:

```python
note["topic"] = topic
note["title"] = title
note["content"] = content
```

---

### 6.7 Exit

Program dihentikan ketika pengguna memilih menu `6`.

Proses utama menggunakan:

```python
break
```

untuk menghentikan loop utama aplikasi.

---

## 7. Input Validation

Aplikasi melakukan validasi sederhana terhadap input pengguna.

Untuk pilihan yang harus berupa nomor, program menggunakan:

```python
choice.isdigit()
```

Kemudian input dikonversi menjadi integer:

```python
index = int(choice)
```

Program juga memeriksa apakah nomor yang dimasukkan berada dalam range data yang tersedia.

Validasi pada versi ini masih sederhana dan dapat dikembangkan lebih lanjut.

---

## 8. Program Structure

Struktur utama program:

```text
main.py
│
├── knowledge
│
├── show_menu()
├── add_knowledge()
├── view_knowledge()
├── search_knowledge()
├── delete_knowledge()
├── edit_knowledge()
│
└── main()
```

Setiap function memiliki tanggung jawab yang berbeda untuk menjaga program tetap mudah dipahami.

---

## 9. Storage

Aplikasi menggunakan penyimpanan sementara di memory.

```python
knowledge = []
```

Tidak terdapat file database atau penyimpanan eksternal.

Konsekuensinya:

```text
Program dijalankan
       ↓
Data ditambahkan
       ↓
Data tersedia di memory
       ↓
Program ditutup
       ↓
Data hilang
```

Persistent storage belum menjadi bagian dari implementasi saat ini.

---

## 10. Non-Functional Requirements

### Usability

Aplikasi harus memiliki menu yang sederhana sehingga pengguna dapat memahami pilihan yang tersedia melalui terminal.

### Maintainability

Kode dipisahkan menjadi beberapa function berdasarkan tanggung jawabnya.

### Simplicity

Aplikasi tidak menggunakan framework, database, atau teknologi tambahan yang tidak diperlukan untuk kebutuhan dasarnya.

### Portability

Aplikasi dapat dijalankan pada sistem yang memiliki Python dan terminal.

---

## 11. Dependencies

Aplikasi tidak menggunakan library eksternal.

Program hanya membutuhkan:

* Python.
* Terminal / Command Prompt.

---

## 12. Limitations

Versi saat ini memiliki beberapa keterbatasan:

* Data tidak persistent.
* Tidak menggunakan database.
* Tidak memiliki authentication.
* Tidak mendukung multiple users.
* Tidak memiliki interface grafis.
* Validasi input masih sederhana.
* Error handling masih terbatas.

---

## 13. Future Considerations

Pengembangan berikutnya dapat mempertimbangkan:

* File handling.
* JSON persistence.
* Validasi input yang lebih baik.
* Error handling.
* Pencarian yang lebih fleksibel.
* Pengelompokan catatan berdasarkan topik.
* Perbaikan struktur kode.

Pengembangan tersebut bersifat opsional dan dapat dilakukan berdasarkan kebutuhan project.

---

## 14. Development Context

Mini Knowledge Vault merupakan project pembelajaran yang dikembangkan untuk menerapkan konsep fundamental pemrograman ke dalam aplikasi sederhana.

Project ini dikembangkan setelah mempelajari dan menyelesaikan kelas:

**Memulai Dasar Pemrograman untuk Menjadi Pengembang Software**

dari Dicoding.

Project digunakan sebagai media praktik untuk menghubungkan konsep pemrograman dengan implementasi aplikasi nyata.
