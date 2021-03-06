###############################
# Created By: Timothy Metzger
# Data cleaning
###############################

import pandas as pd
import csv

# Converts time in table from hh:mm:ss ---> mm:ss
def time_reducer(time):

    split_time = time.str.split(':', expand=True)
    time = pd.to_numeric(split_time[0])*60+pd.to_numeric(split_time[1])+pd.to_numeric(split_time[2])/60
    return time

def try_code(key,dic):
    country = str(key[0])
    try:
        country_code = dic[country]
    except KeyError:
        country_code = country
    return country_code

def main():
    # Getting a dictionary to convert country names to ISO 3166 codes
    country_code_dic = {}
    with open('wikipedia-iso-country-codes.csv') as f:
        file = csv.DictReader(f,delimiter=",")
        for line in file:
            country_code_dic[line['English short name lower case']] = line['Alpha-2 code']

    pure_data = pd.read_csv('Ironman_70_3s.csv')

    # Creating a copy of the data for manipulation
    data = pure_data.copy()
    data = data[data['Time'] != 'DNS']
    # # Converting the time columns to a more useful format
    data['Swim'] = time_reducer(data['Swim'])
    data['Bike'] = time_reducer(data['Bike'])
    data['Run'] = time_reducer(data['Run'])
    data['Time'] = time_reducer(data['Time'])
    #
    # # Converting the location field to separate city and country columns with country code
    data['Country'] = data.apply(lambda row: try_code([row['Location'].split(", ")[-1]], country_code_dic), axis=1)
    data['City'] = data.apply(lambda row: row['Location'].split(", ")[0], axis=1)

    # Get approximate temperature at 6:00 AM, 9:00 AM, 12:00 PM, 3:00 PM, 6:00 PM, 9:00 PM



    data.to_csv('cleaned_data.csv',index=False)




main()