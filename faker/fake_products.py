"""
Fake a csv file with 10+ millions rows

Usage: 
    python fake_products.py -h
    fake_products.py -t <total> -o <outputfile>

Examples:
    python fake_products.py -t 1000 -o products.csv
"""
#!/usr/bin/python

import sys
import getopt
import csv
import random
import time
import os
from typing import Any
from faker import Faker

fake = Faker()

BASE_PRODUCT_URL = 'https://faker.abackend.guru/products'

def get_params(argv: Any) -> dict:
    """
    Get params and return as a dict
    """
    total = 0
    outputfile = ''
    try:
        opts, _ = getopt.getopt(argv, "ht:o:", ["total=", "outputfile="])
        for opt, arg in opts:
            if opt == '-h':
                print('fake_products.py -t <total> -o <outputfile>')
                sys.exit()
            elif opt in ("-t", "--total"):
                total = arg
            elif opt in ("-o", "--outputfile"):
                outputfile = arg
        return {
            'total': int(total),
            'outputfile': outputfile
        }
    except getopt.GetoptError:
        print('fake_products.py -t <total> -o <outputfile>')
        sys.exit(2)


def generate_products(total: int, filename: str):
    """
    Write products to csv file
    """
    header = [
        'id', 'title', 'url', 'short_description',
        'description', 'price', 'quantity', 'is_active'
    ]
    file_path = f'data/{filename}'

    # Check file exists and write header first
    # newline='' to fix new blank line on windows
    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

    # Append more rows to file
    with open(file_path, 'a', encoding='UTF8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(1, total):
            _id = int(time.time())
            title = fake.text(5)
            url = f'{BASE_PRODUCT_URL}/{_id}'
            short_description = fake.text(50)
            description = fake.text(500)
            price = round(random.uniform(1.00, 2000.00), 2)
            quantity = random.randint(1, 500)
            is_active = bool(random.randint(0,1))

            row = [_id, title, url, short_description, description, price, quantity, is_active]
            writer.writerow(row)


if __name__ == "__main__":
    params = get_params(sys.argv[1:])
    generate_products(total=params['total'], filename=params['outputfile'])
