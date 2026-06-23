import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes)

# Histogram
df.hist(figsize=(8,6))
plt.show()

# Box plot for Marks
plt.boxplot(df["Marks"])
plt.title("Box Plot of Marks")
plt.ylabel("Marks")
plt.show()

# Scatter plot
plt.scatter(df["Attendance"], df["Marks"])
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.show()

# Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

print("\nEDA Completed Successfully!")