# Created By: Timothy Metzger
# Program takes links from directory csv and creates dataframes for each race
###############################
import ssl
import urllib.request
import csv
import pandas as pd
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


with open('2015_present.csv',newline='')as f:
    reader = csv.reader(f)
    all_races = list(reader)

base_url = "https://www.endurance-data.com/"
for race in  all_races[1:]:
    race_url = base_url+race[-1]
    print(race_url)

# ironman_results = []
# for page in range(1, 53):
#     html = urllib.request.urlopen(race_url.format(page), context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     athletes = soup.find_all(class_='pointer')
#     for athlete in athletes:
#         athleteStats = []
#         for stat in athlete:
#             try:
#                 athleteStats.append(stat.text)
#             except AttributeError:
#                 continue
#         ironman_results.append(athleteStats)
#
# ironman_dataFrame = pd.DataFrame.from_records(ironman_results)
# ironman_dataFrame.drop(ironman_dataFrame.columns[[0, 1]], axis=1, inplace=True)
# ironman_dataFrame.rename(columns={2: 'Place',
#                                   3: 'Name',
#                                   4: 'Bib',
#                                   5: 'Division',
#                                   6: 'Nation',
#                                   7: 'Swim',
#                                   8: 'Bike',
#                                   9: 'Run',
#                                   10: 'Time'}, inplace=True)
#
#
# print(ironman_dataFrame.head())
# ironman_dataFrame.to_csv('70_3_St_George.csv',index=False)