# who.py
#
# INSTRUCTIONS
# ------------------
# 1. Using one of the languages listed below, make an HTTP GET request to:
# GET https://app.optimaldynamics.io/eng-interviews/q0/<secret>/all
# [ "rachel", "mike", "harvey", "louis", "jessica", "donna", "katrina" ]
#
# 2. Make multiple HTTP GET requests to fetch the information associated with / details of every name listed above one by one:
#
# GET https://app.optimaldynamics.io/eng-interviews/q0/<secret>/mike
# { "key": "mike", "first": "Mike", "last": "Ross", "role": "Associate" }

import os
import json
from pprint import pprint
import pandas as pd
import csv
import logging
import requests
import coloredlogs
from pathlib import Path
from argparse import ArgumentParser
from src.config import config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
coloredlogs.install()

class ODClient:
  def __init__(self):
    self.people = []
    self.details = []

  def get_people(self):
    try:
      response = requests.get(url=f'{config.OD_ENDPOINT_PREFIX}/all')
    except requests.exceptions.RequestException as e:
      logging.error(f'failed to get all info, {e}')
    self.people = json.loads(response.text)
    logging.info(f'all people: {self.people}')
    return self.people
  
  def get_details(self, who: str):
    try:
      response = requests.get(url=f'{config.OD_ENDPOINT_PREFIX}/{who}')
    except requests.exceptions.RequestException as e:
      logging.error(f'failed to get {who}\'s info, {e}')
    details = sorted(json.loads(response.text).items(), key=lambda x: x[0])
    self.details.append(details)
    logging.info(f'{who}\'s details: {details}')
    return details

def main(args):
    client = ODClient()
    people = client.get_people()
    for person in people:
        logging.info(f"requesting details of {person}")
        client.get_details(person)
    all_details = client.details
    logging.info(f"writing csv to {args.csv}")
    # Convert list of tuples to a dictionary
    dict_rows = [dict(row) for row in all_details]
    df = pd.DataFrame(dict_rows)
    logging.info(f'df of all details:\n{df}')
    try:
        df.to_csv(args.csv)
    except IOError as e:
        logging.error(f"failed to write {args.csv}, {e}")


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('--csv', default='people.csv', type=str)
  args = parser.parse_args()
  main(args)
