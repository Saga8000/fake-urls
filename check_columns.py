import csv

with open('dataset/phishing_dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print("Columns in dataset are:")
    for h in headers:
        print(h)
