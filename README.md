# saucedemo_tests

Automated test suite covering:
- UI tests for [SauceDemo](https://www.saucedemo.com/) using Playwright (login, add to cart, cart verification)


## Prerequisites
- Python 3.10+
- Git

## Setup

1. Clone the repository:

   git clone https://github.com/Wadie11/saucedemo_tests.git
   cd saucedemo_tests


2. Create and activate a virtual environment:

   python -m venv venv
   # Windows
   venv\Scripts\activate


3. Install dependencies:

   python -m playwright install


## Running the tests

Run all tests:

pytest -v

pytest test_app.py -v --headed

Omit `--headed` to run headless.

