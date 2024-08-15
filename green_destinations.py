# -*- coding: utf-8 -*-
"""Green Destinations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11K_yPxeJAxFTegJTZMvJzG7VxKhchJSz

# Import Required Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# Load the Data"""

data = pd.read_csv('greendestination.csv')

"""# Calculate the Attrition Rate"""

total_employees = len(data)
employees_left = data['Attrition'].value_counts().get('Yes', 0)
attrition_rate = (employees_left / total_employees) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")

"""# Convert Attrition to Numerical Values"""

data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})

"""# Analyze the Relationship Between Factors and Attrition"""

# Ensure that only numeric columns are considered for correlation
numeric_data = data.select_dtypes(include=['number'])

# Handle missing values by filling them with the mean of the column (optional)
numeric_data = numeric_data.fillna(numeric_data.mean())

# Correlation analysis
correlation = numeric_data.corr()
print("Correlation Matrix:")
print(correlation)

"""# Visualize the Relationships"""

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x='Attrition', y='Age', data=data)
plt.title('Attrition vs Age')

plt.subplot(1, 3, 2)
sns.boxplot(x='Attrition', y='YearsAtCompany', data=data)
plt.title('Attrition vs Years at Company')

plt.subplot(1, 3, 3)
sns.boxplot(x='Attrition', y='MonthlyIncome', data=data)
plt.title('Attrition vs Income')

plt.tight_layout()
plt.show()