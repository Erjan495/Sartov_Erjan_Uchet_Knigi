issued_books = 0

while True:
    print("\n--- Учёт книг (v1) ---")
    print("1 — Выдать одну книгу")
    print("2 — Показать, сколько книг выдано")
    print("3 — Сбросить счётчик")
    print("0 — Выход")

    komanda = input("Введите команду: ")

    if komanda == "1":
        issued_books += 1
        print("Книга выдана.")
    elif komanda == "2":
        print(f"Выдано книг: {issued_books}")
    elif komanda == "3":
        issued_books = 0
        print("Счётчик сброшен до 0.")
    elif komanda == "0":
        print("Завершение работы.")
        break
    else:
        print("Неизвестная команда")
