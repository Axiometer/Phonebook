import csv

# Записываем в файл CSV список словарей
def write_to_csv(phonebook, filename, write_mode = "w"):
        with open(filename, write_mode) as csvfile:
               writer = csv.DictWriter(csvfile, fieldnames=["fullname", "number", "comment"])
               writer.writeheader()
               for item in phonebook:
                   writer.writerow(item)

# Читаем из файла CSV список словарей
def read_from_csv(filename):
    book = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['fullname', 'number', 'comment'])
        next(reader)
        book.extend(reader)
    return book
