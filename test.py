import requests
import pandas as pd
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

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

unique_months, month_counts = np.unique(
date_array[:, :2], axis=0, return_counts=True)

# Calculate the mean temperature for each unique month
mean_temps = []
for month in unique_months:
    month_indices = np.all(date_array[:, :2] == month, axis=1)
    mean_temp = np.mean(temp_array[month_indices])
    mean_temps.append(mean_temp)

monthDict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'}
# Print out the mean temperatures for each month
fullAvgTempdf = pd.DataFrame({
    # 'Month': [f"{month[1]}/{month[0]}" for month in unique_months],
    'Month': [f"{month[0]}-{monthDict[month[1]]}" for month in unique_months],
    'avg_temp': mean_temps
})
index = fullAvgTempdf.loc[fullAvgTempdf['Month'] == '2013-Oct'].index[0]
limitedAvgTempdf = fullAvgTempdf.loc[index:]
limitedAvgTempdf = limitedAvgTempdf.reset_index(drop=True)

future_dates = np.array([[(date_array[-1][0]+i), j, k] for i in range(1, 31) for j in range(1, 13) for k in range(1, 32)])

# values = numpy.empty()
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(date_array, temp_array)
future_temps = np.round(regressor.predict(date_array), 4)
#date_array = np.concatenate((date_array, future_dates))
# create regressor and fit data
###HEREHEREHERE
for x in range(30):
    regressor.fit(date_array, future_temps)

# # predict temperatures for next 30 years
    future_dates = np.array([[(date_array[-1][0]+i), j, k] for i in range(1, 2) for j in range(1, 13) for k in range(1, 32)])
    date_array = np.concatenate((date_array, future_dates))
    future_temps = np.round(regressor.predict(date_array), 4)
###
    # print(future_dates)
    #temp_array = np.concatenate((temp_array, future_temps))
    # values.append(future_temps)
    # print(values)
#print()
ax = plt.gca() 
future_temps.plot(kind = 'line',
        x = 'name',
        y = 'math_marks',
        color = 'green',ax = ax)
plt.show()
# future_temps.plot('kind')
# future_date = np.array([[(date_array[-1][0]+i), j, k] for i in range(1, 31) for j in range(1, 13) for k in range(1, 32)])

# create regressor and fit data
# regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# regressor.fit(date_array, temp_array)

# predict temperatures for next 30 years
df = pd.DataFrame(future_temps)
dfSubset = df[::31]
#print(df)
# temp_array = np.array(list(sorted_data.values())).reshape(-1, 1)
# average tempretures of the month


# print(limitedAvgTempdf)
# regressor = LinearRegression()
# regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# regressor.fit(date_array, temp_array)

#start_year = 2023
#future_date = []
#for year in range(start_year, start_year+30):
#    for month in range(1, 13):
#        for day in range(1, 32):
#            if day <= 28 and month == 2:
#                future_date.append(int(f"{year}02{day:02d}"))
#                #future_date.append(f"{year}-02-{day:02d}")
#            elif day <= 30 and month in [4, 6, 9, 11]:
#                #future_date.append(f"{year}-{month:02d}-{day:02d}")
#                future_date.append(int(f"{year}{month:02d}{day:02d}"))
#            elif day <= 31:
#                #future_date.append(f"{year}-{month:02d}-{day:02d}")
#                future_date.append(int(f"{year}{month:02d}{day:02d}"))
#
#future_temps = []
#regressor = RandomForestRegressor(n_estimators=100, random_state=42)
## print(temp_array)
#future_dateNP = np.array(future_date)
##print(future_date)
#for i in range(30):
#    start_index = i*365
#    end_index = (i+1)*365
#    # fit regressor on data for current year
#    regressor.fit(temp_array[start_index:end_index],future_dateNP[start_index:end_index])
#    # predict temperatures for current year
#    # print(type(date_array[start_index:end_index]))
#    # print(type)
#    #temp = regressor.predict(future_dateNP[start_index:end_index])
#    temp = regressor.predict(future_dateNP[start_index:end_index].reshape(-1, 1))
#    print(temp)
#    year_temps = np.round((temp), 4)
#    future_temps.append(year_temps)
##print(future_temps)
#thirty_days = [4, 6, 9, 11]
#
#future_dates = np.array([[year, month, day]
#                         for year in range(2023, 2025)
#                         for month in range(1, 13)
#                         for day in range(1, 32)
#                         if (day <= 30 or month not in thirty_days)
#                         and not (day == 31 and month == 2)
#                         and not (day == 30 and month == 2)
#                         and not (day == 29 and month == 2 and year % 4 != 0)])
#
## future_temps = np.round(regressor.predict(future_dates), 4)
## future_temps = regressor.predict(future_dates)
#tempfuture_dates = np.array([])
#for i in range(len(future_dates)):
#    date = '-'.join(map(str, future_dates[i]))
#    tempfuture_dates = np.append(tempfuture_dates, date)
##print(tempfuture_dates)
##print(future_temps)
#future_stats = np.column_stack((tempfuture_dates, future_temps))
## future_stats = np.column_stack((np.array(tempfuture_dates), df))
#
#df = pd.DataFrame(future_stats)
#print(df)

