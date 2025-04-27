import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def find_best_sarima_params(series, seasonal_period=4):
    """Find optimal SARIMA parameters using AIC."""
    best_aic = float("inf")
    best_order = None
    best_seasonal_order = None
    
    # Grid search for non-seasonal parameters
    for p in range(2):
        for d in range(2):
            for q in range(2):
                # Grid search for seasonal parameters
                for P in range(2):
                    for D in range(2):
                        for Q in range(2):
                            try:
                                model = SARIMAX(
                                    series,
                                    order=(p,d,q),
                                    seasonal_order=(P,D,Q,seasonal_period)
                                )
                                results = model.fit(disp=False)
                                aic = results.aic
                                
                                if aic < best_aic:
                                    best_aic = aic
                                    best_order = (p,d,q)
                                    best_seasonal_order = (P,D,Q,seasonal_period)
                                    
                            except:
                                continue
                                
    return best_order, best_seasonal_order

def evaluate_sarima_model(series, order, seasonal_order, train_size=0.8):
    """Evaluate SARIMA model using walk-forward validation."""
    train_size = int(len(series) * train_size)
    train, test = series[:train_size], series[train_size:]
    
    history = [x for x in train]
    predictions = []
    
    for t in range(len(test)):
        model = SARIMAX(history, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
        
    return predictions, test.values

def fit_sarima_model(train, order, seasonal_order):
    """Fit SARIMA model and return fitted model."""
    try:
        model = SARIMAX(train, order=order, seasonal_order=seasonal_order)
        model_fit = model.fit(disp=False)
        return model_fit
    except Exception as e:
        print(f"Error fitting SARIMA model: {e}")
        return None 