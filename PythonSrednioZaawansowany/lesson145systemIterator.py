import csv

with open(r'F:\Users\rzemi\Desktop\KursyPython\Python_courses\PythonSrednioZaawansowany\plik.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    while True:
        try:
            info=next(csvreader)
            print(info)
        except Exception as e:
            break;
    #for row in csvreader:
    #    print('|'.join(row))