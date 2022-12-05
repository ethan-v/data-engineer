"""
Read CSV file each line as a list
"""
import csv
import time

info = {
    'total_rows': 0,
    'latest_id': 0,
}

def read_csv():
    with open ('faker/data/products.csv','r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # skip first row
        for row in reader:
            # print(row)
            info['total_rows'] = info['total_rows'] + 1


if __name__ == '__main__':
    print("Reading csv file ...")
    start_time = time.time()
    read_csv()
    print("Complete reading csv file")
    print("--- %s seconds ---" % (time.time() - start_time))
    print(info)