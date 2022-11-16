import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')

print(df.head(5))

#exploring to see if anything is correlated
sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

#1 Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value

#2 Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value

#3 create a bar chart for the success rate of each orbit
# HINT use groupby method on Orbit column and get the mean of Class column

#4 Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value

#5 Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value

#6 visualize the launch success yearly trend
#A function to Extract years from the date 
year=[]
def Extract_year(date):
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year

#Plot a line chart with x axis to be the extracted year and y axis to be the success rate

#----------
#by now yoyu should obtain some preliminary insights about how each important ariable would affect the success rate,
#we will select the features that will be used in the success prediction in the future module
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

#7 Use the function get_dummies and features dataframe to apply OneHotEncoder to the column Orbits, LaunchSite, 
# LandingPad, and Serial. Assign the value to the variable features_one_hot, display the results using the method
#head. Your result dataframe must include all features including the encoded ones. 
# HINT: Use get_dummies() function on the categorical columns

#8 Cast all numeric columns to float64
# HINT: use astype function

features_one_hot.to_csv('C:\\users\peters\Downloads\dataset_part_3.csv', index=False)


