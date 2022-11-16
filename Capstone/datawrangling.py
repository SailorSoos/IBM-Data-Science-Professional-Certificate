import pandas as pd
import numpy as np

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")

#number of missing values
print(df.isnull().sum()/df.count()*100)

#dtypes
print(df.dtypes)

#TODO 1
# Apply value_counts() on column LaunchSite
print(df["LaunchSite"].value_counts())

#TODO 2
# Apply value_counts on Orbit column
print(df["Orbit"].value_counts("Orbit"))

#TODO 3
# landing_outcomes = values on Outcome column
landing_outcomes = df["Outcome"].value_counts()
print(landing_outcomes)

for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)

bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
print(bad_outcomes)

#TODO 4
# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise
landing_class = []
for key,value in df["Outcome"].items():
     if value in bad_outcomes:
        landing_class.append(0)
     else:
        landing_class.append(1) 

df['Class']= landing_class
print(df[['Class']].head(8))

print(df.head(5))

print(df["Class"].mean())

#df.to_csv("C:\\pathway_to_the_folder\dataset_part_2.csv", index=False)






