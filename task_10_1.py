import csv

fields = ['firstname', 'lastname', 'age']
rows = [
    ['Alex', 'Varkalov', '13'],
    ['Aleh', 'Ivanchov', '11'],
    ['Pred', 'Ferrikov', '31'],
    ['Vlad', 'Soloviov', '65'],
    ['Ivan', 'Zolotkov', '47'],
    ['Vova', 'Vorobiov', '19'],
]
new_file = "new_file.csv"
with open(new_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

ages = []
with open(new_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        for index, age in enumerate(row):
            if index == 2:
                ages.append(int(age))

report_fields = ['1-12', '13-18', '19-25', '26-40', '40+']
report_rows = [[0, 0, 0, 0, 0]]
for num in ages:
    if 1 <= num <= 12:
        report_rows[0][0] += 1
    elif 13 <= num <= 18:
        report_rows[0][1] += 1
    elif 19 <= num <= 25:
        report_rows[0][2] += 1
    elif 26 <= num <= 40:
        report_rows[0][3] += 1
    elif num > 40:
        report_rows[0][4] += 1
report_file = "report.csv"
with open(report_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(report_fields)
    csvwriter.writerows(report_rows)
