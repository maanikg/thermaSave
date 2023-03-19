import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = {}
with open('output.csv', 'r') as f:
    for line in f:
        date, temp = line.strip().split(',')
        data[date] = float(temp)

sorted_data = dict(sorted(data.items()))

date_array = np.array([list(map(int, date.split('-')))
                      for date in sorted_data.keys()])
temp_array = np.array(list(sorted_data.values()))

# regressor = LinearRegression()
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(date_array, temp_array)


future_dates = np.array([[year, month, day] for year in range(
    2022, 2023) for month in range(1, 13) for day in range(1, 32)])
future_temps = np.round(regressor.predict(future_dates),4)

last_date = list(sorted_data.keys())[-1]
last_temp = sorted_data[last_date]

for i in range(len(future_dates)):
    date = '-'.join(map(str, future_dates[i]))
    if date == f"{int(last_date[:4])+1}-{last_date[5:]}":
        future_temps[i] = (future_temps[i] + last_temp) / 2

tempfuture_dates = np.array([])
for i in range(len(future_dates)):
    date = '-'.join(map(str, future_dates[i]))
    tempfuture_dates=np.append(tempfuture_dates,date)

future_stats = np.column_stack((np.array(tempfuture_dates), future_temps))

df = pd.DataFrame(future_stats, columns=['Date', 'Temperature'])
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%-m-%d')
print(df)

with open('output.csv', 'r') as f:
    for line in f:
        date, max, min = line.strip().split(',')
        data[date] = float(temp)

# df = pd.DataFrame(data, columns=['Date', 'Temperature'])
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
# print(df)
# Set up the API endpoint URL
# url = 'https://archive-api.open-meteo.com/v1/archive?'

# # Set up the query parameters
# params = {
#     # 'q': 'Paris',
#     'latitude':'52.52',
#     'longitude':'-79.40',
#     'start_date':'2023-02-12',
#     'end_date':'2023-03-13',
#     'daily':'temperature_2
