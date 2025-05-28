# First, let's import necessary libraries
import pandas as pd
import plotly.express as px

# Read the .csv file and store it as a pandas DataFrame
df_tourism = pd.read_csv("datasets/international_tourism.csv")

# Display the data to understand its structure
df_tourism.head()


# Type your answer here

# Filter the data to include only the specified countries
df_tourism_filtered = df_tourism[df_tourism['Country Name'].isin(['Greece', 'Spain', 'France', 'Italy'])]

# Sorting the data in descending order by the number of tourists in 2020
df_tourism_filtered = df_tourism_filtered.sort_values('2020', ascending=False)

# Create the bar chart using Plotly Express
fig = px.bar(
    df_tourism_filtered,
    x='Country Name',
    y='2020',  # Directly use the '2020' column for tourist numbers
    title='Tourist Arrivals in 2020',
    labels={'Country Name': 'Country', '2020': 'Number of Tourists'},
    text='2020'  # Display the tourist number on each bar
)

# Adjust bar width appearance
fig.update_traces(width=0.3)

# Display the figure
fig.show()