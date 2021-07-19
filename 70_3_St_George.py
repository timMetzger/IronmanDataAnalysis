###############################
# Created By: Timothy Metzger
# 70.3 St George Analysis
###############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Converts time in table from hh:mm:ss ---> mm:ss
def time_reducer(time):

    split_time = time.str.split(':', expand=True)
    time = pd.to_numeric(split_time[0])*60+pd.to_numeric(split_time[1])+pd.to_numeric(split_time[2])/60
    return time



pure_data = pd.read_csv('70_3_St_George.csv')
pd.set_option('display.max_columns',None)

data = pure_data.copy()
data['Swim'] = time_reducer(data['Swim'])
data['Bike'] = time_reducer(data['Bike'])
data['Run'] = time_reducer(data['Run'])
data['Time'] = time_reducer(data['Time'])


male_pros = data[data['Division'] == "MPRO"]
female_pros = data[data['Division'] == "FPRO"]
non_pro_males = data[data['Division'] != "MPRO"]
non_pro_females = data[data['Division'] != "FPRO"]
# Swim Analysis

quartiles = [0.25, 0.5, 0.75]
quartile_colors = ['y','r','g']

male_pros_swim_quartiles = np.quantile(male_pros['Swim'], quartiles)
female_pros_swim_quartiles = np.quantile(female_pros['Swim'], quartiles)
non_pro_males_quartiles = np.quantile(non_pro_males['Swim'],quartiles)
non_pro_females_quartiles = np.quantile(non_pro_females['Swim'],quartiles)


fig1,axs1 = plt.subplots(2,2)
axs1[0,0].hist(male_pros['Swim'],edgecolor='black')
axs1[0,1].hist(female_pros['Swim'],edgecolor='black')
axs1[1,0].hist(non_pro_males['Swim'],edgecolor='black')
axs1[1,1].hist(non_pro_females['Swim'],edgecolor='black')





axs1[0,0].set_title('Pro Male Swim Times')
axs1[0,1].set_title('Pro Female Swim Times')
axs1[1,0].set_title('Male Swim Times')
axs1[1,1].set_title('Female Swim Times')

axs1[0,0].set_ylabel('Frequency')
axs1[1,0].set_ylabel('Frequency')

axs1[0,0].set_xlabel('Time (m)')
axs1[0,1].set_xlabel('Time (m)')
axs1[1,0].set_xlabel('Time (m)')
axs1[1,1].set_xlabel('Time (m)')


for i in range(3):
    axs1[0,0].axvline(x=male_pros_swim_quartiles[i], color=quartile_colors[i],label='q{0} = {1:8.2f}'.format(i+1, male_pros_swim_quartiles[i]))
    axs1[0,1].axvline(x=female_pros_swim_quartiles[i], color=quartile_colors[i],label='q{0} = {1:8.2f}'.format(i+1, female_pros_swim_quartiles[i]))
    axs1[1,0].axvline(x=non_pro_males_quartiles[i], color=quartile_colors[i],label='q{0} = {1:8.2f}'.format(i+1, non_pro_males_quartiles[i]))
    axs1[1,1].axvline(x=non_pro_females_quartiles[i], color=quartile_colors[i],label='q{0} = {1:8.2f}'.format(i+1, non_pro_females_quartiles[i]))




axs1[0,0].legend(loc='upper right',title='Legend')
axs1[0,1].legend(loc='upper right',title='Legend')
axs1[1,0].legend(loc='upper right',title='Legend')
axs1[1,1].legend(loc='upper right',title='Legend')

plt.show()