# Real-Time Stock Price Monitoring App

## Overview
This application is designed to fetch and display real-time stock price data using the Alpha Vantage API. It provides a user-friendly dashboard that updates every minute to show the latest stock prices for selected companies.

## Features
- **Real-Time Data Fetching**: Utilizes the Alpha Vantage API to retrieve real-time stock price data every minute.
- **Interactive Dashboard**: Built with Plotly Dash, the dashboard offers an interactive graph that displays the stock prices dynamically.
- **Stock Selection**: Users can select different stocks to view from a dropdown menu, which currently includes Microsoft (MSFT), Apple (AAPL), Google (GOOGL), and Amazon (AMZN).

## How It Works
1. **Data Fetching**: The application fetches the stock data using the Alpha Vantage API. This includes making an HTTP request to retrieve data which updates every minute.
2. **Data Processing**: The raw JSON data from the API is processed and converted into a pandas DataFrame. This data is then used to plot the stock price information.
3. **Dashboard Update**: The Dash app updates the graph in real-time at a set interval. This interval is defined to be 60 seconds, aligning with the frequency of data availability from the API.

## Setup and Installation
1. **Clone the repository**: Download the code to your local machine.
2. **Install dependencies**: Run `pip install -r requirements.txt` to install the required Python libraries.
3. **API Key Configuration**: You'll need to obtain a free API key from Alpha Vantage and replace `'your_api_key_here'` with your actual API key in the script.
4. **Running the Application**: Execute `python app.py` to start the server and access the dashboard through a web browser at `localhost:8050`.

## Technologies Used
- Python
- Pandas for data manipulation
- Plotly Dash for interactive dashboard creation
- Requests for API communication

This app serves as an excellent tool for anyone interested in monitoring stock prices in real-time. It demonstrates the ability to interface with external APIs, process data efficiently, and update a front-end interface dynamically.
