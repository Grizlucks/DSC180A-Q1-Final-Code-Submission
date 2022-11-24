#!/usr/bin/env python

import sys
import json

from etl import get_data

def main(targets):
    if 'test' in targets:
        with open('test-params.json') as fh:
            data_params = json.load(fh)
        get_data(**data_params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)