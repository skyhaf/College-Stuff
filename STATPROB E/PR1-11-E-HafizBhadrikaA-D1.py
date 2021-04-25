import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()

# D. Measures of Positions 
Q1 = (int(data["Active Cases"].describe()["25%"]))
Q3 = (int(data["Active Cases"].describe()["75%"]))
print("Persentil-25 :" + str(Q1))
print("Persentil-75 :" + str(Q3))
