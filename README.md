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

## LLMTime Vs Traditional Time Series Forecasting Methods

Model Testing on synthetically generated data with both a trend (growing overall) and seasonality (repeating up and down patterns).
<img width="882" alt="Screenshot 2025-04-27 at 2 45 52 AM" src="https://github.com/user-attachments/assets/4cf10793-48ea-43d2-ad64-8502db5d24b1" />
<img width="883" alt="Screenshot 2025-04-27 at 2 46 20 AM" src="https://github.com/user-attachments/assets/f1ed27c2-dd05-4b8d-a726-1fbc82f18e2e" />
<img width="879" alt="Screenshot 2025-04-27 at 2 45 14 AM" src="https://github.com/user-attachments/assets/c74c3afa-4448-4406-8537-2dc8f919d6d3" />

As evident LLMTime model has a better fit compared to the ARIMA & SARIMA models for Time Series Forecasting


Model Testing on real-world data for startup ecosystem periodic growth in 4 years (Jan 2020 - Jan 2024)
<img width="849" alt="Screenshot 2025-04-27 at 2 48 33 AM" src="https://github.com/user-attachments/assets/ff0668d5-2f41-440f-9763-aaaa3ce5f560" />

As per the performance metric, MAE, LLMTime beat all other models, while RMSE suggests a similar performance compared to ARIMA & SARIMA models
