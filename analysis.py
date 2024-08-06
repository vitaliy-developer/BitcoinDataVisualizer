import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime

# Download historical Bitcoin data
end_date = datetime.now().strftime('%Y-%m-%d')  # Get the current date
btc_data = yf.download('BTC-USD', start='2009-01-01', end=end_date)

# Identify peaks and troughs
btc_data['High_Peak'] = btc_data['Close'][(btc_data['Close'].shift(1) < btc_data['Close']) & (btc_data['Close'].shift(-1) < btc_data['Close'])]
btc_data['Low_Peak'] = btc_data['Close'][(btc_data['Close'].shift(1) > btc_data['Close']) & (btc_data['Close'].shift(-1) > btc_data['Close'])]

# Create an interactive plot
fig = go.Figure()

# Add the closing price line
fig.add_trace(go.Scatter(x=btc_data.index, y=btc_data['Close'], mode='lines', name='BTC-USD Close Price', line=dict(color='blue')))

# Add peaks
fig.add_trace(go.Scatter(x=btc_data.index, y=btc_data['High_Peak'], mode='markers', name='High Peaks', marker=dict(color='green', symbol='triangle-up', size=10)))

# Add troughs
fig.add_trace(go.Scatter(x=btc_data.index, y=btc_data['Low_Peak'], mode='markers', name='Low Peaks', marker=dict(color='red', symbol='triangle-down', size=10)))

# Update the layout of the plot
fig.update_layout(
    title='Bitcoin Price History with Peaks and Troughs',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    legend_title='Legend',
    hovermode='x'
)

# Display the plot
fig.show()
