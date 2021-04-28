from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
# from IMDB import *
import random


ia=IMDb()
per=Person()

actors = ['Aamir Khan', 'Salman Khan']

#AK: 1992: 0th .... 2022: 20th
 #           2 .......    3

#1 ...5... 2




# def actorsdata(actors):
#     actors = ['Aamir Khan', 'Salman Khan']
#     for i in actors:
#         person = ia.search_person(actors[i])
#         filmography=ia.get_person(person[0].personID, info=['filmography'])
#         filmography_list=filmography['filmography']
#         data = filmography_list['actor']

#     dic = {}
#     list_ = []

#     for item in data:
#         if item.items()[1][1] == 'movie' and type(item.items()[2][1]) == int:
#             if str(item.items()[2][1]) not in dic:
#                 dic[str(item.items()[2][1])] = 1
#             else:
#                 dic[str(item.items()[2][1])] += 1
#             list_.append(item.items()[2][1])

#     for date in range(min(list_), max(list_)):
#         if str(date) not in dic:
#             dic[str(date)] = 0

#     dic_reversed = {}
#     for item in sorted(dic.keys()):
#         dic_reversed[item] = dic[item]

#     print(dic_reversed)

print(actorsdata(actors))