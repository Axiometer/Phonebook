import csv

filename = "phonebook.csv"

print("-"*60)

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    phonebook = [data for data in reader]

for index, item in enumerate(phonebook):
    if item[:1][0].lower().find("kha") != -1:
        print(index, ":", item)

print("-"*60)

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['fullname','number','comment'])
    next(reader)
    for row in reader:
        print(row)

print("-"*60)