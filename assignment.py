print(df.describe())

# Group by a categorical column (e.g., 'species' in the Iris dataset)
grouped_data = df.groupby("species")["petal_length"].mean()
print(grouped_data)

import matplotlib.pyplot as plt

# Example: Time-series data of sales
plt.plot(df["date"], df["sales"], marker="o", linestyle="-")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.show()

#Bar Chart (Comparison Across Categories)
import seaborn as sns

sns.barplot(x="species", y="petal_length", data=df)
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.title("Comparison of Petal Length Across Species")
plt.show()

#Histogram (Distribution of Values)
plt.hist(df["sepal_length"], bins=20, color="blue", edgecolor="black")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()

#Scatter Plot (Relationship Between Two Variables)
plt.scatter(df["sepal_length"], df["petal_length"], color="green")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal vs Petal Length Relationship")
plt.show()

#Error Handling
try:
    df = pd.read_csv("your_dataset.csv")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
