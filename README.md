# MG RAST read counter

The aim of these script is to pull the variable that one want to obtain using MG-rast API
By default the output from MG-RAST API is JSON which due to my limited knowledge rely on a "for loop" to obtain relavant information

Most of the file follow very similar patterns important things to adjust to ones needs are:

- &auth=YourTokenhere - you need to add your own mg-rast webkey which is found My Profile (button on mg rast webpage "human icon") -> press "show webkey"

- The script relies on there being a file with list of MG-rast ID and name etc which can be found My studies (DNA icon) -> "export table data as CSV" although the output is CSV file, in reality it is more of TSV (tab sperated) file which python scirpt treat it as.
