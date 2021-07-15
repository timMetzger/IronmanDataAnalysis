import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def time_reducer(time):

    split_time = time.str.split(':', expand=True)
    time = pd.to_numeric(split_time[0])*60+pd.to_numeric(split_time[1])+pd.to_numeric(split_time[2])/100
    return time



data = pd.read_csv('70_3_St_George.csv')
pd.set_option('display.max_columns',None)
data['Swim'] = time_reducer(data['Swim'])
data['Bike'] = time_reducer(data['Bike'])
data['Run'] = time_reducer(data['Run'])
data['Time'] = time_reducer(data['Time'])
print(data.head())


#male_pros = data[data['Division'] == "MPRO"]
#female_pros = data[data['Division'] == "FPRO"]
#plt.hist(male_pros['Swim'])
#plt.show()