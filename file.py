# ==============================================
# Assignment: Data Loading, Analysis & Visualization
# Using Pandas, Matplotlib, and Seaborn
# ==============================================

# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # DataFrame with features + target
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Explore structure
print("\nData Info:")
print(df.info())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean dataset (not really needed here, Iris has no missing values)
df = df.dropna()

# ==============================================
# Task 2: Basic Data Analysis
# ==============================================

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Grouping by species and computing mean
species_means = df.groupby("species").mean(numeric_only=True)
print("\nMean values per species:")
print(species_means)

# Observations (example)
print("\nObservations:")
print("- Iris-setosa generally has smaller petal length/width compared to others.")
print("- Iris-virginica tends to have the largest measurements.")
print("- Iris-versicolor falls in between.")

# ==============================================
# Task 3: Data Visualization
# ==============================================

# Set Seaborn style
sns.set(style="whitegrid")

# 1. Line Chart (trend of sepal length across samples)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
