# Mini Knowledge Vault
# Day 3 - Basic Version
# Data masih disimpan di memory selama program berjalan.

knowledge = []


def show_menu():
    print("\n=== MINI KNOWLEDGE VAULT ===")
    print("1. Tambah catatan")
    print("2. Lihat semua catatan")
    print("3. Cari catatan")
    print("4. Keluar")


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
            print("\nTerima kasih telah menggunakan Mini Knowledge Vault.")
            print("Program selesai.")
            break

        else:
            print("\nPilihan tidak valid.")
            print("Silakan pilih menu yang tersedia.")


main()
