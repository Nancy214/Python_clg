import csv 
import numpy as np
from matplotlib import pyplot as plt 

plt.style.use('seaborn') 

districts = [] 
confirmed = [] 
active = [] 
deceased = [] 
recovered = [] 

with open('c1.csv') as f: 

    csv_reader = csv.DictReader(f) 

    for row in csv_reader: 

        districts.append(row['District']) 

        confirmed.append(float(row['Confirmed'])) 

        active.append(float(row['Active'])) 

        deceased.append(float(row['Deceased'])) 

        recovered.append(float(row['Recovered'])) 
x_index = np.arange(len(districts))
width = 0.25

plt.ylabel('Cases')
plt.xlabel('Districts')
        
plt.bar(x_index,confirmed,color='blue',width=width,label='Confirmed') 
plt.bar(x_index+width,active,color='red',width=width,label='Active') 
plt.bar(x_index+2*width,deceased,color='gray',width=width,label='Deceased') 
plt.bar(x_index+3*width,recovered,color='green',width=width,label='Recovered') 

plt.xticks(ticks=x_index,labels=districts,rotation=90,fontsize=8)
plt.legend(shadow=True, ncol=1)

plt.title('COVID-19 cases in Gujarat(District-wise)') 

plt.tight_layout() 

plt.legend() 

plt.show()
