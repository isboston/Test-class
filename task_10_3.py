import csv
from datetime import datetime

with open('weather.csv', 'r') as weather:
    lines = []
    csvreader = csv.reader(weather)
    fields = next(csvreader)
    for line in csvreader:
        lines.append(line)
    li_date = []
    for line in lines:
        dt = datetime.strptime(line[0], '%Y-%m-%d').date()
        li_date.append(dt)
    print(f'The earliest date: {min(li_date)}')
