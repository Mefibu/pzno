# Задание 2: Добавить столбец Subsidy и отобразить информацию о квартиросъемщиках по различным критериям
import pandas as pd
import numpy as np

# Загрузка данных из файла
filter_data = pd.read_excel('filter3.xlsx')

# Проверка наличия нужных столбцов
required_columns = ['Rent', 'Debts', 'AverageIncome']
missing_columns = [col for col in required_columns if col not in filter_data.columns]
if missing_columns:
    print(f"Отсутствуют необходимые столбцы в файле filter3.xlsx: {missing_columns}")
else:
    # Преобразование столбцов 'Debts' и 'AverageIncome' в числовой тип данных для корректной работы с условиями
    filter_data['Debts'] = pd.to_numeric(filter_data['Debts'], errors='coerce').fillna(0)
    filter_data['AverageIncome'] = pd.to_numeric(filter_data['AverageIncome'], errors='coerce').fillna(0)

    # Добавление столбца Subsidy по описанным критериям
    filter_data['Subsidy'] = np.where((filter_data['Debts'] == 0) & (filter_data['AverageIncome'] < 4500), filter_data['Rent'] * 0.1, 0)

    # 1. Квартиросъемщики, получающие субсидию
    subsidy_recipients = filter_data[filter_data['Subsidy'] > 0]
    print("Получающие субсидию:")
    print(subsidy_recipients)

    # 2. Зарабатывающие меньше 4500 и имеющие задолженность по квартплате
    debt_low_income = filter_data[(filter_data['AverageIncome'] < 4500) & (filter_data['Debts'] > 0)]
    print("Зарабатывающие меньше 4500 и имеющие задолженность:")
    print(debt_low_income)

    # 3. Квартиросъемщики, чья квартплата превышает 2000
    high_rent = filter_data[filter_data['Rent'] > 2000]
    print("Квартиросъемщики с квартплатой больше 2000:")
    print(high_rent)

    # 4. Квартиросъемщики с зарплатой от 3000 до 5000
    income_range = filter_data[(filter_data['AverageIncome'] >= 3000) & (filter_data['AverageIncome'] <= 5000)]
    print("Квартиросъемщики с зарплатой от 3000 до 5000:")
    print(income_range)

    # 5. Получающие субсидию, чья квартплата превышает 1500
    subsidy_high_rent = filter_data[(filter_data['Subsidy'] > 0) & (filter_data['Rent'] > 1500)]
    print("Получающие субсидию с квартплатой более 1500:")
    print(subsidy_high_rent)

    # 6. Получающие субсидию с квартплатой свыше 1800 или имеющие зарплату менее 5000 и задолженность
    subsidy_or_debt = filter_data[((filter_data['Subsidy'] > 0) & (filter_data['Rent'] > 1800)) | 
                                  ((filter_data['AverageIncome'] < 5000) & (filter_data['Debts'] > 0))]
    print("Получающие субсидию с квартплатой более 1800 или зарплата < 5000 с задолженностью:")
    print(subsidy_or_debt)

    # 7. Задолженность по квартплате, квартплата не превышает 1600 или зарплата от 3000 до 5000 и квартплата более 1800
    debt_rent_income = filter_data[((filter_data['Debts'] > 0) & (filter_data['Rent'] <= 1600)) | 
                                   ((filter_data['AverageIncome'] >= 3000) & (filter_data['AverageIncome'] <= 5000) & (filter_data['Rent'] > 1800))]
    print("Задолженность по квартплате, квартплата <= 1600 или зарплата от 3000 до 5000 и квартплата > 1800:")
    print(debt_rent_income)