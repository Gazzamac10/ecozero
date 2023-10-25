import os
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def createdict(listA, listB):
    return dict(zip(listA, listB))

def gettables(db,table):
    conn = sqlite3.connect(db)
    tablestring = basestr.replace('replace', table)
    sql_query = pd.read_sql_query(tablestring, conn)
    return sql_query

def removeoutliers(list):
    return list[list.between(list.quantile(.25), list.quantile(.75))]

def joindict(listofdicts):
    dall = {}
    for d in listofdicts:
        dall.update(d)
    return dall

def makecsv(t, name):
    return t.to_csv(os.path.join('./', str(name) + '.csv'))


basestr = ''' SELECT * FROM replace '''

def importtables(path):
    con = sqlite3.connect(path)
    mycur = con.cursor()
    mycur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    available_table = ([item[0]for item in mycur.fetchall()])

    tablenames = available_table

    table = [gettables(path,item)for item in tablenames]
    return table


"""
volumes = []
tabname = []
for i in range(len(table)):
    if 'I_VOLUME' in str(list(table[i].columns)) and 'z_NetVolume' in str(list(table[i].columns)):
        volumes.append(table[i]['z_NetVolume'])
        tabname.append(tablenames[i])
    elif 'I_VOLUME' in str(list(table[i].columns)) and 'z_NetVolume' not in str(list(table[i].columns)):
        volumes.append(table[i]['I_VOLUME'])
        tabname.append(tablenames[i])
    elif 'I_VOLUME' not in str(list(table[i].columns)) and 'z_NetVolume' in str(list(table[i].columns)):
        volumes.append(table[i]['z_NetVolume'])
        tabname.append(tablenames[i])
"""

"""
volumes = []
vtabname = []
tableincluded = []
for i in range(len(table)):
    if 'I_VOLUME' in str(list(table[i].columns)):
        volumes.append(table[i]['I_VOLUME'])
        vtabname.append(tablenames[i])
        tableincluded.append(table[i])

tabs = [pd.DataFrame(item)for item in tableincluded]
merged_df = pd.concat(tabs)
"""


"""
v = [removeoutliers(item)for item in volumes]
sumv = [item.sum() for item in v]

volumedict = createdict(vtabname,sumv)
volumeDF = pd.DataFrame([volumedict])
volumeDF.index = [arr[inde]]
volumeDF=(volumeDF.T)

#print (volumeDF)


#yu = volumeDF.plot.pie(y = arr[inde],figsize=(15, 15))
#plt.show()

UNIclass = []
UNItabname = []
for i in range(len(table)):
    if 'T_UNICLASS 2015_CODE' in str(list(table[i].columns)):
        UNIclass.append(table[i]['T_UNICLASS 2015_CODE'])
        UNItabname.append(tablenames[i])


unc = pd.DataFrame([list(item)for item in UNIclass][0])
unc = unc.fillna("Not Filled Out").T
unc.index = ['T_UNICLASS 2015_CODE']
unc = unc.T
unc = unc.groupby(['T_UNICLASS 2015_CODE'])['T_UNICLASS 2015_CODE'].count()

#unc.plot(kind='barh', figsize=(20, 12))
#plt.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = unc.keys()

#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
"""
"""
fig1, ax1 = plt.subplots(figsize=(20,12))
ax1.pie(unc, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
"""
