import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()

stdevTD = st.pstdev(data["Total Deaths"])
stdevAC = st.pstdev(data["Active Cases"])
stdevSC = st.pstdev(data["Serious, Critical"])
meanTD = data["Total Deaths"].describe()["mean"]
meanAC = data["Active Cases"].describe()["mean"]
meanSC = data["Serious, Critical"].describe()["mean"]

temp_dict = {}
standar_dict = {}

for i in data.values:
    temp_dict[i[0]] = i[1:5]

for key in temp_dict:
    # 0.5TD + 0.25AC + 0.25SC 
    standardNegara = ( (0.5 * ( (temp_dict[key][0] - meanTD)/stdevTD ) ) +
                     (0.25 * ( (temp_dict[key][1] - meanAC)/stdevAC ) ) +
                     (0.25 * ( (temp_dict[key][2] - meanSC)/stdevSC ) ) )
    standar_dict[key] = standardNegara

hasil_standard = sorted(standar_dict.items(), key=lambda x: x[1], reverse=True)    

print("Berikut negara terpilih dengan standard score")
for i in range(4):
    print(str(i+1) + " " + str(hasil_standard[i][0] ))
