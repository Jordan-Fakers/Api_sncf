#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import csv
import pandas as pd
import pprint
import os
import unittest


class ReadApiSncf():

    def __init__(self):
        self.url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.token_auth =  '2da277f8-8a43-49f3-9468-5f32fbbed6e7'        
        self.list_hrefs = []
        self.filename_json = "stop_areas_jordan"
        self.filename_csv = "jordan_csv"
    
    def read_json(self):

        response = requests.get(self.url,auth=(self.token_auth,''))
        with open(self.filename_json + '.json', mode='w') as file :
            json.dump(response.json(),file, indent=4)
    
    def read_links(self):

        with open('stop_areas_jordan.json') as json_stop_areas_file:
            data = json.load(json_stop_areas_file)

        links = data['links']

        for loop_link in links:

            if type(loop_link) == dict:
                if "href" in loop_link.keys():
                    local_href = loop_link["href"]
                    self.list_hrefs.append(local_href)
                else:
                    print("Missing key id")
            else:
                print('Unexpected format' +type(loop_link))
    
    def save_csv(self): 
        with open(self.filename_csv + '.csv', mode="w") as f:
            csv_writer = csv.writer(f, delimiter=';')
            if type(self.list_hrefs) == list:
                for row in self.list_hrefs:
                # écriture du contenu du row dans la nouvelle ligne du fichier csv
                    csv_writer.writerow(row)
            else: 
                print("Unexpected input")
            print('Csv is okey')

sncf = ReadApiSncf()
sncf.read_json()
sncf.read_links()
sncf.save_csv()