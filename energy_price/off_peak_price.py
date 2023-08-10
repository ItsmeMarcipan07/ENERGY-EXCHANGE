from energy_price.base_hour_price import base_hour
from energy_price.peak_hour_price import peak_hour


def off_peak_hour(path):
    base = base_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
    peak = peak_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
    result = []
    for i in range(7):
        result.append(f'{(float(base[i]) * 2) - float(peak[i]):.2f}')
    return result
