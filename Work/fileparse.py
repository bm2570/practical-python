# fileparse.py
#
# Exercise 3.3

import csv
import sys

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):

    with open(filename) as f:
        rows = csv.reader(f)


        headers = next(rows) if has_headers else []


        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
		
        for row in rows:
		
            if not row:   
                continue

            if select:
                row = [row[index] for index in indices]
				
            if types:
                row=[func(val) for func, val in zip(types,row)]
	
            if headers:
                record=dict(zip(headers,row))
			
            else:
                record=tuple(row)
		            
            #record = dict(zip(headers, row))
            records.append(record)

    return records

csvfile=sys.argv[1]
portfolio = parse_csv(csvfile)
print (portfolio)

