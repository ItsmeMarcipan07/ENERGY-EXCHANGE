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
            match row:
                case 1:
                    first_day += float(lines[5])
                case 2:
                    second_day += float(lines[5])
                case 3:
                    third_day += float(lines[5])
                case 4:
                    fourth_day += float(lines[5])
                case 5:
                    fifth_day += float(lines[5])
                case 6:
                    sixth_day += float(lines[5])
                case 7:
                    seventh_day += float(lines[5])
                    row = 1
                    continue
            row += 1
        return [f'{first_day / 12:.2f}', f'{second_day / 12:.2f}', f'{third_day / 12:.2f}', f'{fourth_day / 12:.2f}',
                f'{fifth_day / 12:.2f}', f'{sixth_day / 12:.2f}', f'{seventh_day / 12:.2f}']
