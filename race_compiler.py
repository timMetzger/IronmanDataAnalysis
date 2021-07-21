###############################
# Created By: Timothy Metzger
# Compiles csv into one csv
###############################

import pandas as pd
import glob

all_files = glob.glob('races/Ironman_70_3_*.csv')

all_races_list = []
for file in all_files:
    df = pd.read_csv(file, index_col=None, header=0)
    all_races_list.append(df)

pure_data = pd.concat(all_races_list, axis=0, ignore_index=True)
pure_data.drop('11', axis=1, inplace=True)

pure_data.to_csv('Ironman_70_3s.csv')
