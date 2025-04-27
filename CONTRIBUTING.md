# Contributing to Startup Ecosystem Forecasting

Thank you for your interest in contributing to this project! This document provides guidelines and steps for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button on the repository page
   - Clone your forked repository to your local machine

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the project's coding style
   - Add tests for new features
   - Update documentation as needed

4. **Commit Your Changes**
   ```bash
   git commit -m "Description of your changes"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Add a description of your changes
   - Submit the pull request

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Testing

Before submitting a pull request, please ensure:
- All tests pass
- Code coverage is maintained or improved
- Documentation is updated

## Style Guide

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for all public functions and classes
- Keep functions focused and small

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions and classes
- Update examples if API changes

## Questions?

Feel free to open an issue if you have any questions about contributing! 