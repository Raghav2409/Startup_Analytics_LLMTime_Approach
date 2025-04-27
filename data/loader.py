import yfinance as yf
import pandas as pd

def load_startup_data():
    """Load and prepare startup funding data."""
    # Using NASDAQ Composite as a proxy for tech startup ecosystem health
    nasdaq = yf.download('^IXIC', start='2020-01-01', end='2024-01-01')
    series = nasdaq['Close']
    
    # Convert to weekly data to reduce noise
    series = series.resample('W').mean()
    
    # Ensure no missing values
    series = series.ffill()
    
    return series

def analyze_startup_trends(series):
    """Analyze startup ecosystem trends with enhanced visualizations."""
    print("\nStartup Ecosystem Analysis:")
    print(f"Time Period: {series.index[0].date()} to {series.index[-1].date()}")
    
    # Calculate growth
    total_growth = (series.iloc[-1] - series.iloc[0]) / series.iloc[0] * 100
    print(f"Total Growth: {float(total_growth):.2f}%")
    
    # Calculate weekly changes
    weekly_changes = series.pct_change().dropna()
    if isinstance(weekly_changes, pd.DataFrame):
        weekly_changes = weekly_changes.iloc[:, 0]
    avg_weekly_change = weekly_changes.mean() * 100
    weekly_std = weekly_changes.std() * 100
    print(f"Average Weekly Change: {float(avg_weekly_change):.2f}%")
    print(f"Volatility (Weekly Std): {float(weekly_std):.2f}%")
    
    # Calculate quarterly growth
    quarterly = series.resample('QE').mean()
    quarterly_growth = quarterly.pct_change().dropna() * 100
    print("\nQuarterly Growth Rates:")
    print(quarterly_growth)
    
    return {
        'total_growth': total_growth,
        'avg_weekly_change': avg_weekly_change,
        'weekly_std': weekly_std,
        'quarterly_growth': quarterly_growth
    } 