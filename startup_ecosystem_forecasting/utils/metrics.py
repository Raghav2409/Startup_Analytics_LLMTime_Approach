
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(true_values, predictions):
    """Calculate performance metrics."""
    mae = mean_absolute_error(true_values, predictions)
    rmse = np.sqrt(mean_squared_error(true_values, predictions))
    r2 = r2_score(true_values, predictions)
    return {
        'MAE': mae,
        'RMSE': rmse,
        'R2': r2
    }

def compare_models(metrics_list):
    """Compare multiple models based on their metrics."""
    best_mae = float('inf')
    best_rmse = float('inf')
    best_r2 = -float('inf')
    best_mae_model = None
    best_rmse_model = None
    best_r2_model = None
    
    for metrics in metrics_list:
        if metrics['MAE'] < best_mae:
            best_mae = metrics['MAE']
            best_mae_model = metrics['Model']
            
        if metrics['RMSE'] < best_rmse:
            best_rmse = metrics['RMSE']
            best_rmse_model = metrics['Model']
            
        if metrics['R2'] > best_r2:
            best_r2 = metrics['R2']
            best_r2_model = metrics['Model']
    
    return {
        'Best MAE': (best_mae_model, best_mae),
        'Best RMSE': (best_rmse_model, best_rmse),
        'Best R2': (best_r2_model, best_r2)
    } 