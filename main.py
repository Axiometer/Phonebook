import csv, os
import phonebook_files
import phonebook_view

os.system('cls' if os.name == 'nt' else 'clear')
filename = "phonebook.csv"
print("-------------------Телефонный справочник------------------")

def main():
    #global phonebook
    #global filename
    phonebook = phonebook_files.read_from_csv(filename)

    while True:
        print("""
        Выберите действие:
        
        A: Добавить контакт
        L: Вывести список контактов
        S: Поиск контакта
        U: Обновить контакт
        R: Удалить контакт
        E: Выход
        """)
        action = input("Выберите действие: ")
        if action.upper() == "A":
            #phonebook_controller.add_contact()
            print("Добавление контакта...")
        elif action.upper() == "L":
            phonebook_view.list_contacts(phonebook)
        elif action.upper() == "S":
            keyword = input("Введите искомое слово: ")
            phonebook_view.search_contact(phonebook,keyword)
        elif action.upper() == "U":
            keyword = input("Введите имя контакта для изменения: ")
            #phonebook_controller.update_contact()
            print("Обновление контакта...")
        elif action.upper() == "R":
            keyword = input("Введите имя контакта для удаления: ")
            #phonebook_controller.remove_item()
            print("Удаление контакта...")
        elif action.upper() == "E":
            phonebook_files.write_to_csv(phonebook, filename)
            break
        else:
             print("\nНеверное действие")

if __name__ == "__main__":
    main()
