#!python3

import json
import os

import pandas
from kafka import KafkaConsumer
from sqlalchemy import create_engine

# def transformStream(df):
#     df = df \
#             .groupby(['date_search']) \
#             .agg({'id_search':'count'}) \
#             .reset_index()
#     df.columns = 'date_search', 'count_search'

#     return df.head(1)

if __name__ == "__main__":
    print("starting the consumer")
    path = os.getcwd()+"/"

    user_name = 'postgres'
    password = 'admin'
    database = 'dwh_digitalskola'
    ip = 'localhost'
    

    #connect database
    try:
        engine = create_engine(f"postgresql://{user_name}:{password}@{ip}:5432/{database}")
        print(f"[INFO] Successfully Connect Database .....")
    except:
        print(f"[INFO] Error Connect Database .....")

    #try connect kafka server
    try:
        consumer = KafkaConsumer("final-project", bootstrap_servers='localhost')
        print(f"[INFO] Successfully Connect Kafka Server .....")
    except:
        print(f"[INFO] Error Connect Kafka Server .....")

    #read kafka server
    for msg in consumer:
        data = json.loads(msg.value)
        print(f"Records = {json.loads(msg.value)}")

        df = pandas.DataFrame(data, index=[0])

        df.to_sql('dim_streaming_transaction', engine, if_exists='append', index=False)