import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data generation (replace with your real dataset)
data = {
    'city': ['CityA']*12 + ['CityB']*12 + ['CityC']*12,
    'date': pd.date_range('2024-01-01', periods=12, freq='W').tolist() * 3,
    'temperature': np.random.randint(10, 35, size=36)
}

df = pd.DataFrame(data)

# Extract month number from the date
df['month'] = df['date'].dt.month

# Group by city and month and sum temperatures
monthly_sum = df.groupby(['city', 'month'])['temperature'].sum().reset_index()

# Pivot to get month-wise summary table
pivot_table = monthly_sum.pivot(index='city', columns='month', values='temperature').fillna(0)
pivot_table.columns = pivot_table.columns.astype(int)

# Define summer months
summer_months = [6, 7, 8]
available_summer_months = [m for m in summer_months if m in pivot_table.columns]
pivot_table['summer_total'] = pivot_table[available_summer_months].sum(axis=1)

# Print summary table
print("Month-wise Temperature Summary Table:")
print(pivot_table)

# Identify city with highest total summer temperature
max_summer_city = pivot_table['summer_total'].idxmax()
max_summer_value = pivot_table['summer_total'].max()
print(f"\nCity with highest total temperature in summer months: {max_summer_city} ({max_summer_value})")

# --- Plotting the table as a grouped bar chart ---

sns.set(style="whitegrid")

# Prepare data for plotting (melt pivot table to long form)
plot_data = pivot_table.drop(columns='summer_total').reset_index().melt(id_vars='city', var_name='month', value_name='temperature')

plt.figure(figsize=(12, 6))
sns.barplot(data=plot_data, x='month', y='temperature', hue='city')

plt.title('Monthly Total Temperatures by City')
plt.xlabel('Month')
plt.ylabel('Total Temperature')
plt.legend(title='City')
plt.show()
