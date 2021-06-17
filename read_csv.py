import csv

with open('files/data.csv', 'r', encoding='UTF8', newline='') as file:
    # filereader = csv.reader(file, delimiter=' ', quotechar='|')
    # for row in filereader:
    #     print(', '.join(row))
    filereader = csv.DictReader(file)
    for row in filereader:
        print(row)
    file.close()