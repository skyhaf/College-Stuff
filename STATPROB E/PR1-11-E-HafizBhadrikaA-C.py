import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()

# C. Measures of Variability
print("Range :" + str(int(data["Active Cases"].describe()["max"] - data["Active Cases"].describe()["min"])))
print("Variance :" + str( st.pvariance(data["Active Cases"]) ))
print("Standar Deviasi :" + str( st.pstdev(data["Active Cases"]) ))
print()