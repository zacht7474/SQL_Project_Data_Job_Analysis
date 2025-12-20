import matplotlib.pyplot as plt

# Data
jobs = [
    "Data Analyst", "Director of Analytics", "Associate Director- Data Insights",
    "Data Analyst, Marketing", "Data Analyst (Hybrid/Remote)", "Principal Data Analyst (Remote)",
    "Director, Data Analyst - HYBRID", "Principal Data Analyst, AV Performance Analysis",
    "Principal Data Analyst", "ERM Data Analyst"
]

salaries = [
    650000.0, 336500.0, 255829.5, 232423.0, 217000.0,
    205000.0, 189309.0, 189000.0, 186000.0, 184000.0
]

# Create horizontal bar chart
plt.figure(figsize=(12,8))
bars = plt.barh(jobs, salaries, color='skyblue')

# Add labels on the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5000, bar.get_y() + bar.get_height()/2, f"${int(width):,}", va='center')

plt.title("Average Yearly Salary by Job Title")
plt.xlabel("Salary (USD)")
plt.ylabel("Job Title")
plt.gca().invert_yaxis()  # highest salary on top
plt.tight_layout()
plt.show()
