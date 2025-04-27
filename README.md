# Startup Ecosystem Forecasting

A Python package for analyzing and forecasting the health of the startup ecosystem using various time series methods.

## Features

- Multiple forecasting methods:
  - LLMTime: Leveraging Large Language Models for time series forecasting
  - ARIMA: AutoRegressive Integrated Moving Average
  - SARIMA: Seasonal ARIMA
  - Exponential Smoothing
- Comprehensive data preprocessing
- Visualization utilities
- Performance metrics calculation
- Easy-to-use API

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

## Documentation

For detailed documentation, please refer to the [docs](docs/) directory.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Ngruver for researching the Zero-shot learning method, LLMTime.

## Contact

For questions or support, please open an issue in the GitHub repository. 

# LLMTime vs Traditional Time Series Forecasting Methods

## 1. Synthetic Data Testing
- **Dataset**: Synthetically generated with both an overall **trend** (growth over time) and **seasonality** (repeating patterns).
  
<p align="center">
  <img width="882" alt="Synthetic Data - Trend and Seasonality" src="https://github.com/user-attachments/assets/4cf10793-48ea-43d2-ad64-8502db5d24b1" />
</p>

<p align="center">
  <img width="883" alt="Model Comparisons on Synthetic Data" src="https://github.com/user-attachments/assets/f1ed27c2-dd05-4b8d-a726-1fbc82f18e2e" />
</p>

<p align="center">
  <img width="879" alt="Forecasting Accuracy on Synthetic Data" src="https://github.com/user-attachments/assets/c74c3afa-4448-4406-8537-2dc8f919d6d3" />
</p>

- **Results**:
  - **LLMTime** demonstrated a superior fit compared to traditional models like **ARIMA** and **SARIMA**.
  - Captured both trend and seasonality more effectively.

---

## 2. Real-World Data Testing
- **Dataset**: Startup ecosystem's **periodic growth over four years** (Jan 2020 – Jan 2024).

<p align="center">
  <img width="849" alt="Startup Ecosystem Growth - Forecasting" src="https://github.com/user-attachments/assets/ff0668d5-2f41-440f-9763-aaaa3ce5f560" />
</p>

- **Results**:
  - **Performance Metrics**:
    - **MAE**: LLMTime achieved the lowest Mean Absolute Error, outperforming ARIMA and SARIMA.
    - **RMSE**: LLMTime showed marginal improvement; differences with ARIMA/SARIMA were minimal.
  - **Conclusion**: LLMTime provided better or comparable forecasts across key metrics.

---

## Final Conclusion
- On **synthetic data**, LLMTime significantly outperformed traditional models in capturing trend and seasonality.
- On **real-world data**, LLMTime consistently achieved better results based on MAE, and comparable results based on RMSE.
- **LLMTime shows strong generalization capabilities** across both controlled and real-world scenarios.
