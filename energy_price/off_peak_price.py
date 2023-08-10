import csv
from base_hour_price import base_hour
from peak_hour_price import peak_hour

def off_peak_hour(path):
    base = base_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
    peak = peak_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
    result = []
    for i in range(7):
        result.append((base[i] * 2) - peak[i])
    return result