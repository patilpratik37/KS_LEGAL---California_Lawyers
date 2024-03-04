import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("G:/Pratik Profile PC/Download/California Lawyers/lawyers_california.csv")

# Display the rows of the dataset
df

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Data cleaning: Handling missing values
# Fill missing values in 'address' column with a placeholder (e.g., "Unknown")
df['address'].fillna("Unknown", inplace=True)

# Fill missing values in 'infoSnippet' column with a placeholder (e.g., "No information available")
df['infoSnippet'].fillna("No information available", inplace=True)

# Since 'phone', 'name', and 'url' have only a few missing values, we might drop those rows.
df.dropna(subset=['phone', 'name', 'url'], inplace=True)

# For 'rating' column, you might use a specific value to indicate missing ratings (e.g., -1)
df['rating'].fillna(+1, inplace=True)

# For 'reviewSnippet' column, fill missing values with "No review available"
df['reviewSnippet'].fillna("No review available", inplace=True)

# Fill missing values in 'website' column with a placeholder (e.g., "No website available")
df['website'].fillna("No website available", inplace=True)

# Verify if missing values are handled
print("\nMissing values after handling:")
print(df.isnull().sum())

# Generate descriptive statistics for numerical columns
numerical_stats = df['rating'].describe()
print("\nDescriptive statistics for ratings:")
print(numerical_stats)

df

####
# Drop irrelevant columns if they exist in the DataFrame
columns_to_drop = ['address', 'infoSnippet', 'reviewSnippet', 'phone', 'url', 'website']
columns_to_drop = [col for col in columns_to_drop if col in df.columns]  # Filter out columns that do not exist

# Drop the columns if they exist
if columns_to_drop:
    df.drop(columns_to_drop, axis=1, inplace=True)
    print("Columns dropped:", columns_to_drop)
else:
    print("Specified columns do not exist in the DataFrame.")

# Display the first few rows of the updated DataFrame
print("\nUpdated data after dropping irrelevant columns:")
print(df.head())
####
df
####

# Visualization based on Rating

# Histogram of ratings
plt.figure(figsize=(8, 6))
sns.histplot(df['rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

####
# Check for repeated data in the "names" column
name_counts = df['name'].value_counts()
repeated_names = name_counts[name_counts > 1]

if repeated_names.empty:
    print("No repeated data found in the 'names' column.")
else:
    print("Repeated data found in the 'names' column:")
    print(repeated_names)
####
# Filter the DataFrame to include only entries with repeated names
repeated_names_df = df[df['name'].isin(repeated_names.index[:5])]

# Plot the first 5 repeated names
plt.figure(figsize=(10, 6))
sns.countplot(x='name', data=repeated_names_df, order=repeated_names_df['name'].value_counts().index)
plt.title('First 5 Repeated Names')
plt.xlabel('Name')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
####
# Aggregate data to find the maximum rating for each name
max_ratings = df.groupby('name')['rating'].max()

# Filter names with maximum rating more than once
best_rated_names = max_ratings[max_ratings.duplicated(keep=False)]

# Filter the DataFrame to include only entries with names that are in best_rated_names
best_rated_df = df[df['name'].isin(best_rated_names.index)]

# Plot the best rated names with horizontal bar plot
plt.figure(figsize=(10, 8))
sns.countplot(y='name', data=best_rated_df, order=best_rated_df['name'].value_counts().index)
plt.title('Names with Best Rating Multiple Times')
plt.xlabel('Count')
plt.ylabel('Name')
plt.show()

####
# Sort the DataFrame by rating in descending order
df_sorted = df.sort_values(by='rating', ascending=False)

# Display the top 5 rows of the sorted DataFrame
top_5_ratings = df_sorted.head(5)
print("Top 5 Ratings:")
print(top_5_ratings)

####
# Sort the DataFrame by rating in descending order
df_sorted = df.sort_values(by='rating', ascending=False)

# Extract top 5 ratings and their corresponding names
top_5_ratings = df_sorted.head(5)
top_5_names = top_5_ratings['name']
top_5_values = top_5_ratings['rating']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_5_values, labels=top_5_names, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Ratings Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
####