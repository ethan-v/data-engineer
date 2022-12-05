"""
Simple CLI
"""
#!/usr/bin/python

import sys
import getopt
from typing import Any


def get_params(argv: Any) -> dict:
    """
    Get params and return as a dict
    """
    total = 0
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "ht:o:", ["total=", "outputfile="]) 
        for opt, arg in opts:
            if opt == '-h':
                print('simple_cli.py -t <total> -o <outputfile>')
                sys.exit()
            elif opt in ("-t", "--total"):
                total = arg
            elif opt in ("-o", "--outputfile"):
                outputfile = arg
        print(f'Max rows = {total}')
        print(f'Output file = {outputfile}')
        return {
            'total': int(total),
            'outputfile': outputfile
        }
    except getopt.GetoptError:
        print('simple_cli -t <total> -o <outputfile>')
        sys.exit(2)


if __name__ == "__main__":
    params = get_params(sys.argv[1:])
    print(params)
