import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def find_best_arima_params(series, max_p=3, max_d=2, max_q=3):
    """Find optimal ARIMA parameters using AIC."""
    best_aic = float("inf")
    best_order = None
    
    for p in range(max_p + 1):
        for d in range(max_d + 1):
            for q in range(max_q + 1):
                try:
                    model = ARIMA(series, order=(p,d,q))
                    results = model.fit()
                    aic = results.aic
                    
                    if aic < best_aic:
                        best_aic = aic
                        best_order = (p,d,q)
                        
                except:
                    continue
                    
    return best_order

def evaluate_arima_model(series, order, train_size=0.8):
    """Evaluate ARIMA model using walk-forward validation."""
    train_size = int(len(series) * train_size)
    train, test = series[:train_size], series[train_size:]
    
    history = [x for x in train]
    predictions = []
    
    for t in range(len(test)):
        model = ARIMA(history, order=order)
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
        
    return predictions, test.values

def fit_arima_model(train, order):
    """Fit ARIMA model and return fitted model."""
    try:
        model = ARIMA(train, order=order)
        model_fit = model.fit()
        return model_fit
    except Exception as e:
        print(f"Error fitting ARIMA model: {e}")
        return None 