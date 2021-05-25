import csv
import pandas
import requests
import json


URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
api_key = '079uUMHFuOTASHP1KOUBHlrhTMGYtZShSF3t-tMcSoI'

fields =['latitude','longitude','address','postalcode']
csvFile = open('padd.csv', 'a',newline='')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(fields);
'''
with open("padd.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
'''
filenmae ='in.csv'
df = pandas.read_csv(filenmae)

for index, row in df.iterrows():
    #print (row[1])
#    print (row[2])
    lati = row[1]
    long= row[2]
    PARAMS = {'apikey':api_key,'at':'{},{}'.format(lati,long)}
    r = requests.get(url = URL ,params=PARAMS)
    data = r.json()
    #print (data)
    address = data['items'][0]['address']['city']
    pcode = data['items'][0]['address']['postalCode']

    set = [lati,long,address,pcode]
    print (set)
    csvWriter.writerow(set)
'''
    csvWriter.writerow([long])
    csvWriter.writerow([address])
    csvWriter.writerow([pcode])
    #print (address)
    #print (pcode)
'''
df = pandas.read_csv('padd.csv')
print(df)
