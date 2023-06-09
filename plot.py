import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

### Create Data
data = {'Age': [25,30,40], 'YoEx': [3,6,15]}
print("Foretelling")

### Assign data to x & y
x = data['Age']
y = data['YoEx']

### Matplotlib.pyplot
# plt.scatter(x,y)
# plt.show()

### Seaborn
df = pd.DataFrame(data)

# # Plot against axes
# sns.scatterplot(x='Age', y='YoEx', data=df)
# plt.show()

# # Plot relationship
# sns.scatterplot(df)
# plt.show()

### Pandas
df.plot(x='Age', y='YoEx', kind='scatter')
plt.show()

#commit