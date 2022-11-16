import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('c:/Users/peters/Downloads/dataset_part_2.csv')

print(df.head(5))

#exploring to see if anything is correlated
sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=16)
plt.ylabel("Pay load Mass (kg)",fontsize=16)
plt.show()

#1 Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value
sns.catplot(y="FlightNumber", x="LaunchSite", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Site",fontsize=16)
plt.ylabel("Flight Number",fontsize=16)
plt.show()

#2 Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(y="PayloadMass",x="LaunchSite",hue ="Class",data=df,aspect= 5)
plt.xlabel("Launch Site",fontsize=16)
plt.ylabel("Pay Load Mass (kg)",fontsize=16)
plt.show()

#3 create a bar chart for the success rate of each orbit
print(df.groupby(['Orbit']).mean()) 
sns.catplot(x="Orbit",y="Class", kind="bar",data=df)
plt.xlabel("Orbit",fontsize=16)
plt.ylabel("Mean",fontsize=16)
plt.show()

#4 Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(x="Orbit",y="FlightNumber",hue="Class",data = df)
plt.xlabel("Orbit",fontsize=16)
plt.ylabel("Flight Number",fontsize=16)
plt.show()

#5 Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value
sns.scatterplot(x="Orbit",y="PayloadMass",hue="Class",data = df)
plt.xlabel("Orbit",fontsize=16)
plt.ylabel("PayloadMass",fontsize=16)
plt.show()

#6 visualize the launch success yearly trend
#Plot a line chart with x axis to be the extracted year and y axis to be the success rate
year = pd.DatetimeIndex(df['Date']).year
year = np.array(list(year))
successratelist = []
successrate = 0.00
records = 1
data = 0
for x in df['Class']:
    data = x + data
    successrate = data/records
    successratelist.append(successrate)
    records= records +1
    
successratelist = np.array(successratelist)
d = {'successrate':successratelist,'year':year}
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.lineplot(data=d, x="year", y="successrate" )

plt.xlabel("Year",fontsize=20)
plt.title('Space X Rocket Success Rates')
plt.ylabel("Success Rate",fontsize=20)
plt.show()


#----------
#by now yoyu should obtain some preliminary insights about how each important ariable would affect the success rate,
#we will select the features that will be used in the success prediction in the future module
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

#7 Use the function get_dummies and features dataframe to apply OneHotEncoder to the column Orbits, LaunchSite, 
# LandingPad, and Serial. Assign the value to the variable features_one_hot, display the results using the method
#head. Your result dataframe must include all features including the encoded ones. 
features_hot = df[['Orbit','LaunchSite','LandingPad','Serial']]
features_hot['Orbit'] = pd.get_dummies(df['Orbit'])
features_hot['LaunchSite'] = pd.get_dummies(df['LaunchSite'])
features_hot['LandingPad'] = pd.get_dummies(df['LandingPad'])
features_hot['Serial'] = pd.get_dummies(df['Serial'])
features_hot.head()

#8 Cast all numeric columns to float64
features_hot.astype('float64')
features_hot.to_csv('dataset_part_3.csv',index=False)



