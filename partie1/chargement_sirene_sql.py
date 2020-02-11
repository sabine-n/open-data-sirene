#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:30:22 2019

@author: utilisateur
"""

import pandas as pd
from sqlalchemy import create_engine
import time

engine = create_engine('mysql+pymysql://root@localhost/Simplon')

#A= pd.read_sql_query('SELECT * FROM jeux_video',engine)
#print(A)


def importcsv(link, table, date):
    print("Lecture des données")
    start_time = time.time()
    csize = 200000
    df = pd.read_csv(link, compression = 'zip', chunksize = csize)
    print("Données lu")
    i = csize
    for chunk in df:
        chunk.to_sql(table, con = engine, if_exists='append', index = False)
        i += csize
        print(i)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


importcsv('https://www.data.gouv.fr/fr/datasets/r/09af65ff-c1c6-40bb-bfcb-b80f7ac93b72', 'stock_etab_hist', ['dateFiN', 'dateDebut'])

##chunksize = 10 ** 2
##for chunk in pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/377fd07c-e37f-491a-a507-7bf5b690804b", chunksize=chunksize):
##    process(chunk)
#
#
#df_chunk = pd.read_csv(r"https://www.data.gouv.fr/fr/datasets/r/377fd07c-e37f-491a-a507-7bf5b690804b", iterator=True, chunksize=1000,sep='|', header=None,encoding='latin-1')
#
##chunk_list = []  # append each chunk df here 
##
### Each chunk is in df format
##for chunk in df_chunk:  
##    # perform data filtering 
##    chunk_filter = chunk_preprocessing(chunk)
##    
##    # Once the data filtering is done, append the chunk to list
##    chunk_list.append(chunk_filter)
#    
## concat the list into dataframe 
#df_concat = pd.concat([chunk[chunk['n3']>0] for chunk in df_chunk])
#
##print(df_concat)
#
#B = pd.read_sql_query('SELECT siren FROM stock_etab LIMIT 10',engine)
#print(B)



