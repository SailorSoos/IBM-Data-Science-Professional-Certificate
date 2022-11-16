#connect to the sqlserver, ie create an instance of the sqldf and query the following:
import pandas as pd
import numpy as np
import pyodbc
import sqlserver as ss 

#possibly add adg to the front of sqlserver?
db = ss.sqlserver('localhost','1433','SpaceX','admin','admin')

#1 display the names of the unique launch sites in the space mission
db.GetRecordsOfColumn('select DISTINCT Launch_Site from tblSpaceX','Launch_Site')

#2 display 5 records where launch sites begin with the string 'CCA'

conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=localhost;'
                                  'Database=SpaceX;'
                                  'User ID=admin;Password=admin;')
cursor = conn.cursor()

cursor.execute("select TOP 5 * from tblSpaceX WHERE Launch_Site LIKE 'CCA%'")
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():   
     results.append(dict(zip(columns, row)))

df = pd.DataFrame.from_dict(results)
df

#3 display the total payload mass carried by booster launched by nasa
TPM = db.GetRecordsOfColumn("select SUM(PAYLOAD_MASS_KG_) TotalPayloadMass from tblSpaceX where Customer = 'NASA (CRS)'",'TotalPayloadMass')
ndf= pd.DataFrame(TPM)
ndf.columns = ['Total Payload Mass']
ndf

#4 display average payload mass carried by booster version f9 v1.1
APM = db.GetRecordsOfColumn("select AVG(PAYLOAD_MASS_KG_) AveragePayloadMass from tblSpaceX where Booster_Version = 'F9 v1.1'",'AveragePayloadMass')
ndf= pd.DataFrame(APM)
ndf.columns = ['Average Payload Mass']
ndf

#5 list the date when the first successful landing outcome in ground pad was achieved
SLO = db.GetRecordsOfColumn("select MIN(Date) SLO from tblSpaceX where Landing_Outcome = 'Success (drone ship)'",'SLO')
ndf= pd.DataFrame(SLO)
ndf.columns = ['Date which first Successful landing outcome in drone ship was acheived.']
print(ndf)

#6 list the names of the booster which have success in drone ship and have payload mass > 4000 & <6000
SLO = db.GetRecordsOfColumn("select Booster_Version from tblSpaceX where Landing_Outcome = 'Success (ground pad)' AND Payload_MASS_KG_ > 4000 AND Payload_MASS_KG_ < 6000",'Booster_Version')
ndf= pd.DataFrame(SLO)
ndf.columns = ['Date which first Successful landing outcome in drone ship was acheived.']
print(ndf)

#7 list the total numer of successful and failure mission outcomes
conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=localhost;'
                                  'Database=SpaceX;'
                                  'User ID=admin;Password=admin;')
cursor = conn.cursor()

cursor.execute("SELECT(SELECT Count(Mission_Outcome) from tblSpaceX where Mission_Outcome LIKE '%Success%') as Successful_Mission_Outcomes,(SELECT Count(Mission_Outcome) from tblSpaceX where Mission_Outcome LIKE '%Failure%') as Failure_Mission_Outcomes")
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():   
     results.append(dict(zip(columns, row)))

df = pd.DataFrame.from_dict(results)
print(df)

#8 list the names of the booster_versions which have carried the maximum payload mass. Use a subquery
conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=localhost;'
                                  'Database=SpaceX;'
                                  'User ID=admin;Password=admin;')
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT Booster_Version, MAX(PAYLOAD_MASS_KG_) AS [Maximum Payload Mass] FROM tblSpaceX GROUP BY Booster_Version ORDER BY [Maximum Payload Mass] DESC")
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():   
     results.append(dict(zip(columns, row)))

df = pd.DataFrame.from_dict(results)
print(df)

#9 list the failed landing_outcomes in drone ship, thier booster versions, and launch site names for in year 2015
conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=localhost;'
                                  'Database=SpaceX;'
                                  'User ID=admin;Password=admin;')
cursor = conn.cursor()

cursor.execute("SELECT   DateName( month , DateAdd( month , MONTH(CONVERT(date,Date, 105)) , 0 ) - 1 )  as Month, Booster_Version, Launch_Site, Landing_Outcome FROM tblSpaceX WHERE  (Landing_Outcome LIKE N'%Success%') AND YEAR(CONVERT(date,Date, 105)) = '2015'")
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():   
     results.append(dict(zip(columns, row)))

df = pd.DataFrame.from_dict(results)
print(df)

#10 rank the count of landing outcomes (such as failure (drone ship) or success (ground pad)) between the date
# 2010-06-04 and 2017-03-20, in descending order
sl = db.GetRecordsOfColumn("SELECT COUNT(Landing_Outcome) AS sl FROM dbo.tblSpaceX WHERE (Landing_Outcome LIKE '%Success%') AND (Date >'04-06-2010') AND (Date < '20-03-2017')",'sl')

ndf= pd.DataFrame(sl)
ndf.columns = ['Successful Landing Outcomes Between 2010-06-04 and 2017-03-20']
print(ndf)





