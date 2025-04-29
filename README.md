# Startup Ecosystem Forecasting

A Python package for analyzing and forecasting the health of the startup ecosystem using various time series analysis methods, including a **Zero-shot learning method, LLMTime**

## Features

- Multiple forecasting methods:
  - LLMTime: Leveraging Large Language Models for time series forecasting
  - ARIMA: AutoRegressive Integrated Moving Average
  - SARIMA: Seasonal ARIMA
  - Exponential Smoothing (Holt Winters)
- Comprehensive data preprocessing
- Large Language Models (OpenAI)
- Visualization
- Performance metrics calculation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/startup_ecosystem_forecasting.git
   cd startup_ecosystem_forecasting
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package:
   ```bash
   pip install -e .
   ```

## Usage

1. Create a `.env` file in the examples directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

2. Run the example script:
   ```bash
   python examples/main.py
   ```

## Project Structure

```
startup_ecosystem_forecasting/
├── startup_ecosystem_forecasting/
│   ├── data/
│   │   └── loader.py
│   ├── models/
│   │   ├── llmtime.py
│   │   ├── arima.py
│   │   ├── sarima.py
│   │   └── exponential_smoothing.py
│   ├── preprocessing/
│   │   └── preprocessor.py
│   ├── visualization/
│   │   └── visualizer.py
│   ├── utils/
│   │   └── metrics.py
│   └── __init__.py
├── examples/
│   ├── main.py
│   └── .env.example
├── tests/
├── docs/
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── requirements.txt
└── setup.py
```

## LLMTime vs Traditional Time Series Forecasting Methods

I conducted a comprehensive evaluation of the **LLMTime** model against traditional time series forecasting methods, using both **synthetic** and **real-world** datasets.

### 1. Synthetic Dataset

- **Dataset**: Artificially generated with both a **trend** (growing pattern) and **seasonality** (repeating up-and-down cycles).
- **Models Compared**:
  - LLMTime (Zero-shot forecasting with LLMs)
  - ARIMA
  - SARIMA

**Visual Comparison:**

<p align="center">
  <img width="882" alt="Synthetic - Fit Comparison 1" src="https://github.com/user-attachments/assets/4cf10793-48ea-43d2-ad64-8502db5d24b1" />
</p>

<p align="center">
  <img width="883" alt="Synthetic - Fit Comparison 2" src="https://github.com/user-attachments/assets/f1ed27c2-dd05-4b8d-a726-1fbc82f18e2e" />
</p>

<p align="center">
  <img width="879" alt="Synthetic - Fit Comparison 3" src="https://github.com/user-attachments/assets/c74c3afa-4448-4406-8537-2dc8f919d6d3" />
</p>

**Findings**:
- **LLMTime** demonstrated a significantly better fit to the data compared to ARIMA and SARIMA.
- It captured both trend and seasonal patterns more naturally without heavy manual tuning.

---

### 2. Real-World Dataset

- **Dataset**: Startup ecosystem growth data over **4 years** (Jan 2020 – Jan 2024).
- **Models Compared**:
  - LLMTime
  - ARIMA
  - SARIMA
  - Exponential Smoothing

**Visual Comparison:**

<p align="center">
  <img width="849" alt="Real-World Startup Data Comparison" src="https://github.com/user-attachments/assets/ff0668d5-2f41-440f-9763-aaaa3ce5f560" />
</p>

**Findings**:
- Based on **Mean Absolute Error (MAE)**, **LLMTime** outperformed all traditional models.
- Based on **Root Mean Squared Error (RMSE)**, the margin between LLMTime and ARIMA/SARIMA was marginal

---

### Conclusion

- **Synthetic Data**: LLMTime achieves superior generalization to patterns **without needing exhaustive hyperparameter tuning or model pretraining**.
- **Real-World Data**: LLMTime delivers competitive and often better performance than traditional models, offering a strong new approach for startup ecosystem forecasting.


## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Ngruver for researching the Zero-shot learning method, LLMTime.

## Contact

For questions or support, please open an issue in the GitHub repository. 
