"""
Python write csv file with UTF8
"""
import csv

header = ['name', 'country_code', 'language_code']
data = ['Vietnam', 'VN', 'VI']

with open(f'data/countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
