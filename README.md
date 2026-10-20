# SauceDemo Automation Testing

Automated UI testing framework for SauceDemo using Python, Playwright, Pytest, and Page Object Model (POM).

## Technologies Used
- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest HTML Reports

## Test Coverage

| Module | Tests |
|---|---|
| Login | 6 |
| Shopping Cart | 4 |
| Checkout | 4 |
| Total | 14 |

## Features
- Positive and negative test scenarios
- Data-driven testing using parametrization
- Reusable Page Object Model classes
- Automated screenshots on test failures
- HTML test execution reports

## Installation

1. Install dependencies: pip install -r requirements.txt
2. Install browser: python -m playwright install chromium

## Run Tests

python -m pytest tests/ -v

## Generate HTML Report

python -m pytest tests/ -v --html=report.html --self-contained-html

## Latest Test Results

14 tests passed.

## Application Under Test

https://www.saucedemo.com/
