#!python3

#add_library
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = 'postgres'
    password = 'postgres'
    database = 'postgres'
    ip = 'localhost'

#info if success or not succes
    try:
        engine = create_engine(f"postgresql://{username}:{password}@{ip}:5432/{database}")
        print(f"[INFO] Success Connect PostgresSQL .....")
    except:
        print(f"[INFO] Error Connect PostgresSQL .....")
    
    list_filename = ['customer','product','transaction']

    #dump file to postgres
    for file in list_filename:
        pd.read_csv(f"bigdata_{file}.csv").to_sql(f"bigdata_{file}", con=engine)
        print(f"[INFO] Success Dump File {file} .....")