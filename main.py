#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import pprint
import urllib.request
from datetime import datetime

url_of_parrainages = "https://presidentielle2022.conseil-constitutionnel.fr/telechargement/parrainagestotal.json"
actual_file_name = f"json_history/{datetime.today().strftime('%Y-%m-%d')}.json"

with urllib.request.urlopen(url_of_parrainages) as response:  # response is HTTPResponse
    file_content = response.read().decode('utf-8')  # writable in a file.
    file = open(actual_file_name, "w", encoding="utf-8")
    file.write(file_content)
    file.close()
    with open(actual_file_name, "r", encoding="utf-8-sig") as file:
        response_dict = json.load(file)
        file.close()

candidates = {}
for parrain in response_dict:
    candidate = parrain['Candidat']
    try:
        candidates[candidate] += 1
    except KeyError:
        candidates[candidate] = 1

departments = {}
for parrain in response_dict:
    department = parrain['Departement']
    candidate = parrain['Candidat']
    try:
        departments[department][candidate] += 1
    except KeyError:
        try:
            departments[department][candidate] = 1
        except KeyError:
            departments[department] = {candidate: 1}

print("TODAY PARRAINAGES:")
pprint.pprint(candidates)

print("BY DEPARTMENT:")
pprint.pprint(departments)
