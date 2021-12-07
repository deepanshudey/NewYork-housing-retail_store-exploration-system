import wget
from os import mkdir
from shutil import rmtree

with open('code/dataset.txt') as datasets_file:
    urls = datasets_file.readlines()

    # if len(urls) > 5:
    #     raise Exception("Too many datasets were specified")

    rmtree('data', ignore_errors=True)
    mkdir('data')

    for u in urls:
        f = wget.download(u.rstrip(), 'data/')
        print(f)

##########################################################################################

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 5000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("hg8x-zxpr", limit=5000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

#print(results_df)
results_df.to_csv('data/housing.csv')