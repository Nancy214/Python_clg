import csv
from matplotlib import pyplot as plt

plt.style.use('seaborn')

numbers = [5706,724,4253]
labels = ['Active','Deceased','Recovered']
explode = [0.1,0.1,0.1]

plt.pie(numbers,labels=labels,explode=explode,shadow=True,autopct='%1.1f%%',wedgeprops={'edgecolor':'red'})

plt.title('COVID-19 cases in Gujarat')
plt.tight_layout()

plt.show()
