import requests
import pandas as pd 
import csv

from requests.api import head

def run_crypto_etl():

    url = 'http://api.coincap.io/v2/assets'

    headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }
    response = requests.request("GET",url,headers=headers)
    myjson = response.json()
    ourdata = []
    # adding header to the csv file.
    csvheader = ['ID','RANK','SYMBOL','NAME','PRICE(USD)'] 


    # to transform data or to fetch particular columns
    for x in myjson['data']:
        listing = [x['id'],x['rank'],x['symbol'],x['name'],x['priceUsd']]
        ourdata.append(listing)


    # Open the CSV file for writing
    with open('crypto_data.csv', 'w',encoding='UTF8', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the data to the CSV file
        writer.writerow(csvheader)
        writer.writerows(ourdata)

    df = pd.DataFrame(ourdata)
    df.to_csv("s3://etl-airflow-crypto/crypto_data.csv")

    print('write the data into csv is done...!!')

