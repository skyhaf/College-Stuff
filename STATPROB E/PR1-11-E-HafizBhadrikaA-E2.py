import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()


temp_dict = {}
raw_dict = {}

for i in data.values:
    temp_dict[i[0]] = i[1:5]

for key in temp_dict:
    # 0.5TD + 0.25AC + 0.25SC 
    rawNegara = ((0.5 * temp_dict[key][0]) +
                (0.25 * temp_dict[key][1]) + 
                (0.25 * temp_dict[key][2]))
    raw_dict[key] = rawNegara

hasil_raw = sorted(raw_dict.items(), key=lambda x: x[1], reverse=True)    

print("Berikut negara terpilih dengan raw score")
for i in range(4):
    print(str(i+1) + " " + str(hasil_raw[i][0] ))
