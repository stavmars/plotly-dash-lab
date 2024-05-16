### Exercise 1 Solution

import plotly.express as px
import pandas as pd

# Although not necessary, we can convert 'Date' to datetime
df_stock['Date'] = pd.to_datetime(df_stock['Date'])

df_filtered = df_stock[df_stock['Date'].dt.year >= 2015]

# Create the line plot
fig = px.line(
    df_filtered,
    x='Date',
    y='Close',
    title='Daily Close Prices since 2015',
    labels={'Close': 'Close Price'}  # Custom labels for the y-axis
)

# Display the figure
fig.show()
