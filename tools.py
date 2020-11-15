#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:52:18 2020

@author: louisbard
"""
import numpy as np
import sys
import re



# mon_fichier = open("randomA100.tsp","r")
# contenu = mon_fichier.read()
# print(contenu)
# mon_fichier.close()

# prog = re.compile("\d")
# with open("randomA100.tsp", "r") as file:
#     cities = []
#     rows = file.read().splitlines()
#     for i, row in enumerate(rows):
#        if prog.match(row):
#            cities.append(np.fromstring(" ".join(row.split(" ")[1:]), dtype=np.int32, sep=" "))
# print(np.asarray(cities))


def readtsp(filename):
	"""
	reads a tsp file and extracts
	"""
	#prog = re.compile("\d")
	with open(filename, "r") as file:
		cities = []
		rows = file.read().splitlines()
		for i, row in enumerate(rows):
			#if prog.match(row):
			cities.append(np.fromstring(" ".join(row.split(" ")[1:]), dtype=np.int32, sep=" "))
	return np.asarray(cities)
