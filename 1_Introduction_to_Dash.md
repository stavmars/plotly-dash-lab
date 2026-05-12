# Introduction to Dash
Dash is an open-source Python framework developed by Plotly for creating interactive, web-based analytics applications. It is specifically designed to streamline the process of building reactive data visualization interfaces. This makes Dash an ideal choice for data scientists and analysts looking to deploy their data analysis on the web without requiring in-depth knowledge of web development technologies. By abstracting away the complexities of the underlying web tech stack, Dash enables users to focus on creating functional and visually appealing web applications that are responsive and interactive.

For detailed documentation and more information, visit [Dash by Plotly](https://dash.plotly.com/).

### Core Features of Dash:
- **Web Server Architecture**: Dash applications are essentially web servers running Flask, communicating data in JSON format over HTTP requests.
- **React.js Frontend**: The frontend of Dash applications renders using React.js, ensuring a smooth interactive user experience.
- **Declarative and Reactive Programming**: Dash enables a declarative approach to define user interfaces, making it reactive and intuitive to link the UI with the Python code backend.
- **Mobile and Cross-Platform Compatibility**: Applications built with Dash are inherently mobile-ready and compatible across different platforms.

>### Dataset for this Lab
>
>In this lab, we will use Dash to create a dashboard that visualizes and enables interactive exploration of TripAdvisor data on Greek restaurants. This subset is part of a larger dataset covering European restaurants with details like location, average rating, review counts, and cuisine types. For additional information, visit the [TripAdvisor European Restaurants dataset on Kaggle](https://www.kaggle.com/datasets/stefanoleone992/tripadvisor-european-restaurants). Our focus will be specifically on restaurants in Greece.

# Working with Dash Apps

In the previous part of the lab, we used Jupyter Notebook for quick data exploration and Plotly visualizations.

For Dash, we will work with regular Python files. A Dash app runs locally as a small web application and is viewed through the browser.

You may use any code editor or IDE you prefer, such as Visual Studio Code, PyCharm, Spyder, or a simple text editor together with a terminal.

Before continuing, make sure you have already completed the setup steps from the main README, including the installation of the required Python packages.

### Verifying the Setup

To ensure that everything is correctly set up, let's test by running a basic Dash app. First, create a file named `hello_dash.py` and input the following code:

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.Div("Your first Dash app.")
])

if __name__ == '__main__':
    app.run(debug=True)

```

To run the app, open a terminal and execute the command:

```bash
python hello_dash.py
```

The `debug=True` option in the `run()` method enables the app to run in debug mode. This mode provides useful features such as hot reloading (the app automatically reloads when you make changes to the code) and enhanced error logging.

Visit [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your web browser to see your Dash app running. If everything is set up correctly, you should see the greeting "Hello Dash!" displayed on the page.



<br>

**[← Previous](README.md) | [Next →](2_Dash_Components.md)**
---
