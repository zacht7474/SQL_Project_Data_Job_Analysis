import matplotlib.pyplot as plt

# Data
skills = ["SQL", "Excel", "Python", "Tableau", "Power BI"]
demand_count = [7291, 4611, 4330, 3745, 2609]

# Create horizontal bar chart
plt.figure(figsize=(10,6))
bars = plt.barh(skills, demand_count, color='skyblue')

# Add labels on the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 100, bar.get_y() + bar.get_height()/2, f"{width}", va='center')

plt.title("Job Demand by Skill")
plt.xlabel("Demand Count")
plt.ylabel("Skills")
plt.gca().invert_yaxis()  # optional: puts highest demand on top
plt.tight_layout()
plt.show()
