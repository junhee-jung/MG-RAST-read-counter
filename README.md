# MG RAST read counter

The aim of these scripts is to pull the variable that one wants to obtain using [MG-rast](https://www.mg-rast.org/) API. <br/>
By default the output from [MG-rast](https://www.mg-rast.org/) API is JSON. The script relies on a "for loop" to find relavant information <br/>

Most of the files follow very similar patterns important things to adjust to ones needs are:

- &auth=YourTokenhere - you need to add your own mg-rast webkey which is found My Profile (button on mg rast webpage "human icon") -> press "show webkey"

- The script relies on there being a file with list of MG-rast ID (34 character file) and name etc which can be found My studies (DNA icon) -> "export table data as CSV" although the output is ".CSV file", in reality it is more of TSV (tab sperated) file which python script treats as TSV.

there are 3 scripts:

1) [Compare_arabidopsis_to_plant_ratio.py](https://github.com/junhee-jung/MG-RAST-read-counter/blob/main/Compare_arabidopsis_to_plant_ratio.py) -> we wanted to know how much of the plants were "Arabidopsis" in our case Arabidopsis ≈ Thlaspi for some reason MG-RAST does not provide Kingdom level taxanomy under this API so we are are left to be satisfied with only "Streptophyta" at phylum level so in theory SOME plants may have been omitted
  
2) [obtaining_QC_Stat.py](https://github.com/junhee-jung/MG-RAST-read-counter/blob/main/obtaining_QC_Stat.py) -> we wanted to get what the ratio between acceptable read vs rejected reads were. As out reads were based on " Trash" sequence. We were unsure in the beginning how many reads were rejected due to poor quality or being "exogenous". reads for various species.py also provide same function. 

3) reads for various species.py -> the script works but is very messy. If one wants to convert this into their own script simply find which taxonomic rank and change value in "if". (e.g. if "Homo" in j: which look for human read can change into "gallus" if you want to find chicken reads etc.)


