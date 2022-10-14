#!python3

#import_library
import json
import os
from datetime import datetime

import conn_warehouse
import numpy as np
import pandas as pd
import sqlparse

import connection


def load_data_to_local(trans, eng) :
    query_order = sqlparse.format(
       open(
           path_query+'local_'+trans+'.sql','r'
           ).read(), strip_comments=True).strip()

    #get_data_from_database_dwh
    data = pd.read_sql(query_order,eng)    

    #upload 
    path = os.getcwd()
    directory = path+'/'+'mapreduce_transform/input'+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    data.to_csv(f"{directory}dim_{trans}s_{filetime}.csv", index=False)
    print(f"[INFO] Upload Data {trans}s in LOCAL Success .....")


if __name__ == '__main__':
    filetime = datetime.now().strftime('%Y%m%d')    

    #connect db source
    conf = connection.config('postgresql')
    conn, engine = connection.psql_conn(conf)
    cursor = conn.cursor()

    #connect db warehouse
    conn_dwh, engine_dwh  = conn_warehouse.conn()
    cursor_dwh = conn_dwh.cursor()

    #query extract db source
    path_query = os.getcwd()+'/queries/'
    query = sqlparse.format(
        open(
            path_query+'dbsource_query.sql','r'
            ).read(), strip_comments=True).strip()

    #query load db warehouse
    query_dwh = sqlparse.format(
        open(
            path_query+'dwh_design.sql','r'
            ).read(), strip_comments=True).strip()   

    try :
        print(f"[INFO] Service Extract Data Running.....")
        
        #get data from database source
        df = pd.read_sql(query, engine)

        #insert data db source to dwh
        cursor_dwh.execute(query_dwh)
        conn_dwh.commit()
        df.to_sql('dim_transaction_order', engine_dwh, if_exists='append', index=False)
        print(f"[INFO] Create Table DWH Success .....")                
       
        #load data dwh to local csv
        #list_data = ['customer', 'transaction', 'product']
        list_data = ['transaction']
        for i in range(len(list_data)):
            load_data_to_local(list_data[i], engine_dwh)
        
    except :
        print(f"[INFO] Service Extract & Load Data Failed .....")