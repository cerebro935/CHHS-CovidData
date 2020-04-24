import json
import urllib.request as urllib
import time
import csv
from os import path

csv_file = "CAcovid19.csv"
#Columns are the objects of the dictionary
#Rows are the records of the dictionary
csv_columns = ['Most Recent Date', 'Total Count Deaths', 'ICU COVID-19 Positive Patients', 'ICU COVID-19 Suspected Patients'
              ,'Suspected COVID-19 Positive Patients', 'COVID-19 Positive Patients', '_id', 'County Name'
              ,'Total Count Confirmed']

def get_entries(offset, total, csv_total):
    #100 results return with each url call
    while offset < total:
        url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?offset='+str(offset)+'&resource_id=6cd8d424-dfaa-4bdd-9410-a3d656e1176e'
        fileobj = urllib.urlopen(url)
        s = fileobj.read()
        #Be nice to the website
        print("Offset: " + str(offset))
        time.sleep(15)
        data = json.loads(s)
        try:
            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                for row in data['result']['records']:
                    if int(row['_id']) > csv_total:
                        writer.writerow(row)
                csvfile.close()
        except IOError:
            print("I/O error")
        offset += 100

def exit_message(old_count, new_count):
    print(str(new_count-old_count) + " new entries added to "+ csv_file +". New total " 
          + str(new_count)+". Old total " + str(old_count))

def main():
    csv_total = 0
    #quick way to get the current total, request page with zero entries
    url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=6cd8d424-dfaa-4bdd-9410-a3d656e1176e&limit=0'
    fileobj = urllib.urlopen(url)
    s = fileobj.read()
    data = json.loads(s)
    total = data['result']['total']

    if path.exists(csv_file):
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            readCSV = iter(readCSV)
            next(readCSV)
            for row in readCSV:
                _id = int(row[6])
                if _id > csv_total:
                    csv_total = _id
            csvfile.close()
        if csv_total < total:
            get_entries(csv_total - (csv_total % 100), total, csv_total)
        exit_message(csv_total, total)
    else:
        offset = 0
        url = 'https://data.chhs.ca.gov/api/3/action/datastore_search?offset='+str(offset)+'&resource_id=6cd8d424-dfaa-4bdd-9410-a3d656e1176e'
        fileobj = urllib.urlopen(url)
        s = fileobj.read()
        print("Offset: "  + str(offset))
        time.sleep(15)
        #JSON string into a dictionary
        data = json.loads(s)
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for row in data['result']['records']:
                    writer.writerow(row)
                csvfile.close()
        except IOError:
            print("I/O error")
        offset += 100
        get_entries(offset, total, 0)
        exit_message(0, total)

if __name__ == "__main__":
    main()
