import csv
from datetime import datetime, date, timedelta

fields = ['Date', 'Place', 'Degrees', 'Wind_speed']
rows = [
    [date(2020, 11, 18), 'Minsk', '2', '9'],
    [date(2020, 11, 19), 'Pinsk', '5', '11'],
    [date(2020, 11, 19), 'Minsk', '4', '9'],
    [date(2020, 11, 20), 'Gomel', '4', '12'],
    [date(2020, 11, 21), 'Minsk', '1', '9'],
    [date(2020, 11, 22), 'Minsk', '4', '15'],
    [date(2020, 11, 23), 'Grodno', '6', '8'],
    [date(2020, 11, 24), 'Minsk', '4', '12'],
    [date(2020, 11, 25), 'Brest', '2', '14'],
    [date(2020, 11, 25), 'Minsk', '3', '10'],
]
with open('weather.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open('weather.csv', 'r') as f:
    delta = timedelta(7)
    weather = [0, 0]
    count = 0
    lines = []
    csvreader = csv.reader(f)
    fields = next(csvreader)
    for line in csvreader:
        lines.append(line)

    for line in lines:
        a = datetime.strptime(line[0], '%Y-%m-%d').date()
        if line[1] == 'Minsk' and date.today() - a <= delta:
            weather[0] += int(line[2])
            weather[1] += int(line[3])
            count += 1
    avg_temp = weather[0] / count
    avg_speed = weather[1] / count
    print(avg_temp)
    print(avg_speed)
