
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def setup_plotting_style():
    """Set up enhanced visualization styles."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = [14, 8]
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['legend.fontsize'] = 12
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False

def plot_predictions(train, test, preds, model_name, color, uncertainty=None):
    """Plot time series predictions."""
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train.values, label='Training Data', color='gray')
    plt.plot(test.index, test.values, label='True Values', color='black')
    plt.plot(test.index, preds, label=model_name, color=color)
    
    if uncertainty is not None:
        lower, upper = uncertainty
        plt.fill_between(test.index, lower, upper, alpha=0.3, color=color, label='90% CI')
    
    plt.title(f'{model_name} Predictions')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_acf_pacf(series, lags=20):
    """Plot ACF and PACF for ARIMA parameter selection."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    plot_acf(series, lags=lags, ax=ax1)
    plot_pacf(series, lags=lags, ax=ax2)
    plt.tight_layout()
    plt.show()

def plot_metrics_comparison(metrics_df):
    """Plot comparison of model metrics."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    metrics_df.set_index('Model').plot(kind='bar', subplots=True, ax=axes, rot=45)
    plt.tight_layout()
    plt.show()

def plot_quarterly_growth(quarterly_growth):
    """Plot quarterly growth rates."""
    plt.figure(figsize=(12, 4))
    quarterly_growth.plot(kind='bar')
    plt.title('Quarterly Growth Rates')
    plt.xlabel('Quarter')
    plt.ylabel('Growth Rate (%)')
    plt.grid(True)
    plt.show() 