import phonebook_logger

def add_item(phonebook, *, name, number, comment):
    bookitem = {"fullname": "", "number": "", "comment": ""}
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem['comment'] = comment
    phonebook.append(bookitem)
    phonebook_logger.log(__file__, "Добавлен контакт: " + name + " " + number + " " + comment)

def update_contact(phonebook, keyword):
    items =[]
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print(f'Найдено => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Номер записи: {index}\n')
            index_item = phonebook[index]
            phonebook.pop(index)
            while True:
                name = input('Введите ФИО: ')
                if not name.strip():
                    print("\nФИО не может быть пустым. Введите заново")
                    continue
                number = input('Введите номер телефона: ')
                if not number.strip():
                    print("\nНомер телефона не может быть пустым. Введите заново")
                    continue
                comment = input('Введите комментарий: ')
                if not comment.strip():
                    print("\nКомментарий не может быть пустым. Введите заново")
                    continue
                index_item.update({"fullname":name, "number":number, "comment":comment})
                phonebook.insert(index, index_item)
                break
            print(f"\nОбновлена запись => ФИО: {name} | Телефон: {number} | Комментарий: {comment} | Index: {index}\n")
            phonebook_logger.log(__file__, f'\nОбновлена запись => ФИО: {name} | Телефон: {number} | Комментарий: {comment} | Index: {index}\n')
    print("-"*60)

def remove_contact(phonebook, keyword):
    for index, item in enumerate(phonebook):
        if keyword.lower() in item["fullname"].lower():
            print(f'Найдено => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Номер записи: {index}\n')
            sure = input("\nВы действительно хотите удалить контакт? [y/yes]: ")
            if not (sure.lower() == "y" or sure.lower() == "yes"):
                 break
            else:
                phonebook.pop(index)
                print("\nЗапись удалена.")
                phonebook_logger.log(__file__, f'Удалена запись => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Index: {index}\n')
    print("-"*60)   

def is_duplicate_number(phonebook, ph_number):
    for index, item in enumerate(phonebook):
        if ph_number in item["number"]:
            print("Этот телефон уже есть в справочнике.")
            phonebook_logger.log(__file__, "Попытка добавить дублирующую запись")
            return True        

def add_action(phonebook):
    items = []
    while True:
         fullname = input('Введите ФИО:: ')
         if not fullname.strip():
             print("\nФИО не может быть пустым. Введите заново")
             continue   
         ph_number = input('Введите номер телефона: ')
         if not ph_number.strip():
             print("\nНомер телефона не может быть пустым. Введите заново")
             continue
         num_check = is_duplicate_number(phonebook, ph_number)
         if num_check is True:
             continue
         comment = input('Введите комментарий: ')
         if not comment.strip():
             print("\nКомментарий не может быть пустым. Введите заново")
             continue
         items.append((fullname, ph_number,comment))
         char = input("\nВвести новый контакт? [y/yes]: ")
         if not (char.lower() == "y" or char.lower() == "yes"):
            break
    return items

def add_contact(phonebook):
    collected_items = add_action(phonebook)
    for name, number, comment in collected_items:
        add_item(phonebook, name=name, comment=comment, number=number)