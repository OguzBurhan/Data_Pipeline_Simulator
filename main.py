import requests
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

# Function to fetch financial data from Alpha Vantage API
def fetch_financial_data(symbol='MSFT'):
    API_KEY = 'MIP2F80PW0X3AZZV'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        # Check if the required data is in the response
        if 'Time Series (1min)' in data:
            return data
        else:
            print("Error fetching data:", data.get('Note', 'Unknown Error'))
            return None
    except requests.RequestException as e:
        print("HTTP Request failed:", e)
        return None

# Fetch real-time data (example usage)
real_time_data = fetch_financial_data()

# Process the API data into a pandas DataFrame
def process_data(api_data):
    if api_data and 'Time Series (1min)' in api_data:
        df = pd.DataFrame(api_data['Time Series (1min)']).T.astype(float)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index = pd.to_datetime(df.index)
        return df
    else:
        return pd.DataFrame()  # Return an empty DataFrame if there's an issue

# Process fetched data (example processing)
processed_data = process_data(real_time_data)

# Setup the Dash application
app = Dash(__name__)

# Define the layout of the Dash application
app.layout = html.Div([
    html.H1("Real-Time Stock Price Monitoring"),
    dcc.Dropdown(  # Dropdown for selecting stock symbols
        id='symbol-selector',
        options=[{'label': s, 'value': s} for s in ['MSFT', 'AAPL', 'GOOGL', 'AMZN']],
        value='MSFT'
    ),
    dcc.Graph(id='live-update-graph'),  # Graph for displaying the real-time data
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Update interval in milliseconds
        n_intervals=0
    )
])

# Callback function to update the graph based on the dropdown selection
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals'),
     Input('symbol-selector', 'value')])
def update_graph_live(n, symbol):
    real_time_data = fetch_financial_data(symbol)
    processed_data = process_data(real_time_data)
    # Plot the processed data
    fig = go.Figure(data=[
        go.Scatter(x=processed_data.index, y=processed_data['close'], mode='lines+markers')
    ])
    fig.update_layout(title=f'Real-Time Price for {symbol}')
    return fig

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
