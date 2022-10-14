#!python3

import csv
import json

from mr3px.csvprotocol import CsvProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep

cols = 'id_transaction,id_customer,name_customer,date_transaction,product_kategory,product_transaction,amount_transaction'.split(',')


def csv_readline(line):
    for row in csv.reader([line]):
        return row

class OrderDateTotalProduct(MRJob):
    OUTPUT_PROTOCOL = CsvProtocol

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        row = dict(zip(cols, csv_readline(line)))

        if row['product_transaction'] != 'product_transaction':
            yield row['date_transaction'][0:7], str(row['product_transaction'])

    def reducer(self, key, values):
        set_k = set(values)
        val_list = list(set_k)
        total = 0
        for row in val_list:
            total = total +1
        yield None, (key, total)

if __name__ == '__main__':
    OrderDateTotalProduct.run()