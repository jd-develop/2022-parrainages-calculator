#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pprint
import urllib.request

url_of_parrainages = "https://presidentielle2022.conseil-constitutionnel.fr/telechargement/parrainagestotal.json"


with urllib.request.urlopen(url_of_parrainages) as response:
    file_dict = json.load(response)

candidates = {}
for parrain in file_dict:
    candidate = parrain['Candidat']
    try:
        candidates[candidate] += 1
    except KeyError:
        candidates[candidate] = 1

pprint.pprint(candidates)
