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

- Thanks to all contributors who have helped shape this project
- Special thanks to the open-source community for their valuable tools and libraries

## Contact

For questions or support, please open an issue in the GitHub repository. 