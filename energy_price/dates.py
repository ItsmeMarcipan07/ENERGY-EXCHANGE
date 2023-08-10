import csv


def get_dates(path):
    with open(path, mode='r') as file:
        csvFile = csv.reader(file)
        dates = []
        for lines in csvFile:
            if lines[0] == '':
                continue
            elif len(dates) == 7:
                break
            else:
                data = lines[3].split('.')[:2]
                dates.append(f"{data[0]}.{data[1]}")
    return dates
