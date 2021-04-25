import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mclr
import pandas as pd
import statistics as st

data = pd.read_csv("/Users/skyhaf/Documents/Semester 4/STATPROB E/PR/final_covid_19_dataset (1).csv")

plt.figure(figsize=(10,5))
plt.title("Table Histogram")
plt.hist(data['Active Cases'],bins=[i for i in range(0, 1000000, 100000)],color='deepskyblue')
plt.show()
plt.clf()