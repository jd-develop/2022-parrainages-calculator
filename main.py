#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pprint

with open("parrainagestotal.json", mode="r", encoding="UTF-8") as json_file:
    file_dict = json.load(json_file)
    json_file.close()

candidates = {}
for parrain in file_dict:
    candidate = parrain['Candidat']
    try:
        candidates[candidate] += 1
    except KeyError:
        candidates[candidate] = 1

pprint.pprint(candidates)
