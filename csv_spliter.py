"""
Split large CSV file
"""
chunk_size = 40000

FILE_PATH = 'faker/data/products.csv'

def write_chunk(part, lines):
    split_filename = f'faker/data/data_part_'+ str(part) +'.csv'
    with open(split_filename, 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)

with open(FILE_PATH, "r") as f:
    count = 0
    header = f.readline()
    lines = []
    for line in f:
        count += 1
        lines.append(line)
        if count % chunk_size == 0:
            write_chunk(count // chunk_size, lines)
            lines = []
    # write remainder
    if len(lines) > 0:
        write_chunk((count // chunk_size) + 1, lines)