import csv

def peak_hour(path):
    with open(path, mode='r') as file:
        csvFile = csv.reader(file)
        row = 1
        first_day = 0
        second_day = 0
        third_day = 0
        fourth_day = 0
        fifth_day = 0
        sixth_day = 0
        seventh_day = 0
        for lines in csvFile:
            if lines[0] == '' or not 55 < int(lines[0]) < 140:
                continue

            if row == 1:
                first_day += float(lines[5])
            elif row == 2:
                second_day += float(lines[5])
            elif row == 3:
                third_day += float(lines[5])
            elif row == 4:
                fourth_day += float(lines[5])
            elif row == 5:
                fifth_day += float(lines[5])
            elif row == 6:
                sixth_day += float(lines[5])
            elif row == 7:
                seventh_day += float(lines[5])
                row = 1
                continue
            row += 1
        return [first_day / 12, second_day / 12, third_day / 12, fourth_day / 12, fifth_day / 12, sixth_day / 12,
                seventh_day / 12]