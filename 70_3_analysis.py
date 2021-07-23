###############################
# Created By: Timothy Metzger
# Data analysis of 70.3 races around the world
###############################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    pd.set_option('display.max_columns', None)

    data = pd.read_csv('cleaned_data.csv')

    pro_men = data[data['Division'] == 'MPRO']
    pro_women = data[data['Division'] == 'FPRO']

    QUARTILES = [0.25, 0.5, 0.75]
    QUARTILE_COLORS = ['y', 'r', 'g']

    # Swim Plots
    pro_men_swim_quartiles = np.quantile(pro_men['Swim'], QUARTILES)
    pro_women_swim_quartiles = np.quantile(pro_women['Swim'], QUARTILES)
    fig1, axs1 = plt.subplots(1, 2)
    # Plotting quartiles
    for i in range(3):
        axs1[0].axvline(x=pro_men_swim_quartiles[i], color=QUARTILE_COLORS[i],
                        label='q{0} = {1:8.2f}'.format(i + 1, pro_men_swim_quartiles[i]))
        axs1[1].axvline(x=pro_women_swim_quartiles[i], color=QUARTILE_COLORS[i],
                        label='q{0} = {1:8.2f}'.format(i + 1, pro_women_swim_quartiles[i]))
    # Plotting histograms
    axs1[0].hist(pro_men['Swim'], edgecolor='black', bins=20)
    axs1[1].hist(pro_women['Swim'], edgecolor='black', bins=20)

    axs1[0].set_title('Pro Men Swim Time')
    axs1[1].set_title('Pro Women Swim Time')

    axs1[0].set_xlabel('Time (m)')
    axs1[1].set_xlabel('Time (m)')

    axs1[0].legend(loc='upper right', title='legend')
    axs1[1].legend(loc='upper right', title='legend')
    pro_men_best_swimmers = pro_men[pro_men['Swim'] < pro_men_swim_quartiles[0]]
    pro_men_worst_swimmers = pro_men[pro_men['Swim'] > pro_men_swim_quartiles[2]]

    fig2, axs2 = plt.subplots(1,2)
    print(pro_men_best_swimmers['Place'].value_counts())
    pro_men_best_swimmers['Place'].value_counts().plot(kind='bar',ax=axs2[0])
    pro_men_worst_swimmers['Place'].value_counts().plot(kind='bar',ax=axs2[1])

    # fig2, axs2 = plt.subplots(1,2)
    # #axs2[0].bar(pro_men_best_swimmers_placing, edgecolor='black')
    # #axs2[1].bar(pro_men_worst_swimmers_placing, edgecolor='black')
    #
    # axs2[0].set_title('Placings of Pro Men above 75% Quartile')
    # axs2[1].set_title('Placings of Pro Women above 75% Quartile')
    #
    # print(pro_men_best_swimmers_placing[0:])


    plt.show()




main()
