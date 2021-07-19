###############################
# Created By: Timothy Metzger
# Program takes information from a directory of races and compiles it into a dataframe with a link to the results
###############################
import ssl
import urllib.request
import re
import pandas as pd
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Finding the number of events in the catalog
main_url = "https://www.endurance-data.com/en/competitions/1/"
main_html = urllib.request.urlopen(main_url, context=ctx).read()
main_soup = BeautifulSoup(main_html, 'html.parser')
pagination = main_soup(class_='page-item')
num_pages = int(pagination[3].text)
dir_url = "https://www.endurance-data.com/en/competitions/{}/"
complete_race_info = []

# Extracting information from each race
for i in range(1, num_pages + 1):
    dir_html = urllib.request.urlopen(dir_url.format(i), context=ctx).read()
    dir_soup = BeautifulSoup(dir_html, 'html.parser')
    races = dir_soup.find_all(class_='cursor-pointer')

    for race in races:
        race_stats = []
        race_info = race.find_all('td')
        race_results = race.find_all('a')
        for info in race_info:
            try:
                if not re.match('[\n]+', info.text):
                    race_stats.append(info.text)
            except Exception:
                continue
        race_stats.append(race_results[2]['href'])
        complete_race_info.append(race_stats)

all_races_dataframe = pd.DataFrame.from_records(complete_race_info)
all_races_dataframe.rename(columns={
    0: 'Event',
    1: 'Date',
    2: 'Location',
    3: 'Athletes',
    4: 'Results'
}, inplace=True)
all_races_dataframe.to_csv('2015_present.csv', index=False)


