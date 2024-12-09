import asyncio

from database import(
    Base, Book, Genre, Author, 
    session, engine, utils
 ) 

async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    while 1:
        print("""
    Выберите нужное вам действие (введите число)
        1: Добавление новой книги
        2: Добавление нового автора
        3: Добавление нового жанра
        4: Получение списка всех книг
        5: Получение информации о книге по id
        6: Удаление книги по ID
        7: Окончание программы
""")
        action = int(input("Ваш выбор: "))


        match action:

            case 1:
                title = input("Введите название книги: ")
                author_id = int(input("Введите ID автора: "))
                genre_id = int(input("Введите ID жанра: "))
                author_exists = await utils.check_existence(session, Author, author_id)
                if not author_exists:
                    print("\nАвтора с таким ID не существует (рекомендуеться выбрать действие \"2\")")
                    continue
                genre_exists = await utils.check_existence(session, Genre, genre_id)
                if not genre_exists:
                    print("\nЖанра с таким ID не существует (рекомендуеться выбрать действие \"3\")")
                    continue
                book = Book(
                    title=title,
                    author_id=author_id,
                    genre_id=genre_id
                )
                await utils.insert_object(session, book)
                print("\nНовая книга добавлена!")
                continue

            case 2:
                name = input("Введите имя автора: ")
                author = Author(
                    name=name
                )
                await utils.insert_object(session, author)
                print("\nНовый автор добавлен!")
                continue

            case 3:
                name = input("Введите название жанра: ")
                genre = Genre(
                    name=name
                )
                await utils.insert_object(session, genre)
                print("\nНовый жанр добавлен!")
                continue

            case 4:
                books = await utils.select_many(session)
                for book in books:
                    print(f"\nID: {book.id}, Title: {book.title}\n")
                continue

            case 5:
                book_id = int(input("Введите ID книги: "))
                book = await utils.select_by_id(session, Book, object_id=book_id)
                if book:
                    print(f"\nID: {book.id}, Title: {book.title}, Author ID: {book.author_id}, Genre ID: {book.genre_id}")
                else:
                    print("\nТакой книги не существует!")
                continue

            case 6:
                book_id = int(input("Введите ID книги для удаления: "))
                book = await utils.select_by_id(session, Book, object_id=book_id)
                if book:
                    print(f"\nКнига \"{book.title}\" успешно удалена!")
                    await utils.delete_by_id(session, Book, book_id)
                else:
                    print("\nТакой книги не существует!")
                continue

            case 7:
                return
            
            case _:
                print("\nВы выбрали не ту цифру она за пределеом от 1 до 7 (включительно), повторите ещё раз!")




if __name__ == "__main__":
    asyncio.run(main())