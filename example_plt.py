import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
labels = ['P1', 'P2', 'P3', 'P4', 'P5']

# Create a line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Line Plot')

# Add labels to each point
for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=12, ha='center', va='bottom')

# Customize the chart
plt.title('Line Plot with Labels', fontsize=16)
plt.xlabel('X-Axis', fontsize=14)
plt.ylabel('Y-Axis', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show the plot
plt.show()

