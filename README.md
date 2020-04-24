# CHHS-CovidData
This script uses the CKAN Datastore API to request information from the California Health and Human Services Open Data website and stores the information in a csv file titled "CAcovid19.csv".

The data requested is the "Statewide daily inventory of hospital status aggregated to the county level. This dataset depicts: total confirmed cases, total deaths, both positive and suspected positive COVID-19 patients, as well as Intensive Care Unit (ICU) positive and suspected positive COVID-19 patients."

This data can be quickly downloaded at https://data.chhs.ca.gov/dataset/6882c390-b2d7-4b9a-aefa-2068cee63e47/resource/6cd8d424-dfaa-4bdd-9410-a3d656e1176e/download/covid19data.csv and the download is much faster than the script. This is mainly because the script waits 15 seconds between page requests as a courtesy to the website. Alter the sleep statements in the script at your own discretion.

So whats the point of this script?
Ideally, an existing copy of the dataset titled "CAcovid19.csv" would exist in the same directory as the script. The script would only be ran as to check and update the local csv file with any new entries. So, this script can be used to make sure the dataset has the most up-to-date information before the data is used in a larger project without having to redownload the entire dataset.
