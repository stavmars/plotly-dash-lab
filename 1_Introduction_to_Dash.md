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

# Setting Up Your Development Environment

For developing Dash applications, while Jupyter notebooks can be used for quick prototyping, we will switch to using Visual Studio Code (VSCode) in this part of the lab. Unlike Jupyter, VSCode is an Integrated Development Environment (IDE) that is better suited for handling more complex development scenarios that may involve managing multiple files, operating web servers, and debugging—tasks that are more difficult in Jupyter. This makes VSCode the preferred environment for developing Dash applications in a real-world setting.


### Installing Visual Studio Code

To get started with VSCode, follow these steps:

1. **Download VSCode**: Visit the [official Visual Studio Code website](https://code.visualstudio.com/download) and download the version compatible with your operating system.
2. **Install VSCode**: Run the installer and follow the on-screen instructions to install Visual Studio Code on your computer.

### Setting Up Python and Dash in VSCode

To run Dash applications in VSCode, you first need to set up your environment:

1. **Install Python**: Download and install Python from the [official Python website](https://www.python.org/downloads/). Make sure to check 'Add Python to PATH' during installation.
2. **Open VSCode**: Start Visual Studio Code on your computer.
3. **Install the Python Extension for VSCode**: From the Extensions view (`Ctrl+Shift+X`), search for and install the 'Python' extension provided by Microsoft.
4. **Set Up a Python Interpreter**: Access the Command Palette with `Ctrl+Shift+P`, type 'Python: Select Interpreter', and choose your Python interpreter.
5. **Install Dash**: In VSCode, open a new terminal (`Terminal` > `New Terminal`) and execute:

    ```bash
    pip install dash plotly
    ```


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

To run the app, open the terminal in VSCode and execute the command:

```bash
python hello_dash.py
```

The `debug=True` option in the `run()` method enables the app to run in debug mode. This mode provides useful features such as hot reloading (the app automatically reloads when you make changes to the code) and enhanced error logging.

Visit [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your web browser to see your Dash app running. If everything is set up correctly, you should see the greeting "Hello Dash!" displayed on the page.



<br>

**[← Previous](README.md) | [Next →](2_Dash_Components.md)**
---
