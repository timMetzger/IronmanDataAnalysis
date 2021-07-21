###############################
# Created By: Timothy Metzger
# Program takes links from directory csv and creates dataframes for each race
###############################
import ssl
import urllib.request
import csv
import time
import pandas as pd
from bs4 import BeautifulSoup
from os import path


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Getting time to find program execution time
start_time = time.time()

# Reading in directory csv as a list
with open('2015_present.csv', newline='')as f:
    reader = csv.reader(f)
    all_races = list(reader)

base_url = "https://www.endurance-data.com"
# Building csvs for each race
for race in all_races[2:]:
    # Replacing non file directory compatible items
    print(race)
    race_name = race[0].replace(" ", "_")
    race_name = race_name.replace(".","_")
    race_date = race[1].replace("/","_")

    # Skipping race if already recorded
    if path.exists('races/'+race_name+race_date+".csv"):
        continue
    # Setting up pagination navigation loop
    race_url = base_url + race[-1] + '{}'
    main_html = urllib.request.urlopen(race_url.format(1), context=ctx).read()
    main_soup = BeautifulSoup(main_html, 'html.parser')
    pagination = main_soup(class_='page-item')
    num_pages = int(pagination[-2].text)
    ironman_results = []
    for i in range(1, num_pages + 1):
        html = urllib.request.urlopen(race_url.format(i), context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        athletes = soup.find_all(class_='pointer')
        # Building athlete data
        for athlete in athletes:
            athleteStats = []
            for stat in athlete:
                try:
                    athleteStats.append(stat.text)
                except AttributeError:
                    continue
            ironman_results.append(athleteStats)

        ironman_dataFrame = pd.DataFrame.from_records(ironman_results)
        ironman_dataFrame.drop(ironman_dataFrame.columns[[0, 1]], axis=1, inplace=True)
        ironman_dataFrame.rename(columns={2: 'Place',
                                          3: 'Name',
                                          4: 'Bib',
                                          5: 'Division',
                                          6: 'Nation',
                                          7: 'Swim',
                                          8: 'Bike',
                                          9: 'Run',
                                          10: 'Time'}, inplace=True)
        ironman_dataFrame['Race'] = race[0]
        ironman_dataFrame['Date'] = race[1]
        ironman_dataFrame['Location'] = race[2]

    # Saving race dataframe into csv's
    ironman_dataFrame.to_csv("races/"+race_name+race_date+'.csv',index=False)
    print(ironman_dataFrame)

print("--- %s seconds ---" % (time.time() - start_time))
