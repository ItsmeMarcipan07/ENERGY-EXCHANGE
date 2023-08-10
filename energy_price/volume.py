import csv


def volume_total(path):
    with open(path, mode='r') as file:
        csvFile = csv.reader(file)
        row = 0
        first_day = 0
        second_day = 0
        third_day = 0
        fourth_day = 0
        fifth_day = 0
        sixth_day = 0
        seventh_day = 0
        for lines in csvFile:
            match row:
                case 0:
                    pass
                case 1:
                    first_day += float(lines[-1])
                case 2:
                    second_day += float(lines[-1])
                case 3:
                    third_day += float(lines[-1])
                case 4:
                    fourth_day += float(lines[-1])
                case 5:
                    fifth_day += float(lines[-1])
                case 6:
                    sixth_day += float(lines[-1])
                case 7:
                    seventh_day += float(lines[-1])
                    row = 1
                    continue
            row += 1
    return [f'{first_day:.2f}', f'{second_day:.2f}', f'{third_day:.2f}', f'{fourth_day:.2f}', f'{fifth_day:.2f}',
            f'{sixth_day:.2f}', f'{seventh_day:.2f}']
