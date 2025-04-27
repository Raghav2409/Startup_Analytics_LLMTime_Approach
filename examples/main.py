import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv

from startup_ecosystem_forecasting.data.loader import load_startup_data, analyze_startup_trends
from startup_ecosystem_forecasting.preprocessing.preprocessor import preprocess_series
from startup_ecosystem_forecasting.models.llmtime import optimize_llmtime_parameters
from startup_ecosystem_forecasting.models.arima import find_best_arima_params, evaluate_arima_model
from startup_ecosystem_forecasting.models.sarima import find_best_sarima_params, evaluate_sarima_model
from startup_ecosystem_forecasting.models.exponential_smoothing import evaluate_exponential_smoothing
from startup_ecosystem_forecasting.visualization.plotter import (
    setup_plotting_style,
    plot_predictions,
    plot_acf_pacf,
    plot_metrics_comparison,
    plot_quarterly_growth
)
from startup_ecosystem_forecasting.utils.metrics import calculate_metrics, compare_models

def main():
    # Load environment variables
    load_dotenv()
    
    # Set up plotting style
    setup_plotting_style()
    
    # Load startup ecosystem data
    print("Loading startup ecosystem data...")
    series = load_startup_data()
    
    # Analyze startup trends
    trends = analyze_startup_trends(series)
    plot_quarterly_growth(trends['quarterly_growth'])
    
    # Preprocess the data
    print("\nPreprocessing data...")
    series, scaler = preprocess_series(series)
    
    # Split into train and test sets (80-20 split)
    train_size = int(len(series) * 0.8)
    train = series[:train_size]
    test = series[train_size:]
    
    print(f"\nTraining size: {len(train)}, Test size: {len(test)}")
    
    # Plot the preprocessed data
    plot_predictions(train, test, None, 'Preprocessed Data', 'gray')
    
    # LLMTime predictions
    print("\nGetting LLMTime predictions...")
    llmtime_preds, llmtime_params, llmtime_error = optimize_llmtime_parameters(train, test)
    
    if llmtime_preds is not None:
        print(f"Best LLMTime RMSE: {llmtime_error:.4f}")
        print(f"Best parameters: {llmtime_params}")
        plot_predictions(train, test, llmtime_preds, 'LLMTime', 'purple')
    
    # Traditional models
    print("\nFitting traditional models...")
    
    # Plot ACF and PACF for ARIMA parameter selection
    print("\nPlotting ACF and PACF for ARIMA parameter selection...")
    plot_acf_pacf(train)
    
    # ARIMA
    print("\nFinding optimal ARIMA parameters...")
    best_order = find_best_arima_params(train)
    print(f"Best ARIMA order: {best_order}")
    
    try:
        print("Fitting ARIMA model...")
        arima_preds, _ = evaluate_arima_model(series, best_order)
        print("ARIMA model fitted successfully")
    except Exception as e:
        print(f"Error fitting ARIMA model: {e}")
        arima_preds = np.zeros(len(test))
    
    # SARIMA
    print("\nFinding optimal SARIMA parameters...")
    best_order, best_seasonal_order = find_best_sarima_params(train)
    print(f"Best SARIMA order: {best_order}, seasonal order: {best_seasonal_order}")
    
    try:
        print("Fitting SARIMA model...")
        sarima_preds, _ = evaluate_sarima_model(series, best_order, best_seasonal_order)
        print("SARIMA model fitted successfully")
    except Exception as e:
        print(f"Error fitting SARIMA model: {e}")
        sarima_preds = np.zeros(len(test))
    
    # Exponential Smoothing
    print("\nFitting Exponential Smoothing model...")
    try:
        exp_smooth_preds, _ = evaluate_exponential_smoothing(series)
        print("Exponential Smoothing model fitted successfully")
    except Exception as e:
        print(f"Error fitting Exponential Smoothing model: {e}")
        exp_smooth_preds = np.zeros(len(test))
    
    # Calculate metrics
    metrics = []
    
    if llmtime_preds is not None:
        metrics.append({
            'Model': 'LLMTime',
            **calculate_metrics(test.values, llmtime_preds)
        })
    
    metrics.extend([
        {
            'Model': 'ARIMA',
            **calculate_metrics(test.values, arima_preds)
        },
        {
            'Model': 'SARIMA',
            **calculate_metrics(test.values, sarima_preds)
        },
        {
            'Model': 'Exponential Smoothing',
            **calculate_metrics(test.values, exp_smooth_preds)
        }
    ])
    
    # Create metrics dataframe
    metrics_df = pd.DataFrame(metrics)
    print("\nPerformance Metrics:")
    print(metrics_df)
    
    # Compare models
    comparison = compare_models(metrics)
    print("\nBest Models:")
    for metric, (model, value) in comparison.items():
        print(f"{metric}: {model} ({value:.4f})")
    
    # Plot metrics comparison
    plot_metrics_comparison(metrics_df)
    
    # Plot all predictions
    plt.figure(figsize=(15, 8))
    plt.plot(train.index, train.values, label='Training Data', color='gray')
    plt.plot(test.index, test.values, label='True Values', color='black')
    plt.plot(test.index, arima_preds, label='ARIMA', color='blue')
    plt.plot(test.index, sarima_preds, label='SARIMA', color='green')
    plt.plot(test.index, exp_smooth_preds, label='Exponential Smoothing', color='orange')
    
    if llmtime_preds is not None:
        plt.plot(test.index, llmtime_preds, label='LLMTime', color='purple')
    
    plt.title('Time Series Predictions Comparison')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main() 