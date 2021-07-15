###############################
# Created By: Timothy Metzger
###############################

import urllib.request, urllib.parse, urllib.error
import matplotlib as plt
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.endurance-data.com/en/results/511-ironman-703-st-george/all/{}/"

ironman_results = []
for page in range(1,53):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    athletes = soup.find_all(class_='pointer')
    for athlete in athletes:
        athleteStats = []
        for stat in athlete:
            try:
                print(stat.get_text())
            except AttributeError:
                continue
            athleteStats.append(stat.text)
        ironman_results.append(athleteStats)



print(ironman_results)





