import pandas as pd
from energy_price.base_hour_price import base_hour
from energy_price.peak_hour_price import peak_hour
from energy_price.off_peak_price import off_peak_hour
from energy_price.volume import volume_total
from energy_price.dates import get_dates

base_hour_data = base_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
peak_hour_data = peak_hour('C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv')
off_peak_hour_data = off_peak_hour("C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv")
volume_total_data = volume_total("C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv")
dates = get_dates("C:\\Users\SESA732254\PycharmProjects\pythonProject1\ibex\data.csv")

pd_df = pd.DataFrame([base_hour_data, peak_hour_data, off_peak_hour_data],
                     index=['Base(01-24)', 'Peak(9-20)', 'Off-Peak(01-08 & 21-24)'],
                     columns=dates)
pd_df1 = pd.DataFrame([base_hour_data, volume_total_data], index=['Prices', 'Volume'], columns=dates)
print(pd_df, '\n')
print(pd_df1)
