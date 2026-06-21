import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")

# Read only required columns
df = pd.read_csv(
    "US_Accidents_March23.csv",
    usecols=["State", "Weather_Condition", "Start_Time"]
)

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

# Remove missing values
df = df.dropna()

df["Start_Time"] = pd.to_datetime(
    df["Start_Time"],
    format="mixed",
    errors="coerce"
)
df = df.dropna(subset=["Start_Time"])

# Extract Hour
df["Hour"] = df["Start_Time"].dt.hour

# -----------------------------
# Accidents by Hour
# -----------------------------
plt.figure(figsize=(10,5))
sns.countplot(x="Hour", data=df)
plt.title("Accidents by Hour of Day")
plt.savefig("accidents_by_hour.png")
plt.close()

# -----------------------------
# Top 10 States
# -----------------------------
plt.figure(figsize=(10,5))
df["State"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 States with Most Accidents")
plt.ylabel("Number of Accidents")
plt.savefig("top_states.png")
plt.close()

# -----------------------------
# Weather Conditions
# -----------------------------
plt.figure(figsize=(12,6))
df["Weather_Condition"].value_counts().head(10).plot(kind="bar")
plt.title("Top Weather Conditions During Accidents")
plt.ylabel("Number of Accidents")
plt.savefig("weather_conditions.png")
plt.close()

print("\nTask 05 Completed Successfully!")