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
    idealUsage = tk.Label(new_window, text="Your Energy Usage Could Be:", foreground="white")
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
