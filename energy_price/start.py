import csv
import math
from base_hour_price import base_hour
from peak_hour_price import peak_hour
from off_peak_price import off_peak_hour

from connection import connection_plc
print(base_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv'))
print(peak_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv'))
print(off_peak_hour("C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv"))