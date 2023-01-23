import csv, os
import phonebook_logger
import phonebook_files
import phonebook_view
import phonebook_controller

# инициализация
os.system('cls' if os.name == 'nt' else 'clear')
filename = "phonebook.csv"
print("-------------------Телефонный справочник------------------")

def main():
    phonebook_logger.log(__file__, "starting up...")

    # читаем файл CSV и кладем в переменную список словарей
    phonebook = phonebook_files.read_from_csv(filename)

    phonebook_logger.log(__file__, "main CSV file read")

    # выводим меню
    while True:
        print("""
        Выберите действие:
        
        A: Добавить контакт
        L: Вывести список контактов
        S: Поиск контакта
        U: Обновить контакт
        R: Удалить контакт
        I: Импорт файла CSV
        T: Импорт файла TXT
        E: Экспорт файла
        Q: Выход
        """)
        action = input("Выберите действие: ")
        if action.upper() == "A":
            phonebook_controller.add_contact(phonebook)
            print("Добавление контакта выполнено...")
            phonebook_logger.log(__file__, "Добавление контакта выполнено")
        elif action.upper() == "L":
            phonebook_view.list_contacts(phonebook)
            phonebook_logger.log(__file__, "Выведен список контактов")
        elif action.upper() == "S":
            keyword = input("Введите искомое слово: ")
            phonebook_view.search_contact(phonebook,keyword)
            phonebook_logger.log(__file__, "Выполнен поиск контактов")
        elif action.upper() == "U":
            keyword = input("Введите имя контакта для изменения: ")
            phonebook_controller.update_contact(phonebook,keyword)
            print("Обновление контакта выполнено...")
            phonebook_logger.log(__file__, "Обновление контакта выполнено...")
        elif action.upper() == "R":
            keyword = input("Введите имя контакта для удаления: ")
            phonebook_controller.remove_contact(phonebook, keyword)
            print("Удаление контакта выполнено")
            phonebook_logger.log(__file__, "Удаление контакта выполнено...")
        elif action.upper() == "I":
            keyword = input("Введите имя файла для импорта: ")
            phonebook_files.import_file(phonebook, keyword)
            phonebook_logger.log(__file__, "Импортирован CSV файл. Слияние")
        elif action.upper() == "T":
            filetxt = input("Введите имя файла для импорта: ")
            phonebook_files.read_from_txt(phonebook, filetxt)
            phonebook_logger.log(__file__, "Импортирован TXT файл. Слияние")
        elif action.upper() == "E":
            keyword = input("Введите имя файла для экспорта: ")
            phonebook_files.export_file(phonebook, keyword)
            phonebook_logger.log(__file__, "Экспортирован файл в CSV формате")
        elif action.upper() == "Q":
            phonebook_files.write_to_csv(phonebook, filename)
            phonebook_logger.log(__file__, "Выход из программы")
            break
        else:
             print("\nНеверное действие")
             phonebook_logger.log(__file__, "\nНеверное действие")

if __name__ == "__main__":
    main()
