import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()
# B. Measures of Central Tendency 
print("Mean :" + str(data["Active Cases"].describe()["mean"]))
print("Median :" + str(data["Active Cases"].describe()["50%"]))
print("Modus :" + str(st.mode(data["Active Cases"])))
print()

