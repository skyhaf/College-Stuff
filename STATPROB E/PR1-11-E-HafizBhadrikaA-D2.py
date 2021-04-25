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
IQR = ((data["Active Cases"].describe()["75%"] - data["Active Cases"].describe()["25%"]))
RLB = int(Q1) - (1.5*(int(IQR)))
RUB = int(Q3) + (1.5*(int(IQR)))
print("IQR :" + str(IQR))
if(RLB < -1):
    RLB = 0
print("RLB :" + str(RLB))
print("RUB :" + str(RUB))