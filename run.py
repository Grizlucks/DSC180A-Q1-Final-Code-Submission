#!/usr/bin/env python

import sys
import json

from src.data.etl import get_data
from src.features.build_features import get_features


def main(targets):
    if "test" in targets:
        with open("test-params.json") as fh:
            data_params = json.load(fh)
        get_data(**data_params)
        get_features(**data_params)


if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
