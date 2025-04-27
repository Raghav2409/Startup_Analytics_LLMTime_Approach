import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def evaluate_exponential_smoothing(series, seasonal_period=4, train_size=0.8):
    """Evaluate Holt-Winters exponential smoothing."""
    train_size = int(len(series) * train_size)
    train, test = series[:train_size], series[train_size:]
    
    # Fit the model
    model = ExponentialSmoothing(
        train,
        seasonal_periods=seasonal_period,
        trend='add',
        seasonal='add'
    )
    model_fit = model.fit()
    
    # Make predictions
    predictions = model_fit.forecast(len(test))
    
    return predictions, test.values

def fit_exponential_smoothing(train, seasonal_period=4):
    """Fit Exponential Smoothing model and return fitted model."""
    try:
        model = ExponentialSmoothing(
            train,
            seasonal_periods=seasonal_period,
            trend='add',
            seasonal='add'
        )
        model_fit = model.fit()
        return model_fit
    except Exception as e:
        print(f"Error fitting Exponential Smoothing model: {e}")
        return None 