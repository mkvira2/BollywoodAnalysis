from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
 
ia=IMDb()
per=Person()
 
#This function makes a csv and also outputs some information about filmography history without gender or language
def dynasty():
    print("Enter an actor's name")
    person = ia.search_person(input())
    filmography=ia.get_person(person[0].personID, info=['filmography'])
    filmography_list=filmography['filmography']

    dic = {}
    list_ = []

    print(filmography_list)

    
    if 'actor' not in filmography_list:
        data = filmography_list['actress']
    else:
        data = filmography_list['actor']

    for item in data:
        if item.items()[1][1] == 'movie' and type(item.items()[2][1]) == int:
            if str(item.items()[2][1]) not in dic:
                dic[str(item.items()[2][1])] = 1
            else:
                dic[str(item.items()[2][1])] += 1
            list_.append(item.items()[2][1])

    for date in range(min(list_), max(list_)):
        if str(date) not in dic:
            dic[str(date)] = 0

    dic_reversed = {}
    for item in sorted(dic.keys()):
        dic_reversed[item] = dic[item]

    plt.bar(dic_reversed.keys(), dic_reversed.values(), 1, color='g')
    plt.xticks(rotation = 90)
    plt.show()

    # #dataframe
    # required_df=pd.DataFrame(d)
    # #output to csv
    # required_df.to_csv(str(person[0])+'_filmography_df.csv')
 
    # #Year he/she entered film industry
    # entry_year=min(required_df['start_year'][required_df['start_year']!='unknown'])
    # print('The entry year of ', person[0], ' is ' , entry_year)
    # #Debut Movie/non-movie
    # debut= required_df['movie/non-movie'][required_df['start_year']==entry_year]
    # print('The first appearance was in ', debut)
    # #Time in the industry
    # time_industry=max(required_df['start_year'][required_df['start_year']!='unknown'])-entry_year
    # print('The total time in the industry is ', time_industry)
    # #filmography music
    # return required_df
while True: 
    dynasty()
