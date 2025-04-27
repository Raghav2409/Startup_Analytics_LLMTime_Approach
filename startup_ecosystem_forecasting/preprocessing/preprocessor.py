import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import adfuller

def check_stationarity(series):
    """Check if a time series is stationary using Augmented Dickey-Fuller test."""
    result = adfuller(series)
    return result[1] < 0.05  # p-value < 0.05 indicates stationarity

def remove_outliers(series, n_std=3):
    """Remove outliers using standard deviation method."""
    mean = series.mean()
    std = series.std()
    return series[(series > mean - n_std*std) & (series < mean + n_std*std)]

def preprocess_series(series):
    """Comprehensive preprocessing of time series data."""
    # 1. Handle missing values
    series = series.interpolate(method='time')
    
    # 2. Remove outliers using IQR method
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    series = series[(series >= Q1 - 1.5*IQR) & (series <= Q3 + 1.5*IQR)]
    
    # 3. Check and handle stationarity
    if not check_stationarity(series):
        print("Series is not stationary. Applying differencing...")
        series = series.diff().dropna()
        if not check_stationarity(series):
            print("Series is still not stationary after first differencing.")
            # Apply second differencing if needed
            series = series.diff().dropna()
    
    # 4. Normalize the data
    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(series.values.reshape(-1, 1))
    series = pd.Series(scaled_values.flatten(), index=series.index)
    
    return series, scaler

def preprocess_time_series(series, precision=3):
    """Preprocess time series data for LLMTime according to paper specifications."""
    # 1. Normalize the data to [0,1] range
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(series.values.reshape(-1, 1))
    
    # 2. Format numbers with specified precision
    formatted_data = [f"{x[0]:.{precision}f}" for x in scaled_data]
    
    # 3. Create context about the data
    context = f"This is a time series of {len(series)} weekly observations of the NASDAQ Composite Index, representing the health of the tech startup ecosystem. The values are normalized between 0 and 1, where higher values indicate a stronger ecosystem."
    
    return formatted_data, scaler, context 