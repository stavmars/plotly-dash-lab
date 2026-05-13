# Dash HTML and Core Components

Dash offers two primary types of components to allow the application layout construction:

1. **HTML Components**:
   - This library provides Python classes for all HTML tags, simplifying the process of creating the application's layout with Python.
   - These components directly correspond to HTML tags, with keyword arguments for HTML attributes such as style, class, and id.
   - **Import statement:**
     ```python
     from dash import html
     ```

2. **Core Components**:
   - High-level, interactive components such as sliders, date pickers, dropdowns, and graphs.
   - **Import statement:**
     ```python
     from dash import dcc
     ```

## Hands-On Task 1: Dash Components

The first task involves creating a basic Dash application to display a bar chart visualizing the top 10 restaurants in Greece based on the total number of reviews. This will introduce you to the fundamental usage of both HTML and Dash core components.

### Objective:

Develop a dashboard with the following elements:

- **Title**: "Top 10 Restaurants in Greece" - colored blue.
- **Subtitle**: "Based on the total number of reviews" - colored dark gray.
- **Visualization**: A bar chart that displays the top 10 restaurants by total review count, with the restaurant name on the x-axis and the number of reviews on the y-axis.


### Steps to Build the Dashboard for Task 1

1. **Create a New File**
   - Create a new Python script named `dash_components.py`. This file will contain all the code for your dashboard.

2. **Import Libraries**
   - Import necessary libraries including Dash, Plotly, and Pandas to handle data manipulation and visualization:
     ```python
     # Import necessary libraries
     import pandas as pd
     import plotly.express as px
     import dash
     from dash import dcc
     from dash import html
     ```

3. **Load Data**
   - Load the dataset containing information about restaurants:
     ```python
     # Load the dataset
     df_restaurants = pd.read_csv('datasets/tripadvisor_restaurants_greece.csv')
     ```

4. **Prepare Data**
   - Extract the top 10 restaurants based on the total number of reviews:
     ```python
     # Sort the DataFrame by 'total_reviews_count' in descending order to get the top 10 restaurants
     top_restaurants = df_restaurants.sort_values(by='total_reviews_count', ascending=False).head(10)
     ```

5. **Create the Plotly Bar Chart**
   - Construct a Plotly bar chart to visualize the top 10 restaurants by total reviews:
     ```python
     # Create the bar chart with Plotly Express
     fig = px.bar(top_restaurants, x='restaurant_name', y='total_reviews_count', labels={'restaurant_name': 'Restaurant Name', 'total_reviews_count': 'Total Reviews'})
     ```

6. **Application Layout**
   - Define the layout of your dashboard using Dash's layout capabilities. This includes the main title and subtitle centered and styled:
     ```python
     # Initialize the Dash app
     app = dash.Dash(__name__)

     # Define the application HTML layout
     app.layout = html.Div(children=[
         html.H1("Top 10 Restaurants in Greece", style={'color': 'blue'}),
         html.H2("based on the total number of reviews", style={'color': 'darkgrey'}),
         dcc.Graph(figure=fig)
     ])
     ```

7. **Start the App**
   - Launch the application to enable interactive exploration on a local web server:
     ```python
     # Start the Dash server with debug mode enabled for development
     if __name__ == '__main__':
         app.run(debug=True)
     ```




### Practice Exercises

After completing the initial dashboard setup, here are some additional exercises:

1. **Adjust Title and Subtitle Styles**
   - Modify the styles of the dashboard's title and subtitle to center them within the layout. You will need to adjust the existing style dictionaries in your app layout.

2. **Add a Paragraph Element**
   - Below the subtitle, add a paragraph element to the dashboard and center-align it. Use the following text in the paragraph:
   
     `This dashboard utilizes a subset of the TripAdvisor dataset, specifically exploring restaurants in Greece. For more detailed information or to explore the complete dataset, visit the original source on Kaggle.`
   
   - Ensure that the link to Kaggle is clickable by properly using an HTML 'a' element within the paragraph text. Here is the URL for the dataset to be used as the hyperlink address:
   
     `https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants`

   - **Hint**: To insert the paragraph with a clickable link, use the `html.P` element and its `children` parameter to nest text and the `html.A` component for the hyperlink. Refer to the [documentation for the `html.P` element](https://dash.plotly.com/dash-html-components/p) for more details on syntax and usage.


For a complete solution to these exercises, visit [this link](https://github.com/stavmars/plotly-dash-lab/blob/main/scripts/dash_components_practice.py).


### Additional Notes

- **Viewing Updates**: To see changes you've made to the dashboard, simply save the file and reload the browser window where the app is running. Since the server is started with `debug=True`, it will automatically pick up changes made to the Python script.
- **Stopping the App**: If you need to stop the app, you can do so by either closing the terminal where the server is running or by pressing `CTRL+C` in the terminal. This stops the server and frees up the port it was using.


<br>

**[← Previous](1_Introduction_to_Dash.md) | [Next →](3_Dash_Callbacks.md)**
---