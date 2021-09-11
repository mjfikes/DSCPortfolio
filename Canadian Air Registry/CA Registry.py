import pandas as pd
import csv
import requests
import urllib3
import io
import zipfile

import os
import sys

owner={}
heads = []
with requests.get("https://wwwapps.tc.gc.ca/Saf-Sec-Sur/2/CCARCS-RIACC/download/ccarcsdb.zip") as response, io.BytesIO() as mem_zf:
    # Copy into an in-memory zipfile
    mem_zf.write(response.content)

    # open as a zip
    zipf = zipfile.ZipFile(mem_zf)

    with io.TextIOWrapper(zipf.open('carslay.out', 'r'), encoding='iso-8859-1') as outfile:
        headerlist = csv.reader(x.replace('\0','') for x in outfile)
        for row in headerlist:
            if (row == []):
                break
            
            heads.append(row[0].lstrip()[0:33])
    
    newheads = [i.split()[1] for i in heads]
    currheads = newheads[1:47]
    ownerheads = newheads[49:]
    
    with io.TextIOWrapper(zipf.open('carsownr.txt', 'r'), encoding='iso-8859-1') as ownerfile:
        #ownerlist = csv.reader(x.replace('\0','') for x in ownerfile)
        owners = pd.read_csv(ownerfile,header=None)
        
        #for row in ownerlist:
        #    if (row == []):
        #        break
        #    else:
        #        owner[row[0].lstrip()] = row[1]

    with io.TextIOWrapper(zipf.open('carscurr.txt', 'r'), encoding='iso-8859-1') as csvfile:
        airplanes = csv.reader(csvfile, delimiter=',', quotechar='"')
        planes = pd.read_csv(csvfile,header=None)

owners.columns=ownerheads
planes = planes.iloc[: , :-1]
planes.columns=currheads

CA_registry = pd.merge(planes,owners,how='inner',left_on='MARK',right_on='MARK_LINK')
CA_registry.to_excel('CA_registry.xls')
