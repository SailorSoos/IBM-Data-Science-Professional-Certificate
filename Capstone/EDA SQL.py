#connect to the sqlserver, ie create an instance of the sqldf and query the following:
import pandasql
from pandasql import sqldf
import pandas as pd
import numpy as np

df= pd.read_csv('c://Users/soosa/Downloads/ChicagoCrimeData.csv')

#1 display the names of the unique launch sites in the space mission
uniqueSites = sqldf('SELECT DISTINCT Launch_Site FROM df','Launch_Site')
print(uniqueSites)

#2 display 5 records where launch sites begin with the string 'CCA'
CCAsites = sqldf("SELECT TOP 5 * FROM df WHERE Launch_Site LIKE 'CCA%'")
print(CCAsites)

#3 display the total payload mass carried by booster launched by nasa (CRS)
totalPayloadMass = sqldf("SELECT SUM(PAYLOAD_MASS_KG_) TotalPayloadMass FROM df WHERE Customer = 'NASA (CRS)'",'TotalPayloadMass')
newdf = pd.DataFrame(totalPayloadMass)
newdf.columns = ['Total Payload Mass']
print(newdf)

#4 display average payload mass carried by booster version f9 v1.1
avPayloadMass = sqldf("SELECT AVG(PAYLOAD_MASS_KG_) AveragePayloadMass FROM df WHERE Booster_Version = 'F9 v1.1'",'AveragePayloadMass')
newdf= pd.DataFrame(avPayloadMass)
newdf.columns = ['Average Payload Mass']
print(newdf)

#5 list the date when the first successful landing outcome in ground pad was achieved
successOutcome = sqldf("SELECT MIN(Date) SLO FROM df WHERE Landing_Outcome = 'Success (drone ship)'",'SLO')
newdf= pd.DataFrame(successOutcome)
newdf.columns = ['Date which first Successful landing outcome in drone ship was acheived.']
print(newdf)

#6 list the names of the booster which have success in drone ship and have payload mass > 4000 & <6000
shipMass = sqldf("SELECT Booster_Version FROM df WHERE Landing_Outcome = 'Success (ground pad)' AND Payload_MASS_KG_ > 4000 AND Payload_MASS_KG_ < 6000",'Booster_Version')
newdf= pd.DataFrame(shipMass)
newdf.columns = ['Date which first Successful landing outcome in drone ship was acheived.']
print(newdf)

#7 list the total numer of successful and failure mission outcomes
successFail = sqldf("SELECT(SELECT Count(Mission_Outcome) FROM df WHERE Mission_Outcome LIKE '%Success%') AS Successful_Mission_Outcomes,(SELECT Count(Mission_Outcome) FROM tblSpaceX where Mission_Outcome LIKE '%Failure%') AS Failure_Mission_Outcomes")
print(successFail)

#8 list the names of the booster_versions which have carried the maximum payload mass. Use a subquery
maxmass = sqldf("SELECT DISTINCT Booster_Version, MAX(PAYLOAD_MASS_KG_) AS [Maximum Payload Mass] FROM df GROUP BY Booster_Version ORDER BY [Maximum Payload Mass] DESC")
print(maxmass)

#9 list the failed landing_outcomes in drone ship, thier booster versions, and launch site names for in year 2015
year2015 = sqldf("SELECT DateName( month , DateAdd( month , MONTH(CONVERT(date,Date, 105)) , 0 ) - 1 )  as Month, Booster_Version, Launch_Site, Landing_Outcome FROM df WHERE  (Landing_Outcome LIKE N'%Success%') AND YEAR(CONVERT(date,Date, 105)) = '2015'")
print(year2015)

#10 rank the count of landing outcomes (such as failure (drone ship) or success (ground pad)) between the date
# 2010-06-04 and 2017-03-20, in descending order
rankOutcomes = sqldf("SELECT COUNT(Landing_Outcome) AS sl FROM df WHERE (Landing_Outcome LIKE '%Success%') AND (Date >'04-06-2010') AND (Date < '20-03-2017')",'sl')
print(rankOutcomes)


