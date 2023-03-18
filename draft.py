# Project_2023.py
# Author: Norbert Antal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = "mock.csv"
domains = {}
with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    firstline=True
    for line in csvReader:
        if firstline:
            firstline = False
            continue
        email = line[9]
        name = line[1]
        split = email.split("@")
        domain = split[1]
        if domain not in domains:
            domains[domain]=1
        else:
            domains[domain]+=1
                   
for key, value in domains.items():
    print(key,value)
        