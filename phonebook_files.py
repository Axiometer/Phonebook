import csv
import phonebook_logger

# Записываем в файл CSV список словарей
def write_to_csv(phonebook, filename, write_mode = "w"):
    with open(filename, write_mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["fullname", "number", "comment"])
        writer.writeheader()
        for item in phonebook:
            writer.writerow(item)
    phonebook_logger.log(__file__, "Записан файл " + filename)

# Читаем из файла CSV список словарей
def read_from_csv(filename):
    book = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['fullname', 'number', 'comment'])
        # пропускаем шапку
        next(reader)
        book.extend(reader)
    phonebook_logger.log(__file__, "Считан файл " + filename)
    return book

def import_file(book, filename):
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['fullname', 'number', 'comment'])
        # пропускаем шапку
        next(reader)
        book.extend(reader)
    print("Имортирование выполнено успешно...")
    phonebook_logger.log(__file__, "Имортирован файл " + filename)

def export_file(phonebook, filename):
    write_to_csv(phonebook, filename)
    phonebook_logger.log(__file__, "Экспортирован файл " + filename)

def read_from_txt(phonebook, filename):
    book = []
    with open(filename, "r") as txtfile:
        reader = txtfile.readlines()
        lines = [line.rstrip('\n') for line in reader]
        book.extend(lines)
    list_to_listofdicts = [{'fullname':book[i], 'number':book[i+1], 'comment':book[i+2]} for i in range(0, len(book), 4)]
    phonebook.extend(list_to_listofdicts)
    phonebook_logger.log(__file__, "Считан файл " + filename)
