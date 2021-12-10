# -*- coding: utf-8 -*-
import json
from data import data_

def convertToJSON():
    with open(r 'Документы/Lab12/data.py', 'w') as write_file:
        json.dump(data_, write_file)
