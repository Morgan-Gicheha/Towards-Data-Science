import csv
filename = "data.csv"

with open(filename) as opened_file:
    reade_file = csv.reader(opened_file)
# looping throu all rows and getting the Max TemperatureF
    for row in reade_file:
        print(row)
