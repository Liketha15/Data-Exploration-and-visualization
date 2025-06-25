import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset: replace or load your own data
data = {
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen'],
    'department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'work_hours': [40, 45, 38, 42, 50, 47, 44, 39]
}

df = pd.DataFrame(data)

# Group by department to calculate total and average hours
summary = df.groupby('department')['work_hours'].agg(['sum', 'mean']).reset_index()
summary.columns = ['Department', 'Total_Hours', 'Average_Hours']

print("Summary Report:")
print(summary)

# Identify department with highest average working hours
max_avg_dept = summary.loc[summary['Average_Hours'].idxmax(), 'Department']
max_avg_hours = summary['Average_Hours'].max()

print(f"\nDepartment with highest average working hours: {max_avg_dept} ({max_avg_hours:.2f} hours)")

# Plotting

sns.set(style='whitegrid')

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Total hours bar plot with hue and legend disabled
sns.barplot(x='Department', y='Total_Hours', data=summary, ax=axes[0], 
            palette='Blues_d', hue='Department', legend=False)
axes[0].set_title('Total Work Hours by Department')
axes[0].set_ylabel('Total Hours')
axes[0].set_xlabel('Department')

# Average hours bar plot with hue and legend disabled
sns.barplot(x='Department', y='Average_Hours', data=summary, ax=axes[1], 
            palette='Greens_d', hue='Department', legend=False)
axes[1].set_title('Average Work Hours by Department')
axes[1].set_ylabel('Average Hours')
axes[1].set_xlabel('Department')

# Highlight the max average bar
for bar, dept in zip(axes[1].patches, summary['Department']):
    if dept == max_avg_dept:
        bar.set_edgecolor('red')
        bar.set_linewidth(3)

plt.tight_layout()
plt.show()
