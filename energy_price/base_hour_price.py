import csv

def base_hour(path):
    with open(path, mode='r') as file:
        # reading the CSV file
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
            if row == 0:
                pass
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
    return [first_day / 24, second_day / 24, third_day / 24, fourth_day / 24, fifth_day / 24, sixth_day / 24,\
        seventh_day / 24]