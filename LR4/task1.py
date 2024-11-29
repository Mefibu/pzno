import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла
vaccination_data = pd.read_excel('vaccination_process_2021_regions.xlsx')

# Фильтрация данных для вакцины AstraZeneca в Одесской области
vaccination_data['Month'] = pd.to_datetime(vaccination_data['Дата (період) данних'], dayfirst=True).dt.month
odessa_data_astra = vaccination_data[(vaccination_data['Назва території'] == 'Одеська область') & (vaccination_data['AstraZeneca, осіб'] > 0)].copy()

# Суммирование вакцинированных по месяцам
monthly_vaccinated_astra = odessa_data_astra.groupby('Month')['AstraZeneca, осіб'].sum()

# Построение столбиковой диаграммы
plt.figure(figsize=(10, 6))
monthly_vaccinated_astra.plot(kind='bar')
plt.xlabel('Месяц')
plt.ylabel('Количество вакцинированных')
plt.title('Количество людей, вакцинированных вакциной AstraZeneca в Одесской области по месяцам')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
