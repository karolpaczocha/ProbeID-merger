#code by Karol Paczocha
#read the text file attached on how to use
##getting dependencies if using anaconda enviroment 'glob' might still need to be installed
import os
import pandas as pd
import glob

##read all the files in the current working directory's folder files (look for file location to change folder name)
def readAllFiles(files): 
    for file in files:
        df = pd.read_csv(file, index_col=None, header=0)#read with no index column for usability
        allDfs.append(df)# store add dataframes as a list

cwd = os.getcwd()#getting the current working directory
filelocation = cwd + r"/files" #keep folder name as a raw string change to folder name in the same format '/folder_name'

allDfs = [] #initiating list to store all dataframes
allFiles = glob.glob(os.path.join(filelocation , "*.csv")) # glob gathering all the files in the selected path that end with csv, to use other formats please change the extension


readAllFiles(allFiles) #run the function to read all the files in the path


df3 = pd.concat(allDfs, sort = False) #combinging all dataframes as one 
df4 = df3.sort_values(by=['gid']) #sorting values by probeID to perform a clean up

df5 = df4.groupby('gid').ffill() #grouping the probe IDs togetehr to retrive more usable data
df5 = df5.drop_duplicates('gid', keep='last') #dropping the bad data created during the forward fill and keeping only the good data

df5.to_csv('masterfile.csv', index= False) #save to file


