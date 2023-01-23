import phonebook_logger

# функция поиска паттерна в контакте
def search_contact(phonebook, keyword):
    phonebook_logger.log(__file__, "Поиск контактов...")
    # нумеруем список словарей
    for index, item in enumerate(phonebook):
        # в каждом словаре ищем keyword в поле fullname
        if keyword.lower() in item["fullname"].lower():
            print(f'Найдено => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Номер записи: {index}\n')
    print("-"*60)

# функция вывода списка контактов
def list_contacts(book):
    phonebook_logger.log(__file__, "Вывод контактов...")
    # шапка
    print("-"*60)
    print("ФИО\t\t|\tТелефон\t\t|\tКомментарий", end="\n")
    print("-"*60)
    # поэлементно проходим список. один элемент - словарь
    for item in book:
        print(f'{item["fullname"]}\t\t{item["number"]}\t\t{item["comment"]}')
    print("-"*60)