energyData = {}
with open('test.csv', 'r') as g:
    for line in g:
        date, max, min = line.strip().split(',')
        energyData[date] = float((int(max)+int(min))/2)
sorted_data = dict(sorted(energyData.items()))
energyDF = pd.DataFrame(list(sorted_data.items()), columns=[
                        'Month', 'Energy Usage [kwH]'])

merged_df = pd.merge(fullAvgTempdf, energyDF, on='Month')
print(merged_df)
#
fig, ax1 = plt.subplots()

# plot the first y-axis
ax1.plot(merged_df['Month'], merged_df['avg_temp'], color='blue')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y1-axis', color='blue')

# create a second y-axis
ax2 = ax1.twinx()

# plot the second y-axis
ax2.plot(merged_df['Month'], merged_df['Energy Usage [kwH]'], color='red')
ax2.set_ylabel('Y2-axis', color='red')

#plt.show()
#

# merged_df.plot(x='Month', y='Energy Usage [kwH]', kind='line')
# plt.show()

# Calculate the Pearson correlation coefficient between temperature and energy usage
corr_coef = merged_df['avg_temp'].corr(
    merged_df['Energy Usage [kwH]'], method='pearson')

# Print the correlation coefficient
print(f"The Pearson correlation coefficient between temperature and energy usage is: {corr_coef:.2f}")

unique_months, month_counts = np.unique(
date_array[:, :2], axis=0, return_counts=True)

mean_temps = []
for month in unique_months:
    month_indices = np.all(date_array[:, :2] == month, axis=1)
    mean_temp = np.mean(future_temps[month_indices])
    mean_temps.append(mean_temp)

monthDict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'}
# Print out the mean temperatures for each month
fullAvgTempdf = pd.DataFrame({
    # 'Month': [f"{month[1]}/{month[0]}" for month in unique_months],
    'Month': [f"{month[0]}-{monthDict[month[1]]}" for month in unique_months],
    'avg_temp': mean_temps
})
index = fullAvgTempdf.loc[fullAvgTempdf['Month'] == '2024-Jan'].index[0]
limitedAvgTempdf = fullAvgTempdf.loc[index:]
limitedAvgTempdf = limitedAvgTempdf.reset_index(drop=True)

merged_df = pd.merge(fullAvgTempdf, energyDF, on='Month')
print(merged_df)

#for x in range(30*12):
#    # energyDF.a = corr_coef * (future_temps[x] - np.mean(future_temps)) / np.std(future_temps) * np.std(energyDF) + np.mean(energyDF)
#    energyDF = np.insert(energyDF, 'Jan', corr_coef * (dfSubset[x] - np.mean(dfSubset)) / np.std(dfSubset) * np.std(energyDF) + np.mean(energyDF))
#print(energyDF)
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#GHG Emissions = Energy Consumption (in GJ) x 55 (kg CO2e/GJ)
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Your recommended energy usage")
    text = tk.Text(new_window, height=40, width=40)
    text.insert(tk.END, "Tips to decrease energy consumption:\n\n")
    text.tag_add("bold", "1.0", "1.33")
    text.insert(tk.END, "- Upgrade to energy-efficient appliances\n\n" "- Use LED light bulbs\n\n" "- Adjust the thermostat\n\n"  "- Seal air leaks\n\n"  "- Insulate your home\n\n" "- Reduce water usage\n\n" "- Use natural light\n\n" "- Unplug electronics")
    text.tag_config("bold", font=("Helvetica", 12, "bold"))

    text.grid(row= 3, column=3)

    

    # Add widgets to the new window here...
    idealUsage = tk.Label(new_window, text="Your Energy Usage Is: 746kWH/hour", foreground="white")
    idealUsage.grid(row=1, column=1)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 6]
    ax.plot(x, y)

    # Create a canvas to display the Matplotlib figure in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 3, column = 1)



root = tk.Tk()
root.title("Energy Optimization")
root.resizable(False, False)
title_label = tk.Label(root, text="Enter the interval of time you want a projected energy consumption", font=("Arial", 24))
title_label.grid(row=0, column=2, columnspan=4, sticky='nsew')



years = []

for year in range(2023, 2054):
    year_str = str(year)
    years.append(year_str)


startMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
              "December"]
endMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
            "December"]

selected_option1 = tk.StringVar()
selected_option1.set("Select Year")

selected_option2 = tk.StringVar()
selected_option2.set("Select Start Month")

selected_option3 = tk.StringVar()
selected_option3.set("Select End Month")

year_menu = tk.OptionMenu(root, selected_option1, *years)
year_menu.grid(row=1, column=2, padx=10, sticky='nsew')

startMonth_menu = tk.OptionMenu(root, selected_option2, *startMonth)
startMonth_menu.grid(row=1, column=3, padx=5, sticky='nsew')

endMonth_menu = tk.OptionMenu(root, selected_option3, *endMonth)
endMonth_menu.grid(row=1, column=4, padx=10, sticky='nsew')

button = tk.Button(root, text="Calculate emission saving",
                   command=open_new_window)
button.grid(row=2, column=3, sticky='nsew')

option_label = tk.Label(root, text="")
option_label.grid(row=3, column=1, sticky='nsew')

selected_year = selected_option1.get()
selected_startMonth = selected_option2.get()
selected_endMonth = selected_option3.get()


root.mainloop()
