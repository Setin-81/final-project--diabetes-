import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#دیتاست بیماران بخش داخلی

df = pd.read_excel('diabetes.xlsx')


#نمایش اطلاعات دیتافریم
print("Hospital Data:")
print(df)

# تجزیه و تحلیل داده‌ها
average_age = df['Age'].mean()
average_bp = df['Blood_Pressure'].mean()
average_chol = df['Cholesterol'].mean()
average_diab = df['Diabetes-M'].mean()


# چاپ نتایج تحلیل
print("\nAverage Age:", average_age)
print("Average Blood Pressure:", average_bp)
print("Average Cholesterol:", average_chol)
print("Average Diabetes-M:", average_diab)

# نمایش نمودار اطلاعات
plt.figure(figsize=(12, 6))

# نمودار توزیع سن بیماران
plt.subplot(1, 4, 1)
plt.hist(df['Age'], bins=6, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# نمودار فشار خون بیماران
plt.subplot(1, 4, 2)
plt.boxplot(df['Blood_Pressure'])
plt.title('Blood Pressure Distribution')
plt.ylabel('Blood Pressure')

# نمودار کلسترول بیماران
plt.subplot(1, 4, 3)
plt.boxplot(df['Cholesterol'])
plt.title('Cholesterol Distribution')
plt.ylabel('Cholesterol')

# نمودار دیابت بیماران
plt.subplot(1, 4, 4)
plt.hist(df['Diabetes-M'], bins=6, color='lightgreen', edgecolor='black')
plt.title('Diabetes Distribution')
plt.xlabel('Diabetes-M')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()