#
The datasets like housing, retail stores, etc. present in NYC are collected to create an effective database. An application is created that helps users to search for list of hospitals, retail stores, and housing nearest to them or at a particular pincode. A non-relational database containing list of schools is also created using the MongoDB.

GitHub Repository - https://github.com/deepanshudey/NewYork-housing-retail_store-exploration-system

## Data

Main Dataset: Housing Projects in NYC
1. 41 attributes and around 6000 data points
2. https://data.cityofnewyork.us/Housing-Development/Housing-New-York-Units-by-Building/hg8x-zxpr

Supplement Dataset: 

1. Retail Stores in NYC
   a. 15 attributes and around 400 data points
   b. https://data.cityofnewyork.us/Health/Recognized-Shop-Healthy-Stores/ud4g-9x9z

2. Hospital (Patient Care Locations) in NYC
   a. 15 attributes and around 78 data points
   b. https://data.cityofnewyork.us/Health/Recognized-Shop-Healthy-Stores/ud4g-9x9z



Non-Relational Dataset:
1. NYC List of Schools
   a. 19 attributes and around 222 data points
   b. https://data.cityofnewyork.us/Education/iZone-School-List/cr93-x2xf


All the datasets used are open datasets and are publicly available and owned by NY Open Data organization.
## Database Setup

All the required datasets will be generated in the "Data" folder

To setup the database locally:

Run command -- 'pip3 install -r requirements.txt' to install the dependencies/libraries required

1. Login as 'Postgres' using:
   psql -U postgres
   
2. Run database.sql as a super user:
   psql -U postgres postgres < setup.sql

   This creates database project and the user "Admin" who is the owner/administrator of the database. Then the required priveleges are  granted to the owner.

## Loading Data
All the files should be present inside the 'code' folder. 

'dataset.txt' contains the api links and should also be present inside the 'code' folder.




The data can be loaded by (Use python3):
 
1. Run `code/retrieve_data.py` to make API call and download the required datasets. The data folder will be generated automatically and data will be also downloaded in this folder.

2. Run `code/load_data.py` to load the dataset. Following files will run automatically:
    
    a. This will automatically run `schema.sql` and will create the schema for the database. 

    b. Next, preprocess() method of `preprocessing.py` is called to clean and normalize the dataset.
    
    c. `load.py` loads the final dataset used in the project.

3. Run `code/non_relational.py` to load the Non-Relational dataset. 



## Running the Application

To run the application run `code/application.py` file and choose the options specified in the Menu.


## Dependencies

`requirements.txt` has a list of required packages used in the project.
