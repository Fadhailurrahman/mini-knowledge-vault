# Mini Knowledge Vault
# Module 4 - Exploration & Modification
# Data masih disimpan di memory selama program berjalan.

knowledge = []


def show_menu():
    print("\n=== MINI KNOWLEDGE VAULT ===")
    print("1. Tambah catatan")
    print("2. Lihat semua catatan")
    print("3. Cari catatan")
    print("4. Hapus catatan")
    print("5. Edit catatan")
    print("6. Keluar")


def add_knowledge():
    print("\n=== TAMBAH CATATAN ===")

    topic = input("Topik    : ")
    title = input("Judul    : ")
    content = input("Catatan  : ")

    note = {
        "topic": topic,
        "title": title,
        "content": content
    }

    knowledge.append(note)

    print("\nCatatan berhasil disimpan!")


def view_knowledge():
    print("\n=== DAFTAR CATATAN ===")

    if len(knowledge) == 0:
        print("Belum ada catatan.")
        return

    for index, note in enumerate(knowledge, start=1):
        print(f"\n[{index}]")
        print(f"Topik   : {note['topic']}")
        print(f"Judul   : {note['title']}")
        print(f"Catatan : {note['content']}")


def search_knowledge():
    print("\n=== CARI CATATAN ===")

    if len(knowledge) == 0:
        print("Belum ada catatan.")
        return

    keyword = input("Masukkan kata kunci: ")

    found_notes = []

    for note in knowledge:
        if (
            keyword.lower() in note["topic"].lower()
            or keyword.lower() in note["title"].lower()
            or keyword.lower() in note["content"].lower()
        ):
            found_notes.append(note)

    if len(found_notes) == 0:
        print("\nCatatan tidak ditemukan.")
        return

    print("\n=== HASIL PENCARIAN ===")

    for index, note in enumerate(found_notes, start=1):
        print(f"\n[{index}]")
        print(f"Topik   : {note['topic']}")
        print(f"Judul   : {note['title']}")
        print(f"Catatan : {note['content']}")


def delete_knowledge():
    print("\n=== HAPUS CATATAN ===")

    if len(knowledge) == 0:
        print("Belum ada catatan yang dapat dihapus.")
        return

    view_knowledge()

    choice = input("\nPilih nomor catatan yang ingin dihapus: ")

    if not choice.isdigit():
        print("\nPilihan tidak valid.")
        print("Masukkan nomor catatan.")
        return

    index = int(choice)

    if index < 1 or index > len(knowledge):
        print("\nNomor catatan tidak ditemukan.")
        return

    deleted_note = knowledge.pop(index - 1)

    print("\nCatatan berhasil dihapus!")
    print(f"Judul: {deleted_note['title']}")


def edit_knowledge():
    print("\n=== EDIT CATATAN ===")

    if len(knowledge) == 0:
        print("Belum ada catatan yang dapat diedit.")
        return

    view_knowledge()

    choice = input("\nPilih nomor catatan yang ingin diedit: ")

    if not choice.isdigit():
        print("\nPilihan tidak valid.")
        print("Masukkan nomor catatan.")
        return

    index = int(choice)

    if index < 1 or index > len(knowledge):
        print("\nNomor catatan tidak ditemukan.")
        return

    note = knowledge[index - 1]

    print("\n=== DATA CATATAN SAAT INI ===")
    print(f"Topik   : {note['topic']}")
    print(f"Judul   : {note['title']}")
    print(f"Catatan : {note['content']}")

    print("\n=== MASUKKAN DATA BARU ===")

    topic = input("Topik    : ")
    title = input("Judul    : ")
    content = input("Catatan  : ")

    note["topic"] = topic
    note["title"] = title
    note["content"] = content

    print("\nCatatan berhasil diperbarui!")


def main():
    while True:
        show_menu()

        choice = input("\nPilih menu: ")

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
            print("\nTerima kasih telah menggunakan Mini Knowledge Vault.")
            print("Program selesai.")
            break

        else:
            print("\nPilihan tidak valid.")
            print("Silakan pilih menu yang tersedia.")


main()
