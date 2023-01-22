def search_contact(phonebook, keyword):
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print("найдено => ФИО: {} | Телефон: {} | Комментарий: {} | Номер записи: {}\n".format(item["fullname"], item["number"], item["comment"], index))
    print("-"*60)

def list_contacts(book):
    print("-"*60)
    print("ФИО\t\t|\tТелефон\t\t|\tКомментарий", end="\n")
    print("-"*60)
    for item in book:
        print("{}\t\t{}\t\t{}".format(
            item["fullname"],item["number"],item["comment"]
        ))
    print("-"*60)
