import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data.csv')
df = df[df['FactValueNumeric'].notna()]
countries = sorted(df['Location'].dropna().str.strip().unique())

print("=" * 50)
print("WHO Air Quality Data Analysis & Prediction")
print("=" * 50)
print("Source","https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022")
print("=" * 50)
print(f"\nTotal countries available: {len(countries)}")

country_name = input("Enter country name: ").strip()
country_data = df[df['Location'] == country_name].copy()

if country_data.empty:
    print(f"\nNo data found for '{country_name}'")
    print("\nSuggestions:")
    suggestions = [c for c in countries if country_name.lower() in c.lower()]
    for suggestion in suggestions[:10]:
        print(f"  - {suggestion}")
else:
    country_data = country_data.sort_values('Period')
    years = country_data['Period'].values
    pm25_values = country_data['FactValueNumeric'].values
    n = len(years)
    sum_x = np.sum(years)
    sum_y = np.sum(pm25_values)
    sum_xy = np.sum(years * pm25_values)
    sum_x2 = np.sum(years ** 2)
    gradient = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    intercept = (sum_y - gradient * sum_x) / n
    last_year = years[-1]
    future_years = np.array([last_year + 1, last_year + 2, last_year + 3])
    predictions = gradient * future_years + intercept
    predictions = np.maximum(predictions, 0)
    print(f"\n{country_name} - PM2.5 Statistics")
    print("-" * 50)
    print(f"Data available: {years[0]} - {years[-1]}")
    print(f"Number of data points: {len(country_data)}")
    print(f"Latest PM2.5 level: {pm25_values[-1]:.2f} μg/m³")
    print(f"Average PM2.5 level: {pm25_values.mean():.2f} μg/m³")
    first_value = pm25_values[0]
    last_value = pm25_values[-1]
    change = ((last_value - first_value) / first_value) * 100
    trend = "Improving" if change < 0 else "Worsening"
    print(f"Overall trend: {trend} ({change:+.1f}%)")
    print(f"Gradient: {gradient:.2f} μg/m³ per year")
    print(f"\nPredicted PM2.5 levels for next 3 years:")
    print("-" * 50)
    for i, year in enumerate(future_years):
        print(f"Year {int(year)}: {predictions[i]:.2f} μg/m³")
    plt.figure(figsize=(10, 6))
    plt.plot(years, pm25_values, 'o-', label='Historical Data', linewidth=2, markersize=8)
    plt.plot(future_years, predictions, 'o--', label='Predictions', linewidth=2, markersize=8)
    plt.axvline(x=last_year + 0.5, color='gray', linestyle=':', linewidth=1)
    plt.xlabel('Year')
    plt.ylabel('PM2.5 (μg/m³)')
    plt.title(f'{country_name} - PM2.5 Levels')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nGraph displayed successfully!")
