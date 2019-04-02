#!/usr/bin/env python

import os
import argparse
import glob
import json
import logging
from collections import OrderedDict

def check_duplicate_keys(release_listing):
    keys = set()
    for entry in release_listing:
        key = entry['encoding_path']
        if key in keys:
            raise Exception('%s already in list!', key)
        keys.add(key)

def parse_args():
    parser = argparse.ArgumentParser(
        description='Sorts release yang2proto maps.'
    )
    parser.add_argument('--base_dir',
        help='base directory containing release directories',
        default='protos/',
        dest='base_dir'
    )
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_args()
    if not os.path.isdir(args.base_dir):
        raise SystemExit('Base directory does not exist!')
    release_dirs = [
        release for release in os.listdir(args.base_dir)
        if os.path.isdir(os.path.join(args.base_dir, release))
    ]
    basename_glob = '*yang2proto_map.json'
    for release_dir in release_dirs:
        logging.info('Parsing release dir %s', release_dir)
        release_path = os.path.join(args.base_dir, release_dir)
        yang2proto_file_glob = glob.glob(os.path.join(release_path, basename_glob))
        for yang2proto_filename in yang2proto_file_glob:
            logging.info('Parsing map %s', yang2proto_filename)
            yang2proto_listing = []
            with open(yang2proto_filename, 'r') as yang2proto_fd:
                yang2proto_listing.extend(json.load(yang2proto_fd, object_pairs_hook=OrderedDict))
            yang2proto_listing = sorted(yang2proto_listing, key=lambda k: k['encoding_path'])
            check_duplicate_keys(yang2proto_listing)
            with open(yang2proto_filename, 'w') as yang2proto_fd:
                json.dump(yang2proto_listing, yang2proto_fd, sort_keys=True, indent=4)

if __name__ == '__main__':
    main()
