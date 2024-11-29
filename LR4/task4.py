import pandas as pd

# Загрузка данных из файлов
flights_data = pd.read_csv('2008_rand.csv')
airports_data = pd.read_csv('airports.csv')

# 1. Среднее, минимальное и максимальное время полёта
mean_flight_time = flights_data['AirTime'].mean()
min_flight_time = flights_data['AirTime'].min()
max_flight_time = flights_data['AirTime'].max()

print(f"Среднее время полета: {mean_flight_time}")
print(f"Минимальное время полета: {min_flight_time}")
print(f"Максимальное время полета: {max_flight_time}")

# 2. Анализ минимального времени полёта
suspicious_flights = flights_data[flights_data['AirTime'] == min_flight_time]
print("Рейсы с минимальным временем полета:")
print(suspicious_flights)

# 2. Время полета этих же рейсов в другие дни
same_flights = flights_data.merge(suspicious_flights[['FlightNum', 'Origin', 'Dest']], on=['FlightNum', 'Origin', 'Dest'])
same_flights = same_flights[same_flights['AirTime'] != min_flight_time]
print("Время полета тех же рейсов в другие дни:")
print(same_flights[['FlightNum', 'AirTime']])

# 3. Аэропорт с наибольшим количеством полетов
most_flights_airport = flights_data['Dest'].value_counts().idxmax()
most_flights_airport_name = airports_data[airports_data['iata'] == most_flights_airport]['airport'].values[0]
print(f"Аэропорт с наибольшим количеством полетов: {most_flights_airport_name}")

# 4. Три наиболее популярных места назначения в июне
june_flights = flights_data[flights_data['Month'] == 6]
top_3_destinations = june_flights['Dest'].value_counts().head(3)
destinations_info = airports_data[airports_data['iata'].isin(top_3_destinations.index)]

# Используем apply для вывода популярных мест без цикла for
print(destinations_info.apply(lambda row: f"Популярное место назначения: {row['iata']}, город: {row['city']}", axis=1).tolist())

# 5. Аэропорт с наибольшей задержкой при посадке по причине погоды
max_weather_delay = flights_data['WeatherDelay'].max()
max_weather_delay_flight = flights_data[flights_data['WeatherDelay'] == max_weather_delay].iloc[0]
delay_airport = max_weather_delay_flight['Dest']
delay_airport_name = airports_data[airports_data['iata'] == delay_airport]['airport'].values[0]
print(f"Аэропорт с наибольшей задержкой по погоде: {delay_airport_name}, задержка: {max_weather_delay} минут, дата: {max_weather_delay_flight['Month']}/{max_weather_delay_flight['DayofMonth']}/2008")
