#!python3

import json
import time

import numpy as np
import pandas as pd
from kafka import KafkaProducer


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

if __name__ == "__main__":

    #read_data
    file = pd.read_csv('bigdata_log.csv').to_dict(orient='records')

    #connect_kafka_server
    producer = KafkaProducer(bootstrap_servers=['localhost'], 
                             value_serializer=json_serializer)
    
    #push_data_to_kafka_server_with_topic_"final_project"
    while True:
        for data in file:
            print(data)
            producer.send("final_project", data)
            #time.sleep(1)