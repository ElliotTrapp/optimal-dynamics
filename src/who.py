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
import logging
import json
import requests
from pathlib import Path
from argparse import ArgumentParser
from src.config import config

