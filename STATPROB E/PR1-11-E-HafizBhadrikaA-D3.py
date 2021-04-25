import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

print()
print("Berikut data yang ditampilkan")
print()

plt.boxplot(data["Active Cases"])

plt.show()
