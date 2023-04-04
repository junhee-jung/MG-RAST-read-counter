# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:04:22 2023

@author: bbmju01
"""


#This script use  MG rast API to request and get the QC stats 
#using multiprocessing it uses more than 1 core which greatly increases the speed as it relies a very simple loop to get information from website api-ui.mg-rast.org
#it saves the API request result as JSON file as well as writing down "summary" in CSV file
#also the script save output as json

import pandas as pd 
import json
import os
from multiprocessing import Pool
os.chdir("File with all the list of things")

cwd=open("File with all the list of things","r").readlines()
qc_file=open("Output file.csv","a")
qc_file.write("mg_rast_ID"+","+"name"+","+'total'+","+ 'known_prot'+","+ 'known_rna'+","+ 'unknown'+","+ 'unknown_prot'+","+ 'failed_qc'+"\n")
qc_file.close()

def QC_stat(i):
    qc_file=open("Output file.csv","a")
    if "MG" in i:
        pass
    else:
        j=i.split("\t")[0]
        k=i.split("\t")[1]
        print (j,k)
        json_url="https://api-ui.mg-rast.org/metagenome/"+j+"?verbosity=stats&detail=sequence_breakdown&auth=YourTokenhere"
        #print (json_url)
        print (k+".json")
        df = pd.read_json(json_url, typ='series')
        qc_file.write(j+","+k+","+str(df["total"])+","+str(df["known_prot"])+","+str(df["known_rna"])+","+str(df["unknown"])+","+str(df["unknown_prot"])+","+str(df["failed_qc"])+"\n")
        #df.to_json(k+".json") #remove "#" if you want the file to be saved 
        qc_file.close()
if __name__ == '__main__':
    pool = Pool( #whatever number you want < your max thread)  
    pool.map(QC_stat, cwd) 








