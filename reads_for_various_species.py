# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:39:28 2021

@author: Junhee
"""
from urllib.request import urlopen
import json
#web parsing for the MG-RAST data bring out genus level
#uses metadata from the website
A=open("File containing list of mg-rast ID","r").readlines()#metadata
A.pop(0)
print ("ID, NAME, seqc, total, unknownp, unknown, knwonr, knownp, unknown, failedq, bact , euk, vir, arch, homo, bra, aphid, buch")

for i in A:

    """
    #values here needs to be changed - it works for my file with mg-rast ID and name list
    #split by either space OR tab - i.split("seperator here")
    ID=i.split()[0]
    NAME=i.split()[1]
    seqc=i.split()[3]
    """
    url="https://api-ui.mg-rast.org/metagenome/"+ID+"?verbosity=stats&detail=taxonomy&auth=YourTokenhere"
    #print (url)
    qc="https://api-ui.mg-rast.org/metagenome/"+ID+"?verbosity=stats&detail=sequence_breakdown&auth=YourTokenhere"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    page_q = urlopen(qc)
    html_bytes_q = page_q.read()
    html_q = html_bytes_q.decode("utf-8")
    total=unknownp=unknown=knwonr=knownp=unknown=failedq=homo=buch=aphid=bra=euk=vir=bact=arch=0
    """
    as loop continues I wanted to make sure that all the variable becomes 0
    the rest are converting web request into HTML block which is in JSON format (from mg-rast) which is converted into JSON
    """
    if "submission" in html:
        pass
    else:
        data  = json.loads(html)
        genus_list=data['genus']
        family_list=data['family']
        domain_list=data['domain']
        Phylum_list=data['phylum']
        for j in genus_list:
            if "Homo" in j:
                homo = j[1]
            if "Buchnera" in j:
                buch = j[1]
            if "Acyrthosiphon" in j:
                aphid=j[1]
        for k in family_list:
            if "Brassicaceae" in k:
                bra=k[1]
        for l in domain_list:
            if "Eukaryota" in l:
                euk=l[1]
            if "Viruses" in l:
                vir=l[1]
            if "Archaea" in l:
                arch=l[1]
            if "Bacteria" in l:
                bact=l[1]
    if "submission" in html_q:
        pass
    else:
        data_q  = json.loads(html_q)
        knwonr=data_q["known_rna"]
        unknown=data_q["unknown"]
        knownp=data_q["known_prot"]
        failedq=data_q["failed_qc"]
        unknownp=data_q["unknown_prot"]
        total=data_q["total"]
    print (ID, NAME,  seqc,total,unknownp,unknown,knwonr,knownp,unknown,failedq,bact,euk, vir, arch, homo,bra, aphid, buch)
    
    
