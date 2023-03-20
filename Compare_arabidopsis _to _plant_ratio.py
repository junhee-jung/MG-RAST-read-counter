# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:48:41 2023

@author: bbmju01
"""
#this script is similar to other script that uses simple loop to request api-ui.mg-rast.org for information
#requires that you have list of file and their MG-rast ID
#multithreading via multiprocessing import Pool did not work so well therefore from concurrent import futures is used not sure how exactly it works but it is faster
#the idea of this script is one can compare how much of the read belong to Arabidopsis compared to other plants (i.e. Streptophyta) 
#N.B. Arabidopsis is already prefiltered on the settings
#Script requests an html page which obtain is converted to JSON file which is converted to some sort of dataframe? and loop is used to obtain the species / whatever we wanted to obtain
#no output file using ">" is enough


from concurrent import futures
#import pandas as pd
cwd=open("File containing list of mg-rast ID","r").readlines()
def aphid_annot(i):
    from urllib.request import urlopen
    #import pandas as pd
    #import gc
    import json
    if "MG" in i:
        pass
    else:
        j=i.split("\t")[0]
        k=i.split("\t")[1]
        #print (j,k)
        url="https://api-ui.mg-rast.org/metagenome/"+j+"?verbosity=stats&detail=taxonomy&auth=YourTokenhere"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        data  = json.loads(html)
        genus_list=data['genus']
        #family_list=data['family']
        #domain_list=data['domain']
        Phylum_list=data['phylum']
        plant=0
        arabi=0
        for l in Phylum_list:
            if "Streptophyta" in l:
                plant=l[1]
        for m in genus_list:
            if "Arabidopsis" in m:
                arabi=m[1]
        print (k, str(plant), str(arabi), str(int(arabi)/int(plant)).rstrip())


    
if __name__ == '__main__':
    with futures.ThreadPoolExecutor(4) as executor:
        executor.map(aphid_annot, cwd)